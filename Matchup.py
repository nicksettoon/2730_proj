import numpy as np

class MatchupStats():
    #basic class for holding matchup creation methods and arrays
    def __init__(self, file_name):
        self.filename = file_name
        # self.loadStats(file_name)
        # self.makeMatchups()

    def loadStats(self):
        #takes in str of the name of a csv file with character stats in it
        self.data = np.loadtxt(self.filename, delimiter=',', dtype='str')    

        #get headers array
        self.headers = self.data[0,:].copy()
        #make characters array  
        self.characters = self.data[1:,0].copy()
        self.characters = np.expand_dims(self.characters, axis=1)
        #get stats matrix
        self.stats = self.data[1:,1:].copy().astype(float)

    def makeMatchups(self):
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

        self.muarray = np.array(matchups) #make the matchups an np array