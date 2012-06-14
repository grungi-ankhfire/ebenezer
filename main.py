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

def parse_options(argv):
    if argv is None:
            argv = sys.argv

    options, remainder = getopt.getopt(argv[1:], '', ['version'])

    for opt, arg in options:
            if opt in ('--version'):
                print "Ebenezer version " + getVersionString()
                sys.exit(0)

    parser = None
    for item in remainder:
        parser = EbeParser(item)
        if parser.successful:
            parser.write_file(parser.filename+".backup")
            break
    if parser is None or not parser.successful:
        parser = EbeParser(None)

    return parser

#------------------------------------------------------------------------------
def main(argv=None):

    parser = parse_options(argv)

    log_init()

    app = Ebenezer(parser)
    return app.run()

if __name__ == "__main__":
    sys.exit(main())
