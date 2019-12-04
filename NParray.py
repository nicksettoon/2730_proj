import numpy as np

class NParray():
    #wrapper for custom NParray functions
    def __init__(self):
        pass
        # self.arr = np.array()
    
    def addCol(array_in, num_to_add):
        zeroes = np.zeros_like(array_in)
        arrayout = array_in
        i = 1
        while(i <= num_to_add):
            arrayout = np.append(arrayout, zeroes, axis=1)
            i += 1
        return arrayout