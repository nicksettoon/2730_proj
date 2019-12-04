#external libraries
import csv
import numpy as np
import pandas as pd
import os
#custom imports
from Tournament import Tournament as T
from Menu import Menu, ListMenu, FunctionMenu

def normalizeStat(stat_challenger, stat_opponent):
    stat = (stat_challenger-stat_opponent)/(stat_challenger+stat_opponent)
    return stat

def makeTournaments():
    t1 = T("Frostbite 2019")
    t1.printDF()
    t1.saveDF()

    t1 = T("Frostbite 2018")
    t1.printDF()
    t1.saveDF()

    t1 = T("Frostbite 2017")
    t1.printDF()
    t1.saveDF()

class StartMenu(FunctionMenu):
    #Class for start menu options
    def __init__(self):
        print("Welcome to the Smash Ultimate Tournament Data Builder!")
        self.prompt = "SMASH"
        # self.menutype = "functions"
        self.optionlist = ["Make a tournament.", "Search for a tournament.", "Edit global matchup.", "Search global matchups."]
        self.functionlist = [self.makeTournament, self.queryTournament, self.editGlobalMUs, self.queryGlobalMUs]
        super().__init__(self.prompt)

    def makeTournament(self):
        print("Hit makeTournament")
        return True

    def queryTournament(self):
        print("Hit queryTournament")
        Tlist = SelectTournament(self.prompt) #create tournament selection prompt
        selection = Tlist.startPrompt()# get the user's selection

        if selection == True:
            return True
        elif selection == False:
            return False
        else:
            query = QueryTournament(selection) #make menu for tournament
            return query.startPrompt()

    def editGlobalMUs(self):
        print("Hit editGlobalMUs")
        return True

    def queryGlobalMUs(self):
        print("Hit queryGlobalMUs")
        return True
    

class SelectTournament(ListMenu):
    def __init__(self, prompt_in):
        self.getTournaments()
        super().__init__(prompt_in)

    def getTournaments(self):
        self.optionlist = []
        for root, dirs, files in os.walk('./'):
            for filename in files:
                if filename.endswith('.tmnt'):
                    self.optionlist.append(filename[:-5])
        self.optionlist = pd.Series(self.optionlist)

class QueryTournament(FunctionMenu):
    #class for menu of options related to a specific Tournament
    def __init__(self, prompt_in):
        self.prompt = prompt_in
        self.optionlist = ["Print non-zero matchups", "Edit matchups", "Print all matchups."] #set options visible to user
        self.functionlist = [self.printTopMus, self.editMus, self.printAllMus] #set list of functions those options map to
        super().__init__(prompt_in)
        
    def printTopMus(self):
        print("hit printTopMus")
        return True

    def editMus(self):
        print("hit editMus")
        return True

    def printAllMus(self):
        print("hit printAllMus")
        return True


def main():
    start = StartMenu()
    start.startPrompt()
    print("Closing Main")


if __name__ == "__main__": main()
else: print("What you doin' willis.")
