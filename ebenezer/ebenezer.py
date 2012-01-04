# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

from ui.menu_main import MainMenu
from ui.menu_acc_list import AccountListMenu

class Ebenezer:

    def __init__(self, parser):
        self.parser = parser
        self.accounts = parser.get_accounts()
        self.active_account = self.accounts[0]
        self.menus = {}
        self.menus["mainmenu"] = MainMenu(self)
        self.menus["accountlist"] = AccountListMenu(self, parser.get_accounts())
        self.running = False
        self.current_menu = "mainmenu"


    def run(self):
        self.running = True
        while self.running:
            self.menus[self.current_menu].display()

        return
