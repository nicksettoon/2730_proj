import pandas as pd

#custom imports
from Matchup import MatchupStats as MUS
from NParray import NParray as NP

class Tournament():
    #class that holds tournament matchup result self.data
    def __init__(self, name):
        self.name = name

    def makeDF(self):
        #init matchup array
        matchup = MUS("char_stats.csv")
        matchup.loadStats()
        matchup.makeMatchups()
        mudata = matchup.muarray.copy()

        #make panda data frame for easy viewing
        mudata = NP.addCol(mudata, 1)
        
        self.df = pd.DataFrame(mudata, columns=["char1", "char2", "char1_wins", "char2_wins"])
        self.df["total_games"] = self.df["char1_wins"] + self.df["char2_wins"]

    def printDF(self):
        print(self.name)
        print(self.df)
    
    def saveDF(self):
        self.df.dropna()
        export_csv = self.df.to_csv(f"./tournaments/{self.name}.tmnt", index=False)
    
    def loadDF(self):
        try:
            self.df = pd.read_csv(f"./tournaments/{self.name}.tmnt")
            print(f"Found csv for {self.name}.")
            return True
        except FileNotFoundError:
            return False
    
    def editDF(self):
        print("hit editDF")