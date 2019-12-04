import numpy as np

class Matchup():
    #basic class for holding matchup creation methods and arrays
    def __init__(self, char_stats):
        self.importStats(char_stats)
        self.makeMatchups(self.characters)

    def importStats(self, csv_in):
        #takes in str of the name of a csv file with character stats in it
        self.data = np.loadtxt(csv_in, delimiter=',', dtype='str')    

        #get headers array
        self.headers = self.data[0,:].copy()

        #make characters array  
        characters = self.data[1:,0].copy()
        self.characters = np.expand_dims(characters, axis=1)

        #get stats matrix
        stats = self.data[1:,1:].copy()
        self.stats = stats.astype(float)

    def makeMatchups(self, chars):
        #takes in np array containing list of characters and returns new array with all viable unique 1v1 matchups for those characters

        charchecklist = np.zeros_like(chars) #make column of zeros
        chars = np.append(chars, charchecklist, axis = 1) #attach col to chars array   

        matchups = [] #make new matchups array

        for char in chars:
            # print(char)
            # i = 0 #iteration tracker
            char[1] = "1" #mark the character as 'visited'
            for opponent in chars:
                if opponent[1] == "1": #if the opponent's mu list has already been added to the dict, pass.
                    pass
                else:
                    # i += 1 #iteration tracker
                    mu = (char[0], opponent[0]) # create matchup entry in list
                    # print(f"{i}.\t{mu}") print if need be
                    matchups.append(mu)

        self.matchups = np.array(matchups) #make the matchups an np array