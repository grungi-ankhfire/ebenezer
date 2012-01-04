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
        for a in accounts:
            self.contents.append("-- " + a.props["name"])

        self.prompt = "[Enter] to return..."

        self.callback = self.go_back

    def go_back(self):
        self.app.current_menu = self.app.mainmenu
