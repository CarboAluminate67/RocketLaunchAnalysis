import numpy as np
import pandas as pd
import matplotlib.pyplot as plot


# Opening csv files
launches = pd.read_csv('archive/Launches.csv')
configs = pd.read_csv('archive/Configs.csv')

# Setting up dataframes/Cleaning data
launches = launches.drop(["Launch Suborbital", "Launch Year Mon", "2021 Mult", "Dum"], axis=1)
launches = launches.sort_values(by=['Rocket Name'])
launches = launches.dropna(subset='USD/kg to LEO CPI Adjusted')

debut = launches[["Rocket Name", "Launch Time"]]
debut.insert(2, "First Launch", 'NA')

configs.insert(13, 'Debut', 'NA')

# Formatting dataframe
try:
    configs['Liftoff Thrust (kN)'] = configs['Liftoff Thrust (kN)'].astype(int)
except:
    pass

# Function to shorten date
def getDate(d):
    try:
        return int(d[0:4])
    except:
        return "Planned"

# Extracts earliest launch date for each vehicle and adds column to dataframe
previous = 'NA'
debutList = {}

for rocket in debut['Rocket Name']:
    if rocket != previous:
        min_date = debut[debut['Rocket Name'] == rocket]['Launch Time'].min()
        debut.loc[debut['Rocket Name'] == rocket, 'First Launch'] = getDate(min_date)
        debutList[rocket] = getDate(min_date)

    previous = rocket

# Adding debut date to config dataframe
for rocket in configs["Config"]:
    try:
        configs.loc[configs['Config'] == rocket, 'Debut'] = debutList[rocket]
    except:
        configs.loc[configs['Config'] == rocket, 'Debut'] = "Planned"

launches = launches.sort_values(by=['Launch Time'])

print(launches)

# Plotting first launch of vehicle vs liftoff thrust
configs.loc[configs['Debut'] != 'Planned'].plot.scatter(x="Debut", y="Liftoff Thrust (kN)", alpha=0.5)

plot.show()

# Plotting first launch of vehicle vs cost efficiency
launches.plot.scatter(x="Launch Year", y="USD/kg to LEO CPI Adjusted", alpha=0.5)

plot.show()

# Analyzing data on launch providers
companyNum = launches.nunique(0, True)[4]

print(f"Number of Launch Providers: {companyNum}")

print(launches["Rocket Organisation"].value_counts())

companyLaunches = pd.DataFrame()
companyLaunches['Launches'] = launches.groupby('Rocket Organisation').filter(lambda x: len(x)>10)["Rocket Organisation"].value_counts()

# Analyzing success rates
successes = launches.value_counts(subset='Launch Status')

total = successes['Success'] + successes['Failure'] + successes['Partial Failure'] + successes['Prelaunch Failure']
successRate = round((successes['Success']/total)*100, 2)

print(f"Total Success Rate: {successRate}%")

companyLaunches['Successes'] = launches[launches['Launch Status'] == "Success"].groupby('Rocket Organisation').filter(lambda x: len(x)>10)["Rocket Organisation"].value_counts()
companyLaunches['Failures'] = companyLaunches['Launches'] - companyLaunches['Successes']
companyLaunches['Rate'] = round((companyLaunches['Successes']/companyLaunches['Launches'])*100, 2)

companyLaunches['Launches'].plot.bar()

plot.show()

companyLaunches.plot.scatter(x='Launches', y='Rate', alpha=0.5)

plot.show()


companyLaunches.sort_values('Rate')['Rate'].plot.bar()

plot.show()

print(companyLaunches)
