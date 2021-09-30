import os

seasons = ["Spring", "Winter", "Summer", "Fall"]
dir = "D:\Developer\water_ml\Data\Bias_and_Alt\\{}\\{}_{}.csv"

def get_lines(filename, season, year):
    with open(filename, 'r') as file_object:
        lines = [l.strip() for l in file_object.readlines()]
    lines.pop(0)
    return [l + f",{season},{year}\n" for l in lines]


for season in seasons:
    filename = f"{season}_data.csv"
    total_data = ['site,bias,lat,long,Altitude,season,year\n']
    print(f"Processing season: {season}")
    
    for i in range(1995, 2018):
        total_data += get_lines(os.path.join("Data", "Bias_and_Alt", season, season.lower() + f"_{i}.csv"),
            season.lower(), i)
    
    with open(filename, 'w+') as file:
        file.writelines(total_data)
    
    print("File written.")
