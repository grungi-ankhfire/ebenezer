# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

from ui.menu_main import MainMenu
from ui.menu_acc_list import AccountListMenu
from ui.menu_acc_trans import AccountTransactionsMenu

class Ebenezer:

    def __init__(self, parser):
        self.version = (0,1)

        self.parser = parser
        self.accounts = parser.get_accounts()
        if len(self.accounts) == 0:
            self.active_account = None
        else:
            self.active_account = self.accounts[0]
        self.menus = {}
        self.menus["mainmenu"] = MainMenu(self)
        self.menus["accountlist"] = AccountListMenu(self, self.accounts)
        self.menus["accounttrans"] = AccountTransactionsMenu(self, self.active_account)
        self.running = False
        self.current_menu = "mainmenu"


    def run(self):
        self.running = True
        while self.running:
            if self.active_account not in self.accounts:
                if len(self.accounts) == 0:
                    self.active_account = None
                else:
                    self.active_account = self.accounts[0]
            self.menus[self.current_menu].display()
        
        self.parser.replace_accounts(self.accounts)

        if self.parser.filename is None:
            filename = raw_input("Save in which file ? [filename] to save or [Enter] to drop changes : ")
            if filename != "":
                self.parser.filename = filename
            
        self.parser.write_file(self.parser.filename)
        return
