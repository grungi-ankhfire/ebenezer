# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

# Log verbosity levels
MUTE    = 0
NORMAL  = 1
DEBUG   = 2
DEFAULT = 2

_VERBOSITY_LEVEL = DEFAULT 

_LOG_FILE = "ebenezer.log"
_LOG_STREAM = None

def log_init(log_file = _LOG_FILE):
    global _LOG_STREAM
    try:
        _LOG_STREAM=open(log_file, 'w')
    except IOError:
        print "I/O error: cannot open ", log_file 
        print "Disbling logging."
        _VERBOSITY_LEVEL = MUTE

def log(message, verbosity_level=DEFAULT, component=None, type = "INFO"):
    if _VERBOSITY_LEVEL == MUTE or verbosity_level > _VERBOSITY_LEVEL:
        return
    string = ""
    if component is not None:
        string += "[" + str(component) + "] "
    if type is not None:
        string += "[" + str(type) + "] "
    _LOG_STREAM.write(string + str(message) + "\n")

