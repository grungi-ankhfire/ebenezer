# -*- coding:utf-8 -*-
# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
import datetime

from ..data import Transaction
from .. import data
from ..log import *

class SubTransfer():

    def __init__(self, app):
        self.app = app
        self.account = app.active_account
        now = datetime.datetime.today()
        currency = "EUR"
        if self.account is not None:
            currency = "EUR" #self.account.currency


        self.questions = [["Transfer description ", str, "Transfer"],\
                          ["Transfer date  ", str, "%0#4i%0#2i%0#2i" % (now.year, now.month, now.day)],\
                          ["Transfer amount ", float, None],\
                          ["Currency symbol ", str, currency],\
                          ["To which account? ", int, None]]


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
  
        for a in data.accounts:
          if self.answers[4] == a.id and self.answers[4] != self.account.id:
            new_transaction = Transaction(date=self.answers[1],
                                          amount=-self.answers[2],
                                          currency=self.answers[3],
                                          category=None,
                                          description=self.answers[0],
                                          from_account=self.account.id,
                                          to_account=self.answers[4],
                                          person=None)            

            log("Adding transfer from account " + str(self.account.id) + " to account " + str(self.answers[4]), component="SubNewTransaction")
        
        data.transactions.append(new_transaction)
