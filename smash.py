#EXTERNAL IMPORTS#
import numpy as np
import pandas as pd
import os
# from tabulate import tabulate

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
        self.strflag = False
        self.menudict = {
            "Open a tournament.":self.startEditTmntMenu,
            "Make a tournament.":self.startMakeTmntMenu,
            "Rename tournament.":self.renameTmnt,
            "Copy tournament.":self.copyTmnt,
            "Edit global matchups.(dummy func)":self.editGlobalMUs,
            "Search global matchups.(dummy func)":self.startGlobalMuMenu,
            "index":[],
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

    def renameTmnt(self):
        selTmnt = tmnt.SelTmntMenu(self.prompt[:-1])
        choice = selTmnt.startPrompt("Please select a tournament to rename.")
        os.system(f"rename ./TMNTs/{choice}.tmnt ./TMNTs/{choice}-copy.tmnt" if os.name == 'nt' else f"mv ./TMNTs/{choice}.tmnt ./TMNTs/{choice}-copy.tmnt")
        selTmnt.printMenu()
        print(f"{choice} renamed.")

        return False

    def copyTmnt(self):
        selTmnt = tmnt.SelTmntMenu(self.prompt[:-1])
        choice = selTmnt.startPrompt("Please select a tournament to copy.")
        os.system(f"copy ./TMNTs/{choice}.tmnt ./TMNTs/{choice}-copy.tmnt" if os.name == 'nt' else f"cp ./TMNTs/{choice}.tmnt ./TMNTs/{choice}-copy.tmnt")
        selTmnt.printMenu()
        print(f"{choice} copied.")

        return False
    
    def editGlobalMUs(self):
        print("Hit editGlobalMUs")
        return True

    def startGlobalMuMenu(self):
        print("Hit startGlobalMuMenu")
        return True

    def exitFunc(self):
        print("Hit startmenu exitFunc")

    def returnFunc(self):
        # self.clearTerm()
        print("Hit startmenu returnFunc")
        self.printMenu()

if __name__ == "__main__": main()
else: print("What you doin' willis.")
