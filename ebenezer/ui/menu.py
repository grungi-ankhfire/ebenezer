# Copyright (c) 2012 Bastien Gorissen
# Licensed under the MIT license
# See LICENSE file for licensing details

import os

class Menu:

    def __init__(self, app):
        self.app = app
        self.header = []
        self.contents = []
        self.footer = []
        self.prompt = ""
        self.answers = {}
        self.callback = None
        
    def update(self):
        pass

    def display(self):
        self.update()
        os.system("clear")
        for l in self.header:
            print l
        print ""
        for l in self.contents:
            print l
        print ""
        for l in self.footer:
            print l
        print ""
        return self.ask()

    def ask(self):
        ans = raw_input(self.prompt + " ")
        if len(self.answers.keys()) > 0:    
            while ans.lower() not in self.answers.keys():
                return self.display()
            return self.answers[ans.lower()][0](self.answers[ans.lower()][1])
        else:
            return self.callback()
