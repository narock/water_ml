import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics



waterAverage = pd.read_csv("D:\Developer\water_ml\Data\Sitesbycords-fall.csv", sep=r'\s*,\s*')
#waterAverage = pd.read_csv("D:\Developer\water_ml\Data\Sitesbycords-winter.csv", sep=r'\s*,\s*')
#waterAverage = pd.read_csv("D:\Developer\water_ml\Data\Sitesbycords-spring.csv", sep=r'\s*,\s*')
#waterAverage = pd.read_csv("D:\Developer\water_ml\Data\Sitesbycords-summer.csv", sep=r'\s*,\s*')


#y = np.array(waterAverage['average'])
y = np.array(waterAverage['NSE_state'])
X = np.array(waterAverage[['dec_lat_va','dec_long_va']])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)




#clf = RandomForestRegressor(n_estimators=5000,  random_state=100)
clf = RandomForestClassifier(n_estimators=5000,  random_state=100)


clf.fit(X_train, y_train)

y_predict = clf.predict(X_test)


print('Accuracy: %.2f' 
      % metrics.accuracy_score(y_predict,y_test))
print('Mean squared error: %.2f'
      % metrics.mean_squared_error(y_test, y_predict))
print(metrics.classification_report(y_predict,y_test))
# print('Coefficient of determination: %.2f'
#       % metrics.r2_score(y_test, y_predict))