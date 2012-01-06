# -*- coding:utf-8 -*-
# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from ..section import EbeSection

class SubDelAccount():

    def __init__(self, accounts):
        self.accounts = accounts
        self.questions = [["Account number ", int, None]]

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
        
        num = self.answers[0]-1
        if num >= 0 and num < len(self.accounts):
            self.accounts.remove(self.accounts[num])

