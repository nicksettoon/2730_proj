import pandas as pd

#custom imports
from Matchup import Matchup as MU
from NParray import NParray as NP

class Tournament():
    #class that holds tournament matchup result self.data
    def __init__(self, name):
        self.name = name
        
        try:
            self.loadDF()
            print(f"Found csv for {self.name}.")
        except FileNotFoundError:
            print("No tournament was found with that name. Making new one.")
            self.makeDF()

    def makeDF(self):
        #init matchup array
        self.matchup = MU("char_stats.csv")
        self.mudata = self.matchup.matchups

        #make panda data frame for easy viewing
        self.mudata = NP.addCol(self.mudata, 1)
        
        self.df = pd.DataFrame(self.mudata, columns=["char1", "char2", "char1_wins", "char2_wins"])
        self.df["total_games"] = self.df["char1_wins"] + self.df["char2_wins"]

        #make stream object for writing to file
        # with open(f"{name}.csv", 'w') as csvfile:
            # self.outstream = csv.writer(csvfile)
    
    def printDF(self):
        print(self.name)
        print(self.df)
    
    def saveDF(self):
        export_csv = self.df.to_csv(f"{self.name}.csv", index=False)
    
    def loadDF(self):
        self.df = pd.read_csv(f"{self.name}.csv")