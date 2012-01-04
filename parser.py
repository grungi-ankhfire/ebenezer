# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

from section import EbeSection

class EbeParser():
    def __init__(self, filename):
        #try:
            print "Opening file..." + filename
            self.f = open(filename)
            self.sections = []

            self.delimiters = ["@@", "++", "{{"]
            self.types = {"i":int, "s":str, "f":float}
            
            contents = self.f.readlines()

            self.scan_for_section(contents, lookfor="EBENEZER")
            if len(self.sections) > 0:
                print "Found a valid file !"
                self.scan_for_section(contents, lookfor="ACCOUNT")
                print "Found " + str(len(self.sections) - 1) + " accounts."

        #except:
        #    print "Couldn't read file " + filename


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

                print "  Stored property " + prop_name + " with value " + str(section.props[prop_name])

        if father is None:
            self.sections.append(section)
        else:
            father.children.append(section)
