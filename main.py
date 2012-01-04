# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

import sys
import os
from parser import EbeParser

def print_menu():
    os.system("clear")
    print "   Ebenezer Personal Accounting System"
    print "-------------[ Main Menu ]---------------"
    print ""
    print "[A]ccess transaction list"
    print "Add a [T]ransaction"
    print "[V]iew account status"
    print "[Q]uit"
    print ""

def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) > 1:
        for a in argv[1:]:
            parser = EbeParser(a)

    possible_actions = ["A", "T", "V", "Q"]
    choice = "nothing"

    while choice.upper() not in possible_actions:
        print_menu()
        choice = raw_input("What do you want to do ? ")

    if choice.upper() == "Q":
        print "Exiting..."
        return 1
    else:
        print "You chose something else :)"

if __name__ == "__main__":
    sys.exit(main())
