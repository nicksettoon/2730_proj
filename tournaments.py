#EXTERNAL IMPORTS#
import pandas as pd
import numpy as np
import os 
#CUSTOM IMPORTS#
from MNUs import menus as mnus
from CHARs import characters as chars
from MUs import matchups as mus

"""------FUNCTION MENUS-------------------------------------------------"""

class MakeTmntMenu(mnus.FuncMenu):
    def __init__(self):
        #prompt for Tournament name
        self.tmnt = self.makeTmnt()
        self.strflag = False
        self.menudict = {
            "Print current tournament.":self.printTmnt,
            "Save tournament.":self.saveTmnt,
            "Start over.":self.reMake,
            "index":[],
        }

        super().__init__()

    def printTmnt(self):
        self.tmnt.printDF()

        return False

    def reMake(self):
        self.tmnt = self.makeTmnt()
        self.prompt = self.prompt + ">"

        return False

    def saveTmnt(self):
        self.prompt = self.newname + ">"
        self.tmnt.saveDF()

        return False
        
    def makeTmnt(self):
        self.newname = str(input("Tournament Name: "))
        t = Tmnt(self.newname)
        self.prompt = self.newname + "(not saved)"
        t.makeDF()
        return t

class EditTmntMenu(mnus.FuncMenu, mus.MuFuncs):
    #class for menu of options related to a specific Tmnt
    def __init__(self, tmnt_name, META):
        self.prompt = tmnt_name 
        self.strflag = False
        self.menudict = {
            "Edit matchup":self.selectMu,
            "Print matchup":self.printMu,
            "Print tournament. (all matchups)":self.printTmnt,
            "Print non-zero matchups":self.printNonZeroMus,
            "Print matchups above threshold.":self.printThreshMus,
            "index":[],
        }
        #make and load tournament 
        if META == None:
            self.tmnt = Tmnt(tmnt_name)
            self.tmnt.loadDF()
        else:
            self.tmnt = META
        super().__init__() #make menu
    
    def selectMu(self):
        #creates mu object and editMatchup menu instance, then hands off to its prompt
        # #print("hit selectMu")
        self.matchup = self.getMuObj([])
        if self.matchup == False:
            return False        
        editMu = mus.EditMuMenu(self.matchup) #make menu instance for editing matchup
        return editMu.startPrompt("") #start prompt
    
    def printMu(self):
        # #print("hit printMu")
        self.matchup = self.getMuObj([])
        self.printMuObj("Matchup:")

        return False

    def printTmnt(self):
        # #print("hit printTmnt")
        self.tmnt.printDF()

        return False

    def printNonZeroMus(self):
        #print("hit printNonZeroMus")
        mus = self.tmnt.df[(self.tmnt.df['total_games'] > 0)]
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)
        print(mus)

        return False
    
    def printThreshMus(self):
        #print("hit printThreshMus")
        basic = mnus.BaseMenu("\nPlease enter threshold integer.")
        thresh = basic.basicIntLoop()
        mus = self.tmnt.df[(self.tmnt.df['total_games'] > thresh)]
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)
        print(mus)

        return False

    def getMuObj(self, mu_in=[]):
        #function that gets the matchup series for two given characters
        #if no mu_in pair is given, prompts user
        if mu_in == []:
            charMenu = chars.SelCharMenu(self.prompt[:-1]) #set up character list menu
            #get first character in the matchup
            mu_in.append(charMenu.startPrompt("Please select the first character in the matchup."))
            if mu_in[0] == True:#if recieved quit
                return True 
            elif mu_in[0] == False:#if received back
                return False
            matchupprompt = mu_in[0] + "_x_" # make new prompt
            #get second character in the matchup
            charMenu.prompt = matchupprompt
            charMenu.printmenu = False
            mu_in.append(charMenu.startPrompt(f"First char: {mu_in[0]}\nPlease select the second character in the matchup."))
            if mu_in[1] == True:
                return True
            elif mu_in[1] == False:
                return False
        try: #find series which matches the matchup pair
            series = self.tmnt.df.xs((mu_in[0],mu_in[1]))
        except KeyError:
            try:#search for inverse of pair
                series = self.tmnt.df.xs((mu_in[1],mu_in[0]))
            except KeyError:
                if mu_in[0] == mu_in[1]:
                    print("Matchup is a ditto. Dittos are redundant so they have been excluded.")
                else:
                    print("You should not be here... Shoo.")
                series = None #create return list
                return False

        mu = self.makeMuObj(series)
        return mu

    def exitFunc(self):
        #saves the dataframe before exiting
        #print("hit tmnt exitFunc")
        print("Saving/Updating Dataframe.")
        self.tmnt.saveDF()

    def returnFunc(self):
        #clears all previous settings and saves the dataframe
        # self.clearTerm()
        #print("hit tmnt returnFunc")
        self.matchup = None
        print("Saving/Updating Dataframe.")
        self.tmnt.saveDF()
        self.printmenu = True

