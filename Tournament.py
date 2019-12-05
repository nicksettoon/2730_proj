import pandas as pd
import numpy as np

#custom imports
from Matchup import MatchupStats as MUS
# from NParray import NParray as NP

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

        #make two series for holding the zeros 
        size = len(mudata)
        print(size)
        zeros = np.zeros((size,2))
        print(zeros)
        
        mindex = pd.MultiIndex.from_tuples(mudata, names=['c1','c2'])
        self.df = pd.DataFrame(zeros.astype(int),columns=['c1_wins', 'c2_wins'], index=mindex)
        self.df["total_games"] = self.df["c1_wins"] + self.df["c2_wins"]

    def printDF(self):
        print(self.name)
        print(self.df)
    
    def saveDF(self):
        self.df.dropna()
        export_csv = self.df.to_csv(f"./tournaments/{self.name}.tmnt", index=True) #write to csv
    
    def loadDF(self):
        try:
            self.df = pd.read_csv(f"./tournaments/{self.name}.tmnt") #read in csv
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
            return False
    
    def editDF(self):
        print("hit editDF")