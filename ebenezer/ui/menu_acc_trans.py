# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from menu import Menu
from sub_transaction import SubNewTransaction
from sub_del_transaction import SubDelTransaction

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

        self.submenus = {"newtransaction":SubNewTransaction(self.account),\
                         "deltransaction":SubDelTransaction(self.account)}


    def display_prompt(self, prompt):
        self.submenus[prompt].display()

    def update(self):
        self.account = self.app.active_account
        self.transactions = []
        self.contents = []

        if self.account is None:
            return
        for c in self.account.children:
            if c.type == "TRANSACTION":
                self.transactions.append(c)

        index = 0
        balance = self.account.props['balance']
        for t in sorted(self.transactions, key=lambda transaction: transaction.props["date"]):
            index += 1
            string = "%0i %+#15.2f%s   %-#8s   %-#30s %s" % \
                     (index, t.props["amount"], t.props["currency"], t.props["date"], t.props["name"], t.props["category"])


            balance += t.props["amount"]
            self.contents.append(string)
            #self.contents.append(str(index) + "  " + str(t.props["amount"])  + t.props["currency"] + " " + str(t.props["date"]) + " " + t.props['name'])
        self.contents.append("-----------------------------------------")
        self.contents.append("Account balance : %+#15.2f%s" % (balance, self.account.props["currency"]))
