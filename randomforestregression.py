import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, recall_score, f1_score
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics



#waterAverage = pd.read_csv("D:\Developer\water_ml\Data\Fall\\fall_2017.csv", sep=r'\s*,\s*')
#waterAverage = pd.read_csv("D:\Developer\water_ml\Data\Spring\\spring_2017.csv", sep=r'\s*,\s*')
#waterAverage = pd.read_csv("D:\Developer\water_ml\Data\Winter\\winter_2017.csv", sep=r'\s*,\s*')
waterAverage = pd.read_csv("D:\Developer\water_ml\Data\Summer\\summer_2017.csv", sep=r'\s*,\s*')

y = np.array(waterAverage['range'].dropna())
X = np.array(waterAverage[['lat','long']].dropna())



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)



clf = RandomForestClassifier(n_estimators=5000,  random_state=100)


clf.fit(X_train, y_train)

y_predict = clf.predict(X_test)


print('f1-score: %.2f' 
      % metrics.f1_score(y_test, y_predict, average = "micro"))
#print(metrics.classification_report(y_predict,y_test))
