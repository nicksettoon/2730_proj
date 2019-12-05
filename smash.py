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
    start.startPrompt("")

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
        # self.menutype = "functions"
        self.optionlist = [
            "Open a tournament.",
            "Make a tournament.",
            "DONT USE ME YET.",
            "DONT USE ME YET."
        ]

        self.functionlist = [
            self.startEditTmntMenu,
            self.startMakeTmntMenu,
            self.editGlobalMUs,
            self.queryGlobalMUs
        ]
        super().__init__(self.prompt)

    def startMakeTmntMenu(self):
        # print("Hit startMakeTmntMenu")
        makeTmnt = tmnt.MakeTmntMenu()
        return makeTmnt.startPrompt("")

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
            return editTmnt.startPrompt("")

    def editGlobalMUs(self):
        print("Hit editGlobalMUs")
        return True

    def queryGlobalMUs(self):
        print("Hit queryGlobalMUs")
        return True

    def exitFunc(self):
        #saves the dataframe before exiting
        print("Hit startmenu exitFunc")
        # self.tmnt.saveDF()

    def returnFunc(self):
        #clears all previous settings and saves the dataframe
        print("Hit startmenu returnFunc")
        # self.matchup = None
        # self.tmnt.saveDF()

if __name__ == "__main__": main()
else: print("What you doin' willis.")
