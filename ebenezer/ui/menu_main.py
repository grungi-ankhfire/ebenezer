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
                         "Current active account : " + self.app.active_account.props["name"],\
                         "[A]ccounts",\
                         "[T]ransactions",\
                         "[Q]uit"]

        self.prompt = "What do you want to do ?"

        self.answers = {"a":[self.change_menu, "accountlist"],\
                        "t":[self.change_menu, "accounttrans"],\
                        "q":[self.quit, None]}

    def update(self):
        num_acc = self.app.parser.get_num_accounts()
        self.contents[0] = "Found " + str(num_acc) + " accounts"
        self.contents[1] = "Current active account : " + self.app.active_account.props["name"]

    def quit(self, data = None):
        self.app.running = False
        
