from pybaseball import statcast
import pandas as pd



# Pull Statcast data for the 2023 season
statcast_data = statcast(start_dt="2023-03-30", end_dt="2023-10-01", team=None, verbose=True, parallel=True)

# Pull Statcast data for the 2024 season
statcast_data_24 = statcast(start_dt="2024-03-30", end_dt="2024-10-01", team=None, verbose=True, parallel=True)

# Filter the data for only the first inning 2023 season
first_inning_data = statcast_data[statcast_data['inning'] == 1]

# Filter the data for only the first inning 2024 season
first_inning_data_24 = statcast_data_24[statcast_data_24['inning'] == 1]


# Save the 2023 season filtered data to a CSV file
first_inning_data.to_csv('statcast_2023_first_inning.csv', index=False)

# Save the 2024 season filtered data to a CSV file
first_inning_data_24.to_csv('statcast_2024_first_inning.csv', index=False)

print("Statcast data for the first inning of the 2023 season has been successfully saved to 'statcast_2023_first_inning.csv'")
print("Statcast data for the first inning of the 2024 season has been successfully saved to 'statcast_2024_first_inning.csv'")
