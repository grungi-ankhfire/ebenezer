# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

import yaml

accounts = []
transactions = []
active_file = None


class Account(yaml.YAMLObject):
    yaml_tag = u'!Account'
    def __init__(self, name, initial_balance, currency, id):
        self.name = name
        self.initial_balance = initial_balance
        self.currency = currency
        self.id = id

    def __repr__(self):
        return "%s(name=%r, initial_balance=%r, currency=%r, id=%r)" % (
            self.__class__.__name__, self.name, self.initial_balance, self.currency, self.id)


class Transaction(yaml.YAMLObject):
    yaml_tag = u'!Transaction'
    def __init__(self, date, amount, currency, category=None, description=None, from_account=None, to_account=None, person=None):
        self.date = date
        self.amount = amount
        self.currency = currency
        self.category = category
        self.description = description
        self.from_account = from_account
        self.to_account = to_account
        self.person = person

    def __repr__(self):
        return "%s(date=%r, amount=%r, currency=%r, category=%r, description=%r, from_account=%r, to_account=%r, person=%r)" % (
            self.__class__.__name__, self.date, self.amount, self.currency, self.category, self.description, \
            self.from_account, self.to_account, self.person)