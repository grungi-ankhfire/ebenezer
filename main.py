# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

import sys
import os
import getopt

from ebenezer.config import *
from ebenezer.parser import EbeParser
from ebenezer.ebenezer import Ebenezer
from ebenezer.io import *
from ebenezer.log import *
from ebenezer import data

def parse_options(argv):
    if argv is None:
            argv = sys.argv

    options, remainder = getopt.getopt(argv[1:], '', ['version'])

    for opt, arg in options:
            if opt in ('--version'):
                print "Ebenezer version " + getVersionString()
                sys.exit(0)

    return remainder


def processFile(files):
    for item in files:
        load(item)
        save(item + ".backup")
    # TODO Add success checks in io, and error handling



#------------------------------------------------------------------------------
def main(argv=None):

    global accounts
    files = parse_options(argv)

    log_init()

    log("Starting Ebenezer version " + getVersionString(), component="Main")
    log("Using file format version " + getFileFormatVersionString(), component="Main")
    
    processFile(files)

    print data.accounts

    app = Ebenezer()
    return app.run()

if __name__ == "__main__":
    sys.exit(main())
