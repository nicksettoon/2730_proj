#EXTERNAL IMPORTS#
import numpy as np
import pandas as pd
#CUSTOM IMPORTS#
from MUs import matchups as mus
from MNUs import menus as mnus

def normalizeStatFunc(stat_challenger, stat_opponent):
    stat = (stat_challenger-stat_opponent)/(stat_challenger+stat_opponent)
    return stat

class SelCharMenu(mnus.ListMenu):
    #class for listing and selecting characters
    def __init__(self, prompt_in):
        self.strflag = True
        self.prompt = prompt_in
        muloader = mus.MuStats("./CHARs/char_stats.csv")
        muloader.loadMuStats()

        self.optionslist = muloader.characters.ravel().tolist()
        # self.optionslist = np.concatenate(self.optionslist, self.genCharCodes())
        self.optionslist.append(self.genCharCodes())
        print(self.optionslist)
        super().__init__()
    
    def genCharCodes(self):
        charcodes = []
        taglist = []
        for char in self.optionslist:
            newchar = char.replace("_","")
            newchar = newchar.replace("-","")
            tag = newchar[:4].lower()
            taglist.append(tag)
        charcodes = np.array(taglist)
        # for i, tag, char in zip(np.arange(len(charcodes)), charcodes, clist.optionlist):
        #     print(f"{i}.\t{tag}\t{char}")
        charcodes[3] = "bowj"
        charcodes[9] = "drkp"
        charcodes[10] = "drks"
        charcodes[28] = "kddd"
        charcodes[33] = "rage"

        return charcodes

        # optionlist = pd.Series(self.optionlist)
        # optionlist.index = charcodes
        # self.optionlist = optionlist

