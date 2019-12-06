import numpy as np
import pandas as pd
from tabulate import tabulate

from CHARs import characters as chars


def main():
    clist = chars.SelCharMenu("get dem chars>")
    charlist = clist.optionslist

    # print(charcodes)
    # print(tabulate(csindex, tablefmt="grid"))
    # listsize = len(selChars.optionlist)
    # if listsize > 30: 
    #     i = 2
    #     divsize = listsize
    #     while(divsize > 30):
    #         divsize = listsize//i
    #         i += 1 
    #     arr = np.array_split(selChars.optionlist, i)
    #     # print(arr[0])

    #     seriesdict = {}
    #     for arrindex, array in zip(np.arange(i), arr):
    #         seriesdict[str(arrindex)] = pd.Series(array)
    #         seriesdict[str(arrindex)].index
            
        # print(seriesdict)

    # df = pd.DataFrame(selChars.optionlist)
    # df.index += 1
    # print(df.T)
    # print(tabulate(df, tablefmt="psql"))

if __name__ == "__main__":
    main()