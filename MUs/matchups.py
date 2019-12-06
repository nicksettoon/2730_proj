#EXTERNAL IMPORTS#
import numpy as np
from tabulate import tabulate
#CUSTOM IMPORTS#
from MNUs import menus as mnus

"""------CLASSES--------------------------------------------------------"""

class Mu():
    def __init__(self):
        pass

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
        print("Hit Mu returnFunc")
        # self.matchup = None
        # self.tmnt.saveDF()
        print(f"{prefix_in}{self.matchup['mu']}\n")
        self.printmenu = False
        return print(tabulate(self.matchup['df'], headers='keys', showindex=False))

class MuStats():
    #basic class for holding matchup creation methods and arrays
    def __init__(self, file_name):
        self.filename = file_name
        # self.loadStats(file_name)
        # self.makeMuArray()

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
        # print("hit addWins")
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
        # print("Hit printMu")
        self.printMuObj("Matchup: ")

        return False

    def directEdit(self, c1wins, c2wins):
        print("hit directEdit")
        mu = self.matchup
        mu['row']['c1_wins'] = c1wins
        mu['row']['c2_wins'] = c2wins
        mu['row']['total_games'] = mu['row']['c1_wins'] + mu['row']['c2_wins']
        #print new matchup data
        self.matchup = self.makeMuObj(mu['row'])
        self.printMuObj("New Matchup: ")

        return False

    def editWins(self):
        print("hit editWins")
        mu = self.matchup #alias for quick use
        #get user input
        basic = mnus.BaseMenu(f"Set {mu['df'].columns[0]} to")
        c1wins = basic.basicIntLoop()
        basic.prompt = f"Set {mu['df'].columns[1]} to"
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
        print("Hit Mu exitFunc")

    def returnFunc(self):
        print("Hit Mu returnFunc")
        # self.clearTerm()


"""------LIST MENUS-----------------------------------------------------"""