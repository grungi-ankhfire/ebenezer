# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

import yaml

import data
from data import Account, Transaction

from log import *
from config import *



def logio(message, type="INFO"):
    log(message, component="I/O", type=type)

def load(filename):

    try:
        f = file(filename, 'r')
        filedata = yaml.load(f)
    except IOError as e:
        logio("Error loading file " + filename, type="ERROR")
        return

    ebe_info = filedata['software']
    ebe_version = ebe_info['version']
    ebe_version = str(ebe_version[0]) + "." + str(ebe_version[1]) + "." + str(ebe_version[2])
    ebe_fileversion = ebe_info['file_format']
    ebe_fileversion = str(ebe_fileversion[0]) + "." + str(ebe_fileversion[1])

    logio("Reading file " + filename)
    logio("Ebenezer version " + ebe_version)
    logio("File format version " + ebe_fileversion)

    print filedata

    data.accounts = filedata['accounts']
    data.transactions = filedata['transactions']


    


def save(filename):
    try:
        f = file(filename, 'w')
    except:
        logio("Error opening file " + filename + " for writing", type="ERROR")
        return

    # Dump each section in the order we want to see 
    filedata = {}
    filedata['software'] = dumpSoftwareInfo()
    yaml.dump(filedata, f, default_flow_style=False)
    filedata = {}
    filedata['accounts'] = data.accounts
    yaml.dump(filedata, f, default_flow_style=False)
    filedata = {}
    filedata['transactions'] = data.transactions
    yaml.dump(filedata, f, default_flow_style=False)
