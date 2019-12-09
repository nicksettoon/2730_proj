#EXTERNAL IMPORTS#
import numpy as np
import pandas as pd
#CUSTOM IMPORTS#
from MUs import matchups as mus
from MNUs import menus as mnus


class SelCharMenu(mnus.ListMenu):
    #class for listing and selecting characters
    def __init__(self, prompt_in):
        self.strflag = True
        self.prompt = prompt_in
        muloader = mus.MuStats("./CHARs/char_stats.csv")
        muloader.loadMuStats()

        self.optionslist = muloader.characters.ravel().tolist()
        super().__init__()
    
    #     charcodes[3] = "bowj"
    #     charcodes[9] = "drkp"
    #     charcodes[10] = "drks"
    #     charcodes[28] = "kddd"
    #     charcodes[33] = "rage"
