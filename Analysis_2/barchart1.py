import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
crick_df = pd.read_csv(url)

# Assuming your DataFrame is named 'df' and is already loaded

# Change data type of 'world_cup_year' to qualitative (categorical)
crick_df['world_cup_year'] = crick_df['world_cup_year'].astype('category')

# Group data by 'world_cup_year' and get the maximum 'team_1_runs' for each year
highest_runs_by_world_cup_year = crick_df.groupby('world_cup_year')['team_1_runs'].max().reset_index()

# Create the bar chart with exchanged axes and slightly increased bar width
plt.figure(figsize=(12, 6))  # Adjust figsize if needed for better label visibility

# Increased bar width slightly (from 0.8 to 0.9)
plt.barh(highest_runs_by_world_cup_year['world_cup_year'], highest_runs_by_world_cup_year['team_1_runs'], height=0.9)

plt.title('Highest Team 1 Runs Scored Each World Cup Year')
plt.ylabel('World Cup Year')  # Y-axis label is now 'World Cup Year'
plt.xlabel('Highest Runs')  # X-axis label is now 'Highest Runs'

# Set y-axis labels to their value positions
plt.yticks(highest_runs_by_world_cup_year['world_cup_year'], highest_runs_by_world_cup_year['world_cup_year'])

plt.tight_layout()
plt.show()