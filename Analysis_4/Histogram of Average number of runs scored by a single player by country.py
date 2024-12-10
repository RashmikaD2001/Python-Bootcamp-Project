import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/RashmikaD2001/Python-Bootcamp-Project/refs/heads/main/cleaned_data.csv"
crick_df = pd.read_csv(url)



# Group by 'team_1' and calculate total runs
team_stats = crick_df.groupby('team_1')['team_1_runs'].agg(['sum'])

# Rename columns for better clarity
team_stats = team_stats.rename(columns={'sum': 'Total Runs'})

# Display the table
print(team_stats)



# Group by 'team_2' and calculate total runs
team_stats = crick_df.groupby('team_2')['team_2_runs'].agg(['sum'])

# Rename columns for better clarity
team_stats = team_stats.rename(columns={'sum': 'Total Runs'})

# Display the table
print(team_stats)



# Group by 'team_1' and calculate total wickets
team_stats = crick_df.groupby('team_1')['team_1_wickets'].agg(['sum'])

# Rename columns for better clarity
team_stats = team_stats.rename(columns={'sum': 'Total wickets'})

# Display the table
print(team_stats)



# Group by 'team_2' and calculate total wickets
team_stats = crick_df.groupby('team_2')['team_2_wickets'].agg(['sum'])

# Rename columns for better clarity
team_stats = team_stats.rename(columns={'sum': 'Total wickets'})

# Display the table
print(team_stats)



# Get unique team names
all_teams = pd.unique(crick_df[['team_1', 'team_2']].values.ravel('K'))

# Create an empty dictionary to store batting averages
batting_averages = {}

# Calculate batting average for each team
for team in all_teams:
    # Calculate total runs and wickets for the team as team_1
    team_1_runs = crick_df[crick_df['team_1'] == team]['team_1_runs'].sum()
    team_1_wickets = crick_df[crick_df['team_1'] == team]['team_1_wickets'].sum()

    # Calculate total runs and wickets for the team as team_2
    team_2_runs = crick_df[crick_df['team_2'] == team]['team_2_runs'].sum()
    team_2_wickets = crick_df[crick_df['team_2'] == team]['team_2_wickets'].sum()

    # Calculate batting average for the team
    batting_avg = (team_1_runs / team_1_wickets if team_1_wickets else 0) + \
                   (team_2_runs / team_2_wickets if team_2_wickets else 0)

    # Store the batting average in the dictionary
    batting_averages[team] = batting_avg

# Create a DataFrame from the dictionary
batting_avg_df = pd.DataFrame.from_dict(batting_averages, orient='index', columns=['Batting Average'])

# Display the table
print(batting_avg_df)






plt.figure(figsize=(12, 6))
plt.bar(batting_avg_df.index, batting_avg_df['Batting Average'])
plt.xlabel('Country')
plt.ylabel('Batting Average')
plt.title('In each country, an individual player average runs scored in the whole World Cup history.')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()