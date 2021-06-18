import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import plot_confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

seasons = ["Fall", "Spring", "Winter", "Summer"]
dir = "D:\Developer\water_ml\Data\{}\\{}_{}.csv"
starting_year = 1995
for season in seasons:
    for i in range(23):
        waterAverage = pd.read_csv(dir.format(season, season.lower(),i + starting_year), sep=r'\s*,\s*')

        y = np.array(waterAverage['range'])
        X = np.array(waterAverage[['lat_x','long_x', "Altitude"]])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        clf = SVC()

        clf.fit(X_train, y_train)

        y_predict = clf.predict(X_test)

        plot_confusion_matrix(clf, X_test, y_test)

        plt.savefig("D:\Developer\water_ml\Data\SVMResults\Confusion_Matrix_Plots\\{}\\{}_{}.png".format(season,season.lower(),i + starting_year))
