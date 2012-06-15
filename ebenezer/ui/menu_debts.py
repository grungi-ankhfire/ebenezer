# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from menu import Menu

from .. import data

class DebtsListMenu(Menu):

    def __init__(self, app, account):
        Menu.__init__(self,app)
        self.header = ["Ebenezer personal accounting ver 0.1",\
                       "-------------[ Debts ]--------------"]       

        self.contents = []
        self.account  = account
        self.footer = []

        self.prompt = "[G]o back... "
        self.update()

        self.answers['g'] = [self.change_menu, "mainmenu"]

    def update(self):
        self.account = self.app.active_account
        if self.account is None:
            return
        people = {}
        self.contents = []
        for t in data.transactions:
            if t.person is not None:
                if t.person in people.keys():
                    people[t.person]+=t.amount
                else:
                    people[t.person] = t.amount

        for p in people.keys():
            if people[p] < 0:
                self.contents.append(p + " owes you " + str(-people[p]) + self.account.currency+ ".")
            elif people[p] > 0:
                self.contents.append("You owe " + p + " " + str(people[p]) + self.account.currency+ ".")
            
