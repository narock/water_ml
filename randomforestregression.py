import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics


waterAverage = pd.read_csv("Data\Seasonal_Summaries\sites_fall_clean.csv", sep=r'\s*,\s*')
#waterAverage = pd.read_csv("Data\Seasonal_Summaries\sites_spring_clean.csv", sep=r'\s*,\s*')
#waterAverage = pd.read_csv("Data\Seasonal_Summaries\sites_summer_clean.csv", sep=r'\s*,\s*')
#waterAverage = pd.read_csv("Data\Seasonal_Summaries\sites_winter_clean.csv", sep=r'\s*,\s*')

X = np.array(waterAverage['site_no'])
Y = np.array(waterAverage['average'])


X_train = X[:-20]
X_test = X[-20:]
y_train = Y[:-20]
y_test = Y[-20:]


X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)

clf = RandomForestRegressor(n_estimators=5000,  random_state=100)

clf.fit(X_train, y_train)

y_predict = clf.predict(X_test)

print('Mean squared error: %.2f'
      % metrics.mean_squared_error(y_test, y_predict))
print('Coefficient of determination: %.2f'
      % metrics.r2_score(y_test, y_predict))