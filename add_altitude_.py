import pandas as pd

seasons = ["Spring", "Winter", "Summer"]
dir = "D:\Developer\water_ml\Data\{}\\{}_{}.csv"

altitude_data = pd.read_csv("D:\Developer\water_ml\Data\\all_sites_features_altitude.csv", sep=r'\s*,\s*')

starting_year = 1995


for season in seasons:

    for i in range(23):

        season_data = pd.read_csv(dir.format(season, season.lower(),i + starting_year), sep=r'\s*,\s*')

        merged_data = pd.merge(season_data,altitude_data, on = "site", how = "inner").drop(columns=["Unnamed: 5", "Unnamed: 6"])


        merged_data = merged_data[merged_data["Altitude"].notna()]

        merged_data.to_csv(dir.format(season, season.lower(),i + starting_year))