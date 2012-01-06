# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

from section import EbeSection

class EbeParser():
    def __init__(self, filename):

        self.version = (0,1)
        self.sections = []
        self.delimiters = ["@@", "++", "{{"]
        self.types = {"i":int, "s":str, "f":float}

        if filename is not None:
            print "Opening file..." + filename
        try:
            self.f = open(filename)
        except:
            print "[ERROR] Couldn't open file " + str(filename)
            filename = None
        if filename is not None:
            contents = self.f.readlines()
            self.scan_for_section(contents, lookfor="EBENEZER")
            if len(self.sections) > 0:
                print "Found a valid file !"
                self.scan_for_section(contents, lookfor="ACCOUNT")
                print "Found " + str(len(self.sections) - 1) + " accounts."
            self.f.close()
            

    def get_num_accounts(self):
        num = 0
        for s in self.sections:
            if s.type == "ACCOUNT":
                num += 1
        return num
    
    def get_accounts(self):
        accs = []
        for s in self.sections:
            if s.type == "ACCOUNT":
                accs.append(s)
        return accs

    def scan_for_section(self, lines, lookfor=None):
        count = -1
        for l in lines:
            count+=1
            prefix = ""
            if len(l) > 3:
                prefix = l[0:2]
                if prefix in self.delimiters:
                    tok = l.split()
                    if lookfor is not None and tok[1] != lookfor:
                        continue
                    self.parse_section(lines[count:])
                                       

    def parse_section(self, lines, father = None):
        depth = 0
        tok = lines[0].split()
        name = tok[1]
        if tok[0] == "{{": tok[0] = "}}"
        delim = [tok[0]]
        print "Parsing section " + name
        
        section = EbeSection()
        section.type = name

        

        count = 0
        for l in lines[1:]:
            #print delim
            if depth < 0:
                print "----Done----"
                break
            count+=1
            tok = l.split()
            #print depth, tok
            if l[0] == "#" or len(tok) == 0:
                continue

            if tok[0] in self.delimiters and len(tok) > 1:
                depth += 1
                delim.append(tok[0])
                self.parse_section(lines[count:], father = section)
                continue

            if tok[0] == delim[len(delim)-1]:
                depth -= 1
                if len(delim) > 0:
                    delim.pop()
                continue

            if depth == 0:
                prop_name = tok[1]
                section.props_type[prop_name] = tok[0]
                if tok[0] == "s":
                    buf = ""
                    for t in tok[2:]:
                        buf = buf + t + " "
                    buf = buf.strip()
                    section.props[prop_name] = buf
                else:
                    section.props[prop_name] = self.types[tok[0]](tok[2])
                section.props_type[prop_name] = tok[0]
                print "  Stored property " + prop_name + " with value " + str(section.props[prop_name])

        if father is None:
            self.sections.append(section)
        else:
            father.children.append(section)

    def write_section(self, f, s):
        if s.type == "ACCOUNT":
            f.write("{{ " + s.type + "\n")
        else:
            f.write("++ " + s.type + "\n")

        for p in s.props.keys():
            f.write(s.props_type[p] + " " + p + " " + str(s.props[p]) + "\n")
            for c in s.children:
                self.write_section(f, c)

        if s.type == "ACCOUNT":
            f.write("}}\n")
        else:
            f.write("++\n")        

    def write_file(self, filename):
        f = open(filename, 'w')

        # Header section
        f.write("@@ EBENEZER\n")
        f.write("s version 0.1")
        f.write("s format " + str(self.version[0]) + "." +str(self.version[1]) + "\n")
        f.write("@@\n\n")

        for s in self.sections:
            self.write_section(f, s)
        f.close()
