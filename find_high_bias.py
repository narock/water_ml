import pandas as pd
from pandas.core.frame import DataFrame

seasons = ["Spring", "Winter", "Summer","Fall"]
dir = "D:\Developer\water_ml\Data\Bias_By_Year\{}\{}_{}.csv"
starting_year = 1995
save_dir = "D:\Developer\water_ml\Data\Largest_Bias\\largest_bias_{}_{}.csv"

for season in seasons:
    for i in range(23):
        file = pd.read_csv(dir.format(season, season.lower(),i + starting_year), sep=r'\s*,\s*')
        file = file.dropna()

        if season == "Fall":
            sites = [x for x, y in zip(file["site"], file["bias"]) if y >= 57846.58]
        if season == "Winter":
            sites = [x for x, y in zip(file["site"], file["bias"]) if y >= 316711.7]
        if season == "Summer":
            sites = [x for x, y in zip(file["site"], file["bias"]) if y >= 180892.37]
        if season == "Spring":
            sites = [x for x, y in zip(file["site"], file["bias"]) if y >= 502921.3]

        df = pd.DataFrame(sites)

        if(not df.empty):
            df.to_csv(save_dir.format(season.lower(), i + starting_year))


