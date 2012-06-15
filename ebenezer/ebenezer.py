# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

from ui.menu_main import MainMenu
from ui.menu_acc_list import AccountListMenu
from ui.menu_acc_trans import AccountTransactionsMenu
from ui.menu_debts import DebtsListMenu
from log import *
import data

class Ebenezer:

    def __init__(self):

        if len(data.accounts) == 0:
            self.active_account = None
        else:
            self.active_account = data.accounts[0]
        self.menus = {}
        self.menus["mainmenu"] = MainMenu(self)
        self.menus["accountlist"] = AccountListMenu(self)
        #self.menus["accounttrans"] = AccountTransactionsMenu(self, self.active_account)
        #self.menus["debts"] = DebtsListMenu(self, self.active_account)
        self.running = False
        self.current_menu = "mainmenu"


    def run(self):
        self.running = True
        while self.running:
            if self.active_account not in data.accounts:
                if len(accounts) == 0:
                    self.active_account = None
                else:
                    self.active_account = data.accounts[0]
            self.menus[self.current_menu].display()
        
        # self.parser.replace_accounts(self.accounts)

        # if self.parser.filename is None:
        #     filename = raw_input("Save in which file ? [filename] to save or [Enter] to drop changes : ")
        #     if filename != "":
        #         self.parser.filename = filename
            
        #self.parser.write_file(self.parser.filename)
        return