"""------CLASSES--------------------------------------------------------"""

class Tmnt():
    #class that holds tournament matchup result self.data
    def __init__(self, name):
        self.name = name

    def makeDF(self):
        #init matchup array
        muloader = mus.MuStats("./CHARs/char_stats.csv")
        muloader.loadMuStats()
        muloader.genMuArray()
        mudata = muloader.muarray.copy()

        #make a series for holding the zeros 
        size = len(mudata)
        # print(size)
        zeros = np.zeros((size,2))
        # print(zeros)

        #create multiIndex from array of tuples
        mindex = pd.MultiIndex.from_tuples(mudata, names=['c1','c2'])
        #make dataframe with zeroes for columns and the multiIndex for the indexes
        self.df = pd.DataFrame(zeros.astype(int),columns=['c1_wins', 'c2_wins'], index=mindex)

    def printDF(self):
        print(self.name)
        self.df['total_games'] = self.df['c1_wins'] + self.df['c2_wins'] #recalc total_games col
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)
        print(self.df)
    
    def saveDF(self):
        #make total games column as function column
        self.df['total_games'] = self.df['c1_wins'] + self.df['c2_wins'] #recalc total_games col
        self.df.dropna()
        export_csv = self.df.to_csv(f"./TMNTs/{self.name}.tmnt", index=True) #write to csv
    
    def sumAllTmnts(self, tdf_list):
        # tdf_list = self.loadAllTmnts()
        self.df = tdf_list[0].copy()
        for tmntdf in tdf_list[1:]:
            # print("Adding dataframes together.")
            self.df += tmntdf

    def loadAllTmnts(self):
        tmntdflist = []
        tmntmenu = SelTmntMenu("Loading TMNT Files.")
        tmntlist = tmntmenu.menudict["options"]
        tempname = self.name
        for tmntfile in tmntlist:
            if (tmntfile == "META"):
                # print("Found META.tmnt recalculating it instead of loading it.")
                continue
            self.name = f"{tmntfile}"
            # print(f"Loading {self.name}")
            self.loadDF()
            tmntdflist.append(self.df.copy()) 
            # print(f"Adding {self.name} to array.")
        self.name = tempname

        return tmntdflist

    def loadDF(self):
        try:
            delimiter = ","
            self.df = pd.read_csv(f"./TMNTs/{self.name}.tmnt", sep=delimiter) #read in csv
            mindex = pd.MultiIndex.from_frame(self.df[['c1','c2']]) #create multiIndex from csv
            dict = { #make dict of rest of columns
                "c1_wins" : self.df['c1_wins'].astype(int),
                "c2_wins" : self.df['c2_wins'].astype(int)
            }

            self.df = pd.DataFrame(dict) #create new dataframe
            self.df.index = mindex #add indexes after
            self.df['total_games'] = self.df['c1_wins'] + self.df['c2_wins'] #recalc total_games col
            # self.printDF()
            # print(f"Found csv for {self.name}.")
            return True
        except FileNotFoundError:
            print("The tournament file you were looking for wasn't found file not found.")
            return False
    
"""------LIST MENUS-----------------------------------------------------"""

class SelTmntMenu(mnus.ListMenu):
    def __init__(self, prompt_in):
        self.prompt = prompt_in
        self.optionslist = []
        self.strflag = False
        print("Loading TMNT files.")
        for root, dirs, files in os.walk('./TMNTs/'):
            for filename in files:
                if filename.endswith('.tmnt'):
                    self.optionslist.append(filename[:-5])
        # self.optionlist.append(np.arange(1,len(self.optionslist)+1))
        # self.optionslist.append([])

        super().__init__()

        # count = 0
        # try:
        #     for root, dirs, files in os.walk('./TMNTs/'):
        #         for filename in files:
        #             if filename.endswith('.tmnt'):
        #                 # print(filename)
        #                 tmntlist.append(filename)
        #                 # count += 1
        # except FileNotFoundError:
        #     print("idk how you got here. But I'm impressed.")

        # delimiter = ','
        #for each tmnt file, import into a dataframe and ad it to a list.

            # df = pd.read_csv(f"./TMNTs/{tmntfile}", sep=delimiter) #read in csv
            # mindex = pd.MultiIndex.from_frame(df[['c1','c2']]) #create multiIndex from csv
            # dict = { #make dict of rest of column
            #     "c1_wins" : df['c1_wins'].astype(int),
            #     "c2_wins" : df['c2_wins'].astype(int) }
            # df = pd.DataFrame(dict) #create new dataframe
            # df.index = mindex #add indexes after
            # df['total_games'] = df['c1_wins'] + df['c2_wins'] #recalc total_games col
            # tmntdflist.append(df) # append dataframe to list of data frames