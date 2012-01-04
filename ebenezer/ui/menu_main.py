# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from menu import Menu

class MainMenu(Menu):

    def __init__(self, app):
        Menu.__init__(self, app)

        self.header = ["Ebenezer personal accounting ver 0.1",\
                       "-----------[ Main menu ]------------"]

        num_acc = self.app.parser.get_num_accounts()

        self.contents = ["Found " + str(num_acc) + " accounts",\
                         "[L]ist accounts",\
                         "[Q]uit"]

        self.prompt = "What do you want to do ?"

        self.answers = {"l":self.list_accounts, "q": self.quit}

    def update(self):
        num_acc = self.app.parser.get_num_accounts()
        self.contents[0] = "Found " + str(num_acc) + " accounts"

    def list_accounts(self):
        self.app.current_menu = self.app.accountlist

    def quit(self):
        self.app.running = False
        
