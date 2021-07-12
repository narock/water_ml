import matplotlib.pyplot as plt
import pandas as pd

seasons = ["Spring", "Winter", "Summer","Fall"]
dir = "D:\Developer\water_ml\Data\Bias_By_Year\{}\{}_{}.csv"
starting_year = 1995
save_dir = "D:\Developer\water_ml\Data\Bias_plots\{}\{}_{}.png"


for season in seasons:
    for i in range(23):

        file = pd.read_csv(dir.format(season, season.lower(),i + starting_year), sep=r'\s*,\s*')
        file = file.dropna()

        plt.boxplot(file["bias"])
        plt.ylabel("Bias")
        plt.title("{}_{}".format(season, i+starting_year))

        plt.savefig(save_dir.format(season, season.lower(),i + starting_year))
