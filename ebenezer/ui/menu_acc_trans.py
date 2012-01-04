# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from menu import Menu

class AccountTransactionsMenu(Menu):
    
    def __init__(self, app, account):
        Menu.__init__(self, app)
        self.account = account

        self.header = ["Ebenezer personal accounting ver 0.1",\
                       "-------[ Transactions list ]--------"]

        self.update()
        
        self.prompt = "[G]o back..."
        self.answers = {"g":[self.change_menu, "mainmenu"]}

    def update(self):
        self.account = self.app.active_account

        self.transactions = []
        for c in self.account.children:
            if c.type == "TRANSACTION":
                self.transactions.append(c)

        index = 0
        self.contents = []
        for t in self.transactions:
            index += 1
            self.contents.append(str(index) + "  " + t.props['name'])
