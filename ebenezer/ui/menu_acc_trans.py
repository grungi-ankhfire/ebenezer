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

        if self.account is None:
            return
        self.transactions = []
        for c in self.account.children:
            if c.type == "TRANSACTION":
                self.transactions.append(c)

        index = 0
        self.contents = []
        for t in self.transactions:
            index += 1
            string = "%0i %+#15.2f%s   %-#8s   %s" % \
                     (index, t.props["amount"], t.props["currency"], t.props["date"], t.props["name"])


            self.contents.append(string)
            #self.contents.append(str(index) + "  " + str(t.props["amount"])  + t.props["currency"] + " " + str(t.props["date"]) + " " + t.props['name'])
