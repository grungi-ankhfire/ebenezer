# -*- coding:utf-8 -*-
# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
import datetime

from ..section import EbeSection

class SubNewTransaction():

    def __init__(self, account):
        self.account = account
        now = datetime.datetime.today()
        currency = "€"
        if self.account is not None:
            currency = self.account.props["currency"]


        self.questions = [["Transaction name ", str, "Various"],\
                          ["Transaction date  ", str, "%0#4i%0#2i%0#2i" % (now.year, now.month, now.day)],\
                          ["Transaction amount ", float, None],\
                          ["Currency symbol ", str, currency]]

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

        sec = EbeSection()
        sec.type = "TRANSACTION"
        sec.props["name"] = self.answers[0]
        sec.props["date"] = self.answers[1]
        sec.props["amount"] = self.answers[2]
        sec.props["currency"] = self.answers[3]
        sec.props_type["name"] = "s"
        sec.props_type["date"] = "i"
        sec.props_type["amount"] = "f"
        sec.props_type["currency"] = "s"

        self.account.children.append(sec)
