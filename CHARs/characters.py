#EXTERNAL IMPORTS#
#CUSTOM IMPORTS#
from MUs import matchups as mus
from MNUs import menus as mnus

def normalizeStatFunc(stat_challenger, stat_opponent):
    stat = (stat_challenger-stat_opponent)/(stat_challenger+stat_opponent)
    return stat

class SelChar(mnus.ListMenu):
    def __init__(self, prompt_in):
        self.getCharacters()
        super().__init__(prompt_in)
    
    def getCharacters(self):
        # print("Hit getCharacters")
        muloader = mus.MuStats("./CHARs/char_stats.csv")
        muloader.loadMuStats()

        self.optionlist = muloader.characters.ravel()
