import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score, plot_confusion_matrix
from sklearn.ensemble import  RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

seasons = ["Fall", "Spring", "Winter", "Summer"]
dir = "D:\Developer\water_ml\Data\{}\\{}_{}.csv"
starting_year = 1995
for season in seasons:
    #df = pd.DataFrame()
    for i in range(23):
        waterAverage = pd.read_csv(dir.format(season, season.lower(),i + starting_year), sep=r'\s*,\s*')

        y = np.array(waterAverage['range'].dropna())
        X = np.array(waterAverage[['lat','long']].dropna())

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        clf = RandomForestClassifier(n_estimators=5000,  random_state=100)

        clf.fit(X_train, y_train)

        y_predict = clf.predict(X_test)

        plot_confusion_matrix(clf, X_test, y_test)

        plt.savefig("D:\Developer\water_ml\Data\Confusion_Matrix_Plots\{}\\{}_{}.png".format(season,season.lower(),i + starting_year))

        #f1_score =  metrics.f1_score(y_test, y_predict, average = "micro")


        #df["Year"] = i + starting_year
        #df["F1 Score"] = f1_score

   #df.to_csv(r"D:\Developer\water_ml\Data\{}f1_score.csv".format(season), index = False)



