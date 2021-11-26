import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

seasons = ["Fall", "Spring", "Winter", "Summer"]
starting_year = 1995
for idx, season in enumerate(seasons):
    waterAverage = pd.read_csv(f"{season}_data.csv", sep=r'\s*,\s*')

    y = np.array(waterAverage['bias'])
    seasons_encoded = np.array(
        [idx for _ in range(waterAverage['season'].shape[0])])
    seasons_encoded = seasons_encoded.reshape(-1, 1)
    X = np.array(waterAverage[['lat', 'long', "Altitude", "year"]])
    print(seasons_encoded.shape)
    X = np.append(X, seasons_encoded, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.33,
                                                        random_state=42)

    clf = RandomForestRegressor(n_estimators=5000, random_state=100)

    clf.fit(X_train, y_train)

    y_predict = clf.predict(X_test)

    print(f"For {season} our MSE is {mean_squared_error(y_test,y_predict)}")
