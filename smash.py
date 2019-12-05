#external libraries
# import csv
import numpy as np
import pandas as pd
import os
from tabulate import tabulate

#custom imports
from Tournament import Tournament as T
from Menu import MenuBase, Menu, ListMenu, FunctionMenu
from Matchup import MatchupStats as MUS

def normalizeStat(stat_challenger, stat_opponent):
    stat = (stat_challenger-stat_opponent)/(stat_challenger+stat_opponent)
    return stat

class StartMenu(FunctionMenu):
    #Class for start menu options
    def __init__(self):
        print("Welcome to the Smash Ultimate Tournament Data Builder!")
        self.prompt = "SMASH"
        # self.menutype = "functions"
        self.optionlist = [
            "Open a tournament.",
            "Make a tournament.",
            "DONT USE ME YET.",
            "DONT USE ME YET."
        ]

        self.functionlist = [
            self.queryTournament,
            self.makeTournament,
            self.editGlobalMUs,
            self.queryGlobalMUs
        ]
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
        self.optionlist = [
            "Print current tournament.",
            "Restart",
            "Save tournament",
            "Rename tournament."
        ]
        self.functionlist = [
            self.printTournament,
            self.restartMake,
            self.saveTournament,
            self.renameTournament
        ]

        self.tournament = self.makeTournament()
        super().__init__(self.prompt)

    def restartMake(self):
        self.tournament = self.makeTournament()

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
        # print(matchup.characters)

        self.optionlist = matchup.characters.ravel()

class EditMatchup(FunctionMenu):
    #class for edit matchup menu instance
    def __init__(self, matchup_in):
        #set up matchup
        # matchup = {'row':series, 'df':df, 'mu':mustring}
        self.matchup = matchup_in
        self.prompt = self.matchup['mu']
        self.printmenu = True
        self.optionlist = [
            "Add wins",
            "Print matchup.",
            "Edit wins."
        ]
        self.functionlist = [
            self.addWins,
            self.printMu,
            self.editWins
        ]

        super().__init__(self.prompt) #make menu
    
    def addWins(self):
        print("hit addWins")
        print(self.matchup)

        basic = MenuBase(f"New {self.char1} wins: ")
        c1add = basic.basicIntLoop()
        basic.prompt = f"New {self.char2} wins: "
        c2add = basic.basicIntLoop()

        # print(self.matchup)

        # c1wins = int(self.matchup.at[0,'char1_wins'])
        c1wins = self.matchup['char1_wins'].iloc[0]
        print(type(c1wins))
        print(type(c1add))
        self.matchup.loc[self.matchup.index[0], 'char1_wins'] = c1wins + c1add
        
        print(self.matchup) 
        # char2wins = self.matchup.loc[0,'char2_wins']
        # self.matchup.set_value(0,'char2_wins', char2wins + c2add)

        # c1wins = self.matchup['char1_wins']
        # char2wins = self.matchup['char2_wins']
        # c1wins[0] = c1wins[0] + c1add
        # char2wins[0] = char2wins[0] + c1add
        # self.matchup['char1_wins'].iat[0] = self.matchup['char1_wins'].iat[0] + c1add
        # self.matchup['char2_wins'].iat[0] = self.matchup['char2_wins'].iat[0] + c2add

    def printMu(self):
        self.clearTerm()
        print(f"Matchup: {self.matchup['mu']}\n")
        self.printmenu = False
        return print(tabulate(self.matchup['df'], headers='keys', showindex=False))

    def editWins(self):
        print("hit editwins")
        
        basic = MenuBase(f"{self.char1} wins: ")
        c1wins= basic.basicIntLoop()
        basic.prompt(f"{self.char2} wins: ")
        char2wins = basic.basicIntLoop()

        self.matchup['char1_wins'].iat[0] = c1wins
        self.matchup['char2_wins'].iat[0] = char2wins

class QueryTournament(FunctionMenu):
    #class for menu of options related to a specific Tournament
    def __init__(self, tournament_name):
        #menu setup
        self.prompt = tournament_name
        self.optionlist = [
            "Print tournament. (all matchups)",
            "Edit matchup",
            "Print matchup",
            "Print non-zero matchups",
            "Print matchups above threshold.",
        ] #set options visible to user

        self.functionlist = [
            self.printTournament,
            self.editMus,
            self.printMu,
            self.printNonZeroMus,
            self.printThreshMus,
        ] #set list of functions those options map to

        #make and load tournament 
        self.tournament = T(tournament_name)
        self.tournament.loadDF()
        super().__init__(tournament_name) #make menu

    def editMus(self):
        #creates mu object and editMatchup menu instance, then hands off to its prompt
        print("hit editMus")
        series = self.getMuSeries()
        if series is not None:
            editor = EditMatchup(self.makeMuObj(series)) #make menu instance for editing matchup

        self.clearTerm()
        return editor.startPrompt("") #start prompt
    
    def makeMuObj(self, series):
        #turns matchup series into printable dataframe
        mustring = f"{series.name[0]}_x_{series.name[1]}"
        # print("\n"+mustring)
        df = series.to_frame().T
        df.rename( columns ={ df.columns[0] : f"{series.name[0]}_wins", df.columns[1] : f"{series.name[1]}_wins" }, inplace=True)

        return {'row':series, 'df':df, 'mu':mustring}

    def printMu(self):
        series = self.getMuSeries()
        if series is not None:
            mu = self.makeMuObj(series)
        self.clearTerm()
        print(f"Matchup: {mu['mu']}\n")
        print(tabulate(mu['df'], headers='keys', showindex=False))
        return False

    def getMuSeries(self, mu_in=[]):
        #function that gets the matchup series for two given characters
        #if no mu_in pair is given, prompts user
        if mu_in == []:
            Clist = SelectCharacter(self.prompt) #set up character list menu
            #get first character in the matchup
            mu_in.append(Clist.startPrompt("Please select the first character in the matchup."))
            if mu_in[0] == True:#if recieved quit
                return True 
            elif mu_in[0] == False:#if received back
                return False
            matchup = mu_in[0] + "_x_" # make new prompt
            #get second character in the matchup
            Clist.prompt = matchup 
            Clist.printmenu = False
            mu_in.append(Clist.startPrompt(f"First char: {mu_in[0]}\nPlease select the second character in the matchup."))
            if mu_in[1] == True:
                return True
            elif mu_in[1] == False:
                return False
        try: #find series which matches the matchup pair
            series = self.tournament.df.xs((mu_in[0],mu_in[1]))
        except KeyError:
            try:#search for inverse of pair
                series = self.tournament.df.xs((mu_in[1],mu_in[0]))
            except KeyError:
                if mu_in[0] == mu_in[1]:
                    print("Matchup is a ditto. Dittos are redundant so they have been excluded.")
                else:
                    print("You should not be here.")
                series = None #create return list
        return series

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

    def printTournament(self):
        print("hit printTournament")
        self.tournament.printDF()

        return False


def main():
    # start = StartMenu()
    # start.startPrompt("")

    query = QueryTournament("test")
    # query.getMuSeries(['Banjo', 'Bayonetta'])
    query.startPrompt("")

    # maker = MakeTournament()
    # maker.startPrompt("")

    # editor = EditMatchup() #make menu for matchup
    # editor.startPrompt("")
    print("Closing Main")

if __name__ == "__main__": main()
else: print("What you doin' willis.")
