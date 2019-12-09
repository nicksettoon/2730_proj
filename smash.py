#EXTERNAL IMPORTS#
import numpy as np
import pandas as pd
import os
# from tabulate import tabulate

#CUSTOM IMPORTS#
from MNUs import menus as mnus
from MUs import matchups as mus
from TMNTs import tournaments as tmnt
from CHARs import characters as chars
from sklearn.model_selection import train_test_split

def main():

    meta = tmnt.Tmnt("META")

    meta.loadAllTmnts()


    from sklearn.model_selection import train_test_split
    docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=123)

    from sklearn.svm import SVC
    X = train_fit
    y = y_train
    for c in [0.01, 0.1, 1, 10, 30, 500]:
        model = SVC(kernel='linear', C=c)
        model.fit(X,y)
        y_pred = model.predict(test_tran)
        print(accuracy_score(y_test, y_pred))

if __name__ == "__main__": main()
else: print("What you doin' willis.")