# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

version = [0,2,0]
file_format = [0,2]

def getVersionString():
    return str(version[0])+"."+str(version[1])+"."+str(version[2])

def getFileFormatVersionString():
    return str(file_format[0])+"."+str(file_format[1])

def dumpSoftwareInfo():
    data = {}
    data['version'] = version
    data['file_format'] = file_format
    return data
