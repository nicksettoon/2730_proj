import pandas as pd

#custom imports
from Matchup import Matchup as MU
from NParray import NParray as NP

class Tournament():
    #class that holds tournament matchup result self.data
    def __init__(self, name):
        self.name = name

    def makeDF(self):
        #init matchup array
        self.matchup = MU("char_stats.csv")
        self.mudata = self.matchup.matchups

        #make panda data frame for easy viewing
        self.mudata = NP.addCol(self.mudata, 1)
        
        self.df = pd.DataFrame(self.mudata, columns=["char1", "char2", "char1_wins", "char2_wins"])
        self.df["total_games"] = self.df["char1_wins"] + self.df["char2_wins"]

    def printDF(self):
        print(self.name)
        print(self.df)
    
    def saveDF(self):
        export_csv = self.df.to_csv(f"./tournaments/{self.name}.tmnt", index=False)
    
    def loadDF(self):
        try:
            self.df = pd.read_csv(f"./tournaments/{self.name}.tmnt")
            print(f"Found csv for {self.name}.")
            return True
        except FileNotFoundError:
            # print("No tournament was found with that name. Making new one.")
            # print("You should never have issues finding a tournament.")
            # print("Something went wrong with SelectTournament().")
            return False
    
    def editDF(self):
        print("hit editDF")