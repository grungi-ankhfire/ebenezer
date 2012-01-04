# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

import sys
import os
from ebenezer.parser import EbeParser
from ebenezer.ebenezer import Ebenezer

def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) > 1:
        for a in argv[1:]:
            parser = EbeParser(a)

    app = Ebenezer(parser)
    return app.run()


if __name__ == "__main__":
    sys.exit(main())
