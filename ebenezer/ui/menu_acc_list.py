# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from menu import Menu

class AccountListMenu(Menu):

    def __init__(self, app, accounts):
        Menu.__init__(self, app)
        self.header = ["Ebenezer personal accounting ver 0.1",\
                       "---------[ Accounts list ]----------"]

        self.contents = []
        index = 0
        for a in accounts:
            index += 1
            string = ""
            if a.props["name"] == self.app.active_account.props["name"]:
                string += "* "
            else:
                string += "  "

            string += str(index) + " " + a.props["name"]
            self.contents.append(string)
            self.answers[str(index)] = [self.set_active, index]

        self.prompt = "[1] to [" + str(index) + "] to set active account, or  [G]o back..."


        self.answers['g'] = [self.change_menu, "mainmenu"]


    def update(self):
        index = 0
        for a in self.app.accounts:
            index += 1
            string = ""
            if a.props["name"] == self.app.active_account.props["name"]:
                string += "* "
            else:
                string += "  "

            string += str(index) + " " + a.props["name"]
            self.contents[index-1] = string

    def set_active(self, data):
        self.app.active_account = self.app.accounts[data-1]

    def change_menu(self, data):
        self.app.current_menu = data
