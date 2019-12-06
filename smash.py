#EXTERNAL IMPORTS#
import numpy as np
import pandas as pd
# import csv

#CUSTOM IMPORTS#
from MNUs import menus as mnus
from MUs import matchups as mus
from TMNTs import tournaments as tmnt

def main():
    start = StartMenu()
    start.startPrompt("Please input a number.")

    # MATCHUP EDIT TESTING #
    # editTmnt = tmnt.EditTmntMenu("test")
    # editMu = mus.EditMuMenu(editTmnt.getMuObj(['Banjo', 'Bayonetta']))
    # end = editMu.test()
    # editTmnt.printTmnt()
    # end = editMu.test()
    # editTmnt.printTmnt()

    #LOOP TESTING#
    # end = False
    # while(end == False):

    #MAKE TOURNAMENT TESTING#
    # makeTmnt = MakeTournament()
    # makeTmnt.startPrompt("")

    print("Closing Main")

        
class StartMenu(mnus.FuncMenu):
    #Class for start menu options
    def __init__(self):
        print("Welcome to the Smash Ultimate Tournament Data Builder!")
        self.prompt = "SHOW ME YOUR MUs"
        # self.strflag = False
        # self.optionslist = []
        # self.functionslist = []
        self.menudict = {
            "Open a tournament.":self.startEditTmntMenu,
            "Make a tournament.":self.startMakeTmntMenu,
            "Edit global matchups.(dummy func)":self.editGlobalMUs,
            "Search global matchups.(dummy func)":self.queryGlobalMUs,
            "index":None,
        }

        super().__init__()

    def startEditTmntMenu(self):
        # print("Hit startEditTmntMenu")
        tmntMenu = tmnt.SelTmntMenu(self.prompt) #create tournament selection prompt
        selection = tmntMenu.startPrompt("Please select a tournament.")# get the user's selection

        if selection == True:
            return True
        elif selection == False:
            return False
        else:
            editTmnt = tmnt.EditTmntMenu(selection) #make menu for tournament
            return editTmnt.startPrompt("Please input a number.")

    def startMakeTmntMenu(self):
        makeTmnt = tmnt.MakeTmntMenu()
        return makeTmnt.startPrompt("Please input a number.")

    def editGlobalMUs(self):
        print("Hit editGlobalMUs")
        return True

    def queryGlobalMUs(self):
        print("Hit queryGlobalMUs")
        return True

    def exitFunc(self):
        print("Hit startmenu exitFunc")

    def returnFunc(self):
        self.clearTerm()
        print("Hit startmenu returnFunc")

if __name__ == "__main__": main()
else: print("What you doin' willis.")
