#EXTERNAL IMPORTS#
import numpy as np
import pandas as pd
import os
# from tabulate import tabulate

#CUSTOM IMPORTS#
from MNUs import menus as mnus
from MUs import matchups as mus
from TMNTs import tournaments as tmnt
from CHARs import characters as chars
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import GridSearchCV
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, f1_score 
# from sklearn.svm import SVC

def main():
    start = StartMenu()
    start.startPrompt("Please input a number.")

    # meta = tmnt.Tmnt("META")
    # tdflist = meta.loadAllTmnts()
    # meta.sumAllTmnts(tdflist)
    
    # muload = mus.MuStats("./CHARs/char_stats.csv")
    # muload.loadMuStats()
    # muload.genMuArray()
    # muload.getMuStats()

    # matchups = muload.MUdf.to_csv("./MUs/MUstats.csv")
    # results = meta.df.to_csv("./MUs/MUresults.csv")

    # matchups = muload.MUdf.to_numpy()
    # results = meta.df.to_numpy()
    # print(matchups.shape)
    # print(results.shape)
    # dataset = np.concatenate((matchups, results), 1)
    # print(dataset.shape)

    # mutrain, mutest, ytrain, ytest = train_test_split(dataset, results[:,:2], test_size=0.25, random_state=123)
    # did not get further than this. data entry took all the time.
    
    print("Closing Main")
   
class StartMenu(mnus.FuncMenu):
    #Class for start menu options
    def __init__(self):
        print("Welcome to the Smash Ultimate Tournament Data Builder!")
        self.prompt = "SHOW ME YOUR MUs"
        self.globaltmntdf = None
        self.strflag = False
        self.menudict = {
            "Open a tournament.":self.startEditTmntMenu,
            "Make a tournament.":self.startMakeTmntMenu,
            "Rename tournament.":self.renameTmnt,
            "Copy tournament.":self.copyTmnt,
            "Search global matchups.":self.startGlobalMuMenu,
            # "Edit global matchups.(dummy func)":self.editGlobalMUs,
            "index":[],
        }
        super().__init__()

    def startEditTmntMenu(self):
        print("hit startEditTmntMenu")
        if self.globaltmntdf != None:
            editTmnt = tmnt.EditTmntMenu("GLOBAL_MUS", self.globaltmntdf) #make menu for tournament
            return editTmnt.startPrompt("Please input a number.")
        else:
            tmntMenu = tmnt.SelTmntMenu(self.prompt) #create tournament selection prompt
            selection = tmntMenu.startPrompt("Please select a tournament.")# get the user's selection

            if selection == True:
                return True
            elif selection == False:
                return False
            else:
                editTmnt = tmnt.EditTmntMenu(selection, None) #make menu for tournament
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
        #print("hit editGlobalMUs")
        return True

    def startGlobalMuMenu(self):
        #print("hit startGlobalMuMenu")
        print("Recomputing META.tmnt")
        meta = tmnt.Tmnt("META")
        tmnts = meta.loadAllTmnts()
        meta.sumAllTmnts(tmnts)
        meta.saveDF()
        self.globaltmntdf = meta

        self.startEditTmntMenu();
        return True

    def exitFunc(self):
        #print("hit startmenu exitFunc")
        pass

    def returnFunc(self):
        # self.clearTerm()
        #print("hit startmenu returnFunc")
        self.printMenu()


if __name__ == "__main__": main()
else: print("What you doin' willis.")
