import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/RashmikaD2001/Python-Bootcamp-Project/refs/heads/main/cleaned_data.csv"
crick_df = pd.read_csv(url)

# Group by 'team_1' and calculate total wickets
team_stats = crick_df.groupby('team_1')['team_1_wickets'].agg(['sum'])

# Rename columns for better clarity
team_stats = team_stats.rename(columns={'sum': 'Total Wickets'})

# Display the table
print(team_stats)



# Group by 'team_2' and calculate total wickets
team_stats = crick_df.groupby('team_2')['team_2_wickets'].agg(['sum'])

# Rename columns for better clarity
team_stats = team_stats.rename(columns={'sum': 'Total Wickets'})

# Display the table
print(team_stats)

# Group by 'team_1' and calculate the total runs scored by 'team_2'
team1_team2_runs = crick_df.groupby('team_1')['team_2_runs'].sum()

# Convert the result to a DataFrame for better presentation
team1_team2_runs_df = pd.DataFrame(team1_team2_runs).reset_index()

# Rename the columns for clarity
team1_team2_runs_df.columns = ['Team 1', 'Total Runs Scored by Team 2']

# Display the table without the index
print(team1_team2_runs_df.to_string(index=False))



# Group by 'team_2' and calculate the total runs scored by 'team_1'
team2_team1_runs = crick_df.groupby('team_2')['team_1_runs'].sum()

# Convert the result to a DataFrame for better presentation
team2_team1_runs_df = pd.DataFrame(team2_team1_runs).reset_index()

# Rename the columns for clarity
team2_team1_runs_df.columns = ['Team 2', 'Total Runs Scored by Team 1']

# Display the table without the index
print(team2_team1_runs_df.to_string(index=False))



# Calculate total runs scored by team 2 against each team 1
team1_team2_runs = crick_df.groupby('team_1')['team_2_runs'].sum()
team1_team2_runs_df = pd.DataFrame(team1_team2_runs).reset_index()
team1_team2_runs_df.columns = ['Team 1', 'Total Runs Scored by Team 2']

# Calculate total runs scored by team 1 against each team 2
team2_team1_runs = crick_df.groupby('team_2')['team_1_runs'].sum()
team2_team1_runs_df = pd.DataFrame(team2_team1_runs).reset_index()
team2_team1_runs_df.columns = ['Team 2', 'Total Runs Scored by Team 1']

def calculate_bowling_average(team_name):
  """Calculates the bowling average for a given team."""
  total_runs_scored_by_team2 = team1_team2_runs_df.loc[
      team1_team2_runs_df['Team 1'] == team_name,
      'Total Runs Scored by Team 2'
  ].values[0] if team_name in team1_team2_runs_df['Team 1'].values else 0

  total_runs_scored_by_team1 = team2_team1_runs_df.loc[
      team2_team1_runs_df['Team 2'] == team_name,
      'Total Runs Scored by Team 1'
  ].values[0] if team_name in team2_team1_runs_df['Team 2'].values else 0

  team1_wickets = crick_df[crick_df['team_1'] == team_name]['team_1_wickets'].sum()
  team2_wickets = crick_df[crick_df['team_2'] == team_name]['team_2_wickets'].sum()

  total_runs_conceded = total_runs_scored_by_team2 + total_runs_scored_by_team1
  total_wickets_taken = team1_wickets + team2_wickets

  if total_wickets_taken == 0:
    bowling_average = float('inf') 
  else:
    bowling_average = total_runs_conceded / total_wickets_taken

  return bowling_average

# Calculate and print bowling averages for all teams
for team in crick_df['team_1'].unique():
  avg = calculate_bowling_average(team)
  print(f"Bowling Average for {team}: {avg}")







# Create a list to store team and average data
team_averages = []

# Calculate and store averages for all teams
for team in crick_df['team_1'].unique():
  avg = calculate_bowling_average(team)
  team_averages.append([team, avg])

# Create a DataFrame from the list
bowling_averages_df = pd.DataFrame(team_averages, columns=['Team', 'Bowling Average'])

# Display the table
print(bowling_averages_df.to_string(index=False))






# Sort the DataFrame by 'Bowling Average' in descending order
bowling_averages_df = bowling_averages_df.sort_values(by=['Bowling Average'], ascending=False)

# Plot the horizontal bar chart
plt.barh(bowling_averages_df['Team'], bowling_averages_df['Bowling Average'])
plt.xlabel('Bowling Average')
plt.ylabel('Team')
plt.title('Bowling Averages by Team')
plt.gca().invert_yaxis()  # Invert the y-axis to place highest values at the top
plt.show()