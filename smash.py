#external libraries
import csv
import numpy as np
import pandas as pd
import os
#custom imports
from Tournament import Tournament as T
from Menu import MenuBase, Menu, ListMenu, FunctionMenu
from Matchup import MatchupStats as MUS

def normalizeStat(stat_challenger, stat_opponent):
    stat = (stat_challenger-stat_opponent)/(stat_challenger+stat_opponent)
    return stat

# def makeTournaments():
#     t1 = T("Frostbite 2019")
#     t1.printDF()
#     t1.saveDF()

#     t1 = T("Frostbite 2018")
#     t1.printDF()
#     t1.saveDF()


class StartMenu(FunctionMenu):
    #Class for start menu options
    def __init__(self):
        print("Welcome to the Smash Ultimate Tournament Data Builder!")
        self.prompt = "SMASH"
        # self.menutype = "functions"
        self.optionlist = ["Make a tournament.", "Open a tournament.", "DONT USE ME YET.", "DONT USE ME YET."]
        self.functionlist = [self.makeTournament, self.queryTournament, self.editGlobalMUs, self.queryGlobalMUs]
        super().__init__(self.prompt)

    def makeTournament(self):
        print("Hit makeTournament")
        maker = MakeTournament()
        return maker.startPrompt("")

    def queryTournament(self):
        print("Hit queryTournament")
        Tlist = SelectTournament(self.prompt) #create tournament selection prompt
        selection = Tlist.startPrompt("Please select a tournament.")# get the user's selection

        if selection == True:
            return True
        elif selection == False:
            return False
        else:
            query = QueryTournament(selection) #make menu for tournament
            return query.startPrompt("")

    def editGlobalMUs(self):
        print("Hit editGlobalMUs")
        return True

    def queryGlobalMUs(self):
        print("Hit queryGlobalMUs")
        return True
    
class MakeTournament(FunctionMenu):
    def __init__(self):
        self.optionlist = ["Print current tournament.", "Save tournament", "Rename tournament."]
        self.functionlist = [self.printTournament, self.saveTournament, self.renameTournament]
        self.tournament = self.makeTournament()
        super().__init__(self.prompt)

    def renameTournament(self):
        print("hit renameTournament. I don't do anything yet.")
        return False

    def saveTournament(self):
        print("hit saveTournament")
        self.prompt = self.prompt[:-12] + ">"
        self.tournament.saveDF()
        return False

    def printTournament(self):
        print("hit printTournament")
        self.tournament.printDF()
        return False

    def makeTournament(self):
        print("Name:")
        name = str(input())
        self.prompt = name + "(not saved)"
        t = T(name)
        t.makeDF()
        return t

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

class SelectCharacter(ListMenu):
    def __init__(self, prompt_in):
        self.getCharacters()
        super().__init__(prompt_in)
    
    def getCharacters(self):
        matchup = MUS('char_stats.csv')
        matchup.loadStats()
        print(matchup.characters)

        self.optionlist = matchup.characters.ravel()

class EditMatchup(FunctionMenu):
    def __init__(self, matchup_in):
        char1 = matchup_in['char1'][0]
        char2 = matchup_in['char2'][0]
        self.prompt = char1 + "_x_" + char2
        self.optionlist = ["Function1", "Function2"]
        self.functionlist = [self.dummyFunc, self.dummyFunc]
        super().__init__(self.prompt) #make menu
    
    def dummyFunc(self):
        print("I'm a useless function.")

class QueryTournament(FunctionMenu):
    #class for menu of options related to a specific Tournament
    def __init__(self, tournament_name):
        #menu setup
        self.prompt = tournament_name
        self.optionlist = ["Edit matchup", "Print matchup", "Print non-zero matchups", "Print matchups above threshold.", "Print all matchups."] #set options visible to user
        self.functionlist = [self.editMus, self.printMu, self.printNonZeroMus, self.printThreshMus, self.printAllMus] #set list of functions those options map to
        #make and load tournament 
        self.tournament = T(tournament_name)
        self.tournament.loadDF()
        super().__init__(tournament_name) #make menu

    def editMus(self):
        print("hit editMus")
        mu = self.getMu()
        print(mu)

        editor = EditMatchup(mu) #make menu for matchup
        return editor.startPrompt("")

    def printMu(self):
        mu = self.getMu()
        if mu != None:
            print(mu)

        return False

    def getMu(self):
        Clist = SelectCharacter(self.prompt)

        #get first character in the matchup
        selection1 = Clist.startPrompt("Please select the first character in the matchup.")
        if selection1 == True:
            return True
        elif selection1 == False:
            return False
        matchup = selection1 + "_x_"
        
        #get second character in the matchup
        Clist.prompt = matchup 
        selection2 = Clist.startPrompt(f"First char: {selection1}\nPlease select the second character in the matchup.", False)
        if selection2 == True:
            return True
        elif selection2 == False:
            return False

        print(f"Searching for matchup: {selection1} vs. {selection2}")
        row = self.tournament.df[(self.tournament.df['char1'] == selection1) & (self.tournament.df['char2'] == selection2)].copy()
        empty = row.values.size
        if empty == 0:
            print("Did not find that matchup.")
            print(f"Searching for matchup: {selection2} vs. {selection1}")
            row = self.tournament.df[(self.tournament.df['char1'] == selection2) & (self.tournament.df['char2'] == selection1)]
            empty = row.values.size
        if empty == 0:
            print("Could not find matchup because it's a ditto. Dittos have been excluded from the dataset.")
            row = None

        return row
        
    def printNonZeroMus(self):
        print("hit printNonZeroMus")
        mus = self.tournament.df[(self.tournament.df['total_games'] > 0)]
        print(mus)
        return False
    
    def printThreshMus(self):
        print("hit printThreshMus")
        basic = MenuBase("\nPlease enter threshold integer.")
        thresh = basic.basicIntLoop()
        print(self.tournament.df['total_games'] > thresh)
        return False

    def printAllMus(self):
        print("hit printAllMus")
        self.tournament.printDF()
        return False


def main():
    start = StartMenu()
    start.startPrompt("")
    # query = QueryTournament("Frostbite")
    # query.startPrompt("")
    # maker = MakeTournament()
    # maker.startPrompt("")
    print("Closing Main")


if __name__ == "__main__": main()
else: print("What you doin' willis.")
