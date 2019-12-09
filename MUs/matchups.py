#EXTERNAL IMPORTS#
import numpy as np
import pandas as pd
from tabulate import tabulate
#CUSTOM IMPORTS#
from MNUs import menus as mnus

"""------CLASSES--------------------------------------------------------"""

class MuFuncs():
    #base class for classes requiring matchup object creation and printing
    def makeMuObj(self, series):
        #turns matchup series into printable dataframe
        mustring = f"{series.name[0]}_x_{series.name[1]}"
        # print("\n"+mustring)
        df = series.to_frame().T
        df.rename( columns ={ df.columns[0] : f"{series.name[0]}_wins", df.columns[1] : f"{series.name[1]}_wins" }, inplace=True)
        self.matchup = {'row':series, 'df':df, 'mu':mustring}

        return self.matchup

    def printMuObj(self, prefix_in):
        self.clearTerm()
        #clears all previous settings and saves the dataframe
        # #print("hit Mu returnFunc")
        # self.matchup = None
        # self.tmnt.saveDF()
        print(f"{prefix_in}{self.matchup['mu']}\n")
        self.printmenu = False
        return print(tabulate(self.matchup['df'], headers='keys', showindex=False))

class MuStats():
    #basic class for holding matchup creation methods and arrays
    def __init__(self, file_name):
        self.filename = file_name

    def loadMuStats(self):
        #takes in str of the name of a csv file with character stats in it
        self.data = np.loadtxt(self.filename, delimiter=',', dtype='str')    

        #get headers array
        self.headers = self.data[0,:].copy()
        #make characters array  
        self.characters = self.data[1:,0].copy()
        self.characters = np.expand_dims(self.characters, axis=1)
        #get stats matrix
        self.stats = self.data[1:,1:].copy().astype(float)
        # print(f"Matchup shape: {mchups.shape}")
        # print(f"Character shape: {chrs.shape}")
        # print(f"Headers shape: {heads.shape}")
        # print(f"Stats Shape: {stats.shape}")

    def getMuStats(self):
        #uses the normalization formula to establish a single line relationship
        #between the two fighters' stats for each unique matchup
        mchups = np.array(self.muarray)
        headers = pd.Series(self.headers[1:])
        chrseries = pd.Series(self.characters[:,0])

        size = len(mchups)
        zeros = np.zeros((size,11))

        # create multiIndex from array of tuples
        mindex = pd.MultiIndex.from_tuples(self.muarray.copy(), names=['c1','c2'])
        # make dataframe with zeroes for columns and the multiIndex for the indexes
        matchupdf = pd.DataFrame(zeros.astype(float),columns=headers[:], index=mindex)

        for mu in mchups:
            chr1 = chrseries[chrseries == mu[0]].index[0]
            chr2 = chrseries[chrseries == mu[1]].index[0]
            chr1stats = self.stats[chr1]
            chr2stats = self.stats[chr2]
            murow = matchupdf.xs((mu[0],mu[1]))
            for ch1, ch2, i  in zip(chr1stats, chr2stats, range(0,12)):
                sample = self.statFunc(ch1, ch2)
                print(f"{mu[0]} vs {mu[1]}, {headers[i]}: {sample}")
                murow[i] = sample

        print(matchupdf)

    def statFunc(self, chr1_stat, chr2_stat):
        stat = (chr1_stat-chr2_stat)/(chr1_stat+chr2_stat)*100

        return stat

    def genMuArray(self):
        #takes in np array containing list of characters and returns new array with all viable unique 1v1 matchups for those characters
        charchecklist = np.zeros_like(self.characters) #make column of zeros
        self.characters = np.append(self.characters, charchecklist, axis = 1) #attach col to self.characters array   
        matchups = [] #make new matchups array

        for char in self.characters:
            # print(char)
            # i = 0 #iteration tracker
            char[1] = "1" #mark the character as 'visited'
            for opponent in self.characters:
                if opponent[1] == "1": #if the opponent's mu list has already been added to the dict, pass.
                    pass
                else:
                    # i += 1 #iteration tracker
                    mu = (char[0], opponent[0]) # create matchup entry in list
                    # print(f"{i}.\t{mu}") print if need be
                    matchups.append(mu)

        self.muarray = matchups #make the matchups an np array

"""------FUNCTION MENUS-------------------------------------------------"""

class EditMuMenu(mnus.FuncMenu, MuFuncs):
    #class for edit matchup menu instance
    def __init__(self, matchup_in):
        #set up matchup
        # matchup = {'row':series, 'df':df, 'mu':mustring}
        self.matchup = matchup_in
        self.prompt = self.matchup['mu']
        self.strflag = False
        self.optionslist = []
        self.functionslist = []
        self.printmenu = True
        self.menudict = {
            "Add wins":self.addWins,
            "Print matchup.":self.printMu,
            "Edit wins.":self.editWins,
            "index":[],
        }

        super().__init__() #make menu
        self.printMu()
    
    def addWins(self):
        # #print("hit addWins")
        mu = self.matchup #alias for quicker use
        #get user input
        prompt = f"New {mu['df'].columns[0]}"
        basic = mnus.BaseMenu(prompt)
        c1add = basic.basicIntLoop()
        basic.prompt = f"New {mu['df'].columns[1]}"
        c2add = basic.basicIntLoop()
        #add user input to existing values
        mu['row']['c1_wins'] += c1add
        mu['row']['c2_wins'] += c2add
        mu['row']['total_games'] = mu['row']['c1_wins'] + mu['row']['c2_wins']
        #print new matchup data
        self.matchup = self.makeMuObj(mu['row'])
        self.printMuObj("New Matchup: ")

        return False

    def printMu(self):
        # #print("hit printMu")
        self.printMuObj("Matchup: ")

        return False

    def editWins(self):
        #print("hit editWins")
        mu = self.matchup #alias for quick use
        #get user input
        basic = mnus.BaseMenu(f"Set {mu['df'].columns[0]} to")
        c1wins = basic.basicIntLoop()
        basic.prompt = f"Set {mu['df'].columns[1]} to>"
        c2wins = basic.basicIntLoop()
        #set values to user input
        mu['row']['c1_wins'] = c1wins
        mu['row']['c2_wins'] = c2wins
        mu['row']['total_games'] = mu['row']['c1_wins'] + mu['row']['c2_wins']
        #print new matchup data
        self.matchup = self.makeMuObj(mu['row'])
        self.printMuObj("New Matchup: ")

        return False

    def exitFunc(self):
        #print("hit Mu exitFunc")
        pass

    def returnFunc(self):
        #print("hit Mu returnFunc")
        # self.clearTerm()
        pass


"""------LIST MENUS-----------------------------------------------------"""