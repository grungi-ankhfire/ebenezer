# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from menu import Menu
from sub_transaction import SubNewTransaction
from sub_del_transaction import SubDelTransaction
from .. import data


class AccountTransactionsMenu(Menu):

    def __init__(self, app, account):
        Menu.__init__(self, app)
        self.account = account


        self.header = ["Ebenezer personal accounting ver 0.1",\
                       "-------[ Transactions list ]--------"]

        self.update()

        self.footer = ["[N]ew transaction",\
                       "[D]elete transaction",\
                       "[G]o back"]

        self.prompt = "What do you want to do ?"
        self.answers = {"n":[self.display_prompt, "newtransaction"],\
                        "d":[self.display_prompt, "deltransaction"],\
                        "g":[self.change_menu, "mainmenu"]}

        self.submenus = {"newtransaction":SubNewTransaction(app),\
                         "deltransaction":SubDelTransaction(self)}


    def display_prompt(self, prompt):
        self.submenus[prompt].display()

    def update(self):
        self.account = self.app.active_account
        self.transactions = []
        self.contents = []

        if self.account is None:
            return
        for c in data.transactions:
            if c.from_account == self.account.id:
                self.transactions.append(c)
            if c.to_account == self.account.id:
                self.transactions.append(c)

        index = 0
        balance = self.account.initial_balance
        for t in sorted(self.transactions, key=lambda transaction: transaction.date[0]):
            index += 1
            if t.from_account == self.account.id:
                string = "%0i %+#15.2f %s   %-#8s   %-#30s %s" % \
                        (index, t.amount, t.currency, t.date, t.description, t.category)
                balance += t.amount
            else:
                string = "%0i %+#15.2f %s   %-#8s   %-#30s %s" % \
                        (index, -t.amount, t.currency, t.date, t.description, t.category)               
                balance -= t.amount

            self.contents.append(string)
            
        self.contents.append("-----------------------------------------")
        self.contents.append("Account balance : %+#15.2f %s" % (balance, self.account.currency))
