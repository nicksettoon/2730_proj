#external libraries
import csv
import numpy as np
import pandas as pd
#custom imports

def normalizeStat(stat_challenger, stat_opponent):
    stat = (stat_challenger-stat_opponent)/(stat_challenger+stat_opponent)
    return stat


        
def main():
    # t1 = Tournament("Let's Make Moves")
    t1 = Tournament("Frostbite 2019")
    t1.printDF()
    # t1.saveDF()

    
if __name__ == "__main__": main()
else:
    print("What you doin' willis.")
