# -*- coding:utf-8 -*-
# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
import datetime

from ..data import Transaction
from .. import data
from ..log import *

class SubNewTransaction():

    def __init__(self, app):
        self.app = app
        self.account = app.active_account
        now = datetime.datetime.today()
        currency = "€"
        if self.account is not None:
            currency = "€" #self.account.currency


        self.questions = [["Transaction name ", str, "Various"],\
                          ["Transaction date  ", str, "%0#4i%0#2i%0#2i" % (now.year, now.month, now.day)],\
                          ["Transaction amount ", float, None],\
                          ["Person concerned ", str, "you"],\
                          ["Currency symbol ", str, currency],\
                          ["Category ", str, "General"]]


    def display(self):
        self.account = self.app.active_account
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

        if self.answers[3] != "" and self.answers[3] != "you":
            person = self.answers[3]
        else:
            person = None

        new_transaction = Transaction(date=self.answers[1],
                                      amount=self.answers[2],
                                      currency=self.answers[4],
                                      category=self.answers[5],
                                      description=self.answers[0],
                                      from_account=self.account.id,
                                      to_account=None,
                                      person=person)


        log("Adding transaction with from_account id " + str(self.account.id), component="SubNewTransaction")
        data.transactions.append(new_transaction)
        # sec = EbeSection()
        # sec.type = "TRANSACTION"
        # sec.props["name"] = self.answers[0]
        # sec.props["date"] = self.answers[1]
        # sec.props["amount"] = self.answers[2]
        # if self.answers[3] != "" and self.answers[3] != "you":
        #     sec.props["person"] = self.answers[3]
        #     sec.props_type["person"] = "s"

        # sec.props["currency"] = self.answers[4]
        # sec.props["category"] = self.answers[5]
        # sec.props_type["name"] = "s"
        # sec.props_type["date"] = "i"
        # sec.props_type["amount"] = "f"
        # sec.props_type["currency"] = "s"
        # sec.props_type["category"] = "s"

        # self.account.children.append(sec)
