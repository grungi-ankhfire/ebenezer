# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details
from menu import Menu

class MainMenu(Menu):

    def __init__(self, app):
        Menu.__init__(self)

        self.app = app

        self.header = ["Ebenezer personal accounting ver 0.1",\
                       "-----------[ Main menu ]------------"]

        self.contents = ["Found",\
                         "[Q]uit"]

        self.prompt = "What do you want to do ?"

        self.answers = {"q": self.quit}

    def quit(self):
        self.app.running = False
        
