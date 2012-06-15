# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from menu import Menu
from sub_account import SubNewAccount
from sub_del_account import SubDelAccount

from .. import data

class AccountListMenu(Menu):

    def __init__(self, app):
        Menu.__init__(self, app)
        self.header = ["Ebenezer personal accounting ver 0.1",\
                       "---------[ Accounts list ]----------"]

        self.contents = []
        index = 0
        self.footer = []
        for a in data.accounts:
            index += 1
            string = ""
            if a.name == self.app.active_account.name:
                string += "* "
            else:
                string += "  "

            string += str(index) + " " + a.name
            self.contents.append(string)
            self.answers[str(index)] = [self.set_active, index]

        if len(data.accounts) > 1:
            self.footer.append("[1] to [" + str(index) + "] to set active account")
            
        self.footer.append("[N]ew account")
        self.footer.append("[D]elete an account")
        self.footer.append("[G]o back")

        self.prompt = "What do you want to do ?"


        self.answers['g'] = [self.change_menu, "mainmenu"]
        self.answers['n'] = [self.display_prompt, "newaccount"]
        self.answers['d'] = [self.display_prompt, "delaccount"]

        self.submenus = {"newaccount":SubNewAccount(data.accounts),\
                         "delaccount":SubDelAccount(data.accounts)}

    def display_prompt(self, prompt):
        self.submenus[prompt].display()

    def update(self):
        index = 0
        self.contents = []
        for a in data.accounts:
            index += 1
            string = ""
            if a.name == self.app.active_account.name:
                string += "* "
            else:
                string += "  "

            string += str(index) + " " + a.name
            self.contents.append(string)
            self.answers[str(index)] = [self.set_active, index]


    def set_active(self, index):
        self.app.active_account = data.accounts[index-1]


