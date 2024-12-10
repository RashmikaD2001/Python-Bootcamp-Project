import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/RashmikaD2001/Python-Bootcamp-Project/refs/heads/main/cleaned_data.csv"
crick_df = pd.read_csv(url)



# Group by 'team_1' and calculate total runs and average
team_stats = crick_df.groupby('team_1')['team_1_runs'].agg(['sum', 'mean'])

# Rename columns for better clarity
team_stats = team_stats.rename(columns={'sum': 'Total Runs', 'mean': 'Average'})

# Display the table
print(team_stats)

# --- Average runs for team_1 ---
team_1_avg_runs = crick_df.groupby('team_1')['team_1_runs'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))  # Adjust figure size if needed
plt.bar(team_1_avg_runs.index, team_1_avg_runs.values)
plt.xlabel('Team 1')
plt.ylabel('Average Runs')
plt.title('Average Runs for Team 1')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



# Group by 'team_2' and calculate total runs and average
team_stats = crick_df.groupby('team_2')['team_2_runs'].agg(['sum', 'mean'])

# Rename columns for better clarity
team_stats = team_stats.rename(columns={'sum': 'Total Runs', 'mean': 'Average'})

# Display the table
print(team_stats)

import matplotlib.pyplot as plt
import pandas as pd



# --- Average runs for team_2 ---
team_2_avg_runs = crick_df.groupby('team_2')['team_2_runs'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))  # Adjust figure size if needed
plt.bar(team_2_avg_runs.index, team_2_avg_runs.values)
plt.xlabel('Team 2')
plt.ylabel('Average Runs')
plt.title('Average Runs for Team 2')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()