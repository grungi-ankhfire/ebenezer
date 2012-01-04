# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

from ui.menu_main import MainMenu

class Ebenezer:

    def __init__(self, parser):
        self.mainmenu = MainMenu(self)
        self.running = False
        self.parser = parser
        self.current_menu = self.mainmenu


    def run(self):
        self.running = True
        while self.running:
            self.current_menu.display()

        return
