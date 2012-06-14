# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

import sys
import os
import getopt

from ebenezer.parser import EbeParser
from ebenezer.ebenezer import Ebenezer
from ebenezer.io import *
from ebenezer.log import *

def main(argv=None):
    if argv is None:
        argv = sys.argv

    log_init()

    if len(argv) > 1:

        load(argv[1])
        log("Loaded file", component="Main")
        for a in argv[1:]:
            parser = EbeParser(a)
            if parser.successfull:
                parser.write_file(parser.filename+".backup")
                break
    else:
        parser = EbeParser(None)

    app = Ebenezer(parser)
    return app.run()


if __name__ == "__main__":
    sys.exit(main())
