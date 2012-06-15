# -*- coding:utf-8 -*-
# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

from ..section import EbeSection
from .. import data
from ..data import Account

class SubNewAccount():

    def __init__(self, accounts):
        self.accounts = accounts
        
        self.questions = [["Account name ", str, "New account"],\
                          ["Initial balance  ", float, 0],\
                          ["Currency symbol ", str, "€"]]

    def display(self):
        self.answers = []
        for q in self.questions:
            string = q[0]
            if q[2] is not None:
                string += "["+str(q[2])+"] "
            ans = raw_input(string)
            if ans == "" and q[2] is not None:
                ans = q[2]
            ok = False
            while not ok and q[2] is None:
                try:
                    ans = q[1](ans)
                    ok = True
                except:
                   ans = raw_input(string)

            self.answers.append(ans)

        new_account = Account(name=self.answers[0],
                              initial_balance=self.answers[1],
                              currency=self.answers[2])

        data.accounts.append(new_account)
