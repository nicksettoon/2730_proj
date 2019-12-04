#external libraries
import csv
import numpy as np
import pandas as pd
#custom imports
from Tournament import Tournament as Tour
from Menu import Menu

def normalizeStat(stat_challenger, stat_opponent):
    stat = (stat_challenger-stat_opponent)/(stat_challenger+stat_opponent)
    return stat


class StartMenu(Menu):
    #Class for start menu options
    def __init__(self):
        print("Welcome to the Smash Ultimate Tournament Data Builder!")
        prompt = "SMASH>"
        opts = ["Make tournament.", "Edit tournament.", "Search tournament.", "Edit global matchup.", "Search global matchups."]
        funcs = [self.makeTournament, self.editTournament, self.queryTournament, self.editMUs, self.queryMUs]
        super().__init__(prompt, opts, funcs)

    def makeTournament(self):
        print("Hit makeTournament")

    def editTournament(self):
        print("Hit editTournament")
        
    def queryTournament(self):
        print("Hit queryTournament")

    def editMUs(self):
        print("Hit editMUs")

    def queryMUs(self):
        print("Hit queryMUs")

# class MenuTemp(Menu):
#     def __init__(self):
#         prompt = ""
#         opts = []
#         funcs = []
#         super().__init__(prompt, opts, funcs)
        
# class QueryTournamentMenu(Menu):
#     def __init__(self):
#         prompt = f"{super.prompt}>QueryT>"
#         opts = ["List Tournaments", ""]
#         funcs = []
#         super().__init__(prompt, opts, funcs)


def main():
    start = StartMenu()

    close = False
    while(close == False):
        start.promptLoop()()
    # t1 = Tournament("Let's Make Moves")

    # t1 = Tour("Frostbite 2019")
    # t1.printDF()
    # t1.saveDF()
    # pass

    
if __name__ == "__main__": main()
else:
    print("What you doin' willis.")
