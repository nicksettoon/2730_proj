#EXTERNAL IMPORTS#
import numpy as np
import pandas as pd
import os
# from tabulate import tabulate

#CUSTOM IMPORTS#
from MNUs import menus as mnus
from MUs import matchups as mus
import tournaments as tmnt
from CHARs import characters as chars
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score 
from sklearn.svm import SVC

def main():

    meta = tmnt.Tmnt("META")
    tdflist = meta.loadAllTmnts()
    meta.sumAllTmnts(tdflist)
    
    muload = mus.MuStats("./CHARs/char_stats.csv")
    muload.loadMuStats()
    muload.genMuArray()
    muload.getMuStats()

    matchups = muload.MUdf.to_csv("./MUs/MUstats.csv")
    results = meta.df.to_csv("./MUs/MUresults.csv")

    matchups = muload.MUdf.to_numpy()
    results = meta.df.to_numpy()
    print(matchups.shape)
    print(results.shape)
    dataset = np.concatenate((matchups, results), 1)
    print(dataset.shape)

    mutrain, mutest, ytrain, ytest = train_test_split(dataset, results[:,:2], test_size=0.25, random_state=123)

    # print(mutrain.shape)
    # print(mutest.shape)

    # print(ytrain.shape) #bad input shape (2310,2)
    # print(ytest.shape)

    # X = mutrain
    # y = ytrain

    # for num in (20, 100, 500, 1000):
    #     rfc = RandomForestClassifier(n_estimators=num)
    #     rfc = rfc.fit(X,y)
    #     rf_pred = rfc.predict(mutest)
    #     print(accuracy_score(ytest, rf_pred))

    # for c in [0.01, 0.1, 1, 10, 30, 500]:
    #     model = SVC(kernel='linear', C=c)
    #     model.fit(X,y)
    #     y_pred = model.predict(mutest)
    #     print(accuracy_score(ytest, ypred))
# from sklearn.ensemble import RandomForestClassifier


































if __name__ == "__main__": main()
else: print("What you doin' willis.")