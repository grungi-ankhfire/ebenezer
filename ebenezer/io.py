# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

import yaml

from log import *

class Contents:

    def __init__(self):
        self.accounts = None
        self.transactions = None

def load(filename):
    try:
        f = open(filename, 'r')
        text = f.read()
        data = yaml.safe_load(text)
    except:
        log("Error loading file " + filename, component="I/O", type="ERROR")
        return
    ebe_info = data['software']
    ebe_version = ebe_info['version']
    ebe_version = str(ebe_version[0]) + "." + str(ebe_version[1]) + "." + str(ebe_version[2])
    ebe_fileversion = ebe_info['file_format']
    ebe_fileversion = str(ebe_fileversion[0]) + "." + str(ebe_fileversion[1])

    log("Reading file " + filename, component="I/O")
    log("Ebenezer version " + ebe_version, component="I/O")
    log("File format version " + ebe_fileversion, component="I/O")

