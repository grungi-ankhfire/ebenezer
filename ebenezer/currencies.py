# -*- coding: utf-8 -*-
# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

from log import *

# TODO : Use a webservice to translate between currencies

symbols = {'€':'EUR',
           '$':'USD',
           '£':'GBP',
           '¥':'JPY'}

def get_string(symbol):
    if symbol in symbols:
        return symbols[symbol]
    else:
        log('Unknown symbol : ' + str(symbol), component="currencies")