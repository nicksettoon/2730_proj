import csv
import numpy as np
import pandas as pd

def normalizeStat(stat_challenger, stat_opponent):
    stat = (stat_challenger-stat_opponent)/(stat_challenger+stat_opponent)
    return stat


class tournament():


def main():

    filename = "stats.csv"
    headers, chars, stats = importStats(filename)

    mutemplate = makeMatchups(chars)


    # muarray = getMatchups(chars)
    # mudata = np.array(getMatchups("stats.csv"))
    # pdmus = pd.DataFrame(mudata, columns=["plyr1", "opponent"])
    # print(mudata.shape)
    # print(pdmus)
    


def importStats(csv_in):
    #takes in str of the name of a csv file with character stats in it
    data = np.loadtxt(csv_in, delimiter=',', dtype='str')    

    #get headers array
    headers = data[0,:].copy()

    #make characters array  
    characters = data[1:,0].copy()
    characters = np.expand_dims(characters, axis=1)

    #get stats matrix
    stats = data[1:,1:].copy()
    stats.astype(float)

    return headers, characters, stats

def makeMatchups(chars):
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

    matchups = np.array(matchups) #make the matchups an np array

    return matchups

if __name__ == "__main__":
    main()
else:
    print("What you doin' willis.")
