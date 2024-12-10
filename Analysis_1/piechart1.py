import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/RashmikaD2001/Python-Bootcamp-Project/refs/heads/main/cleaned_data.csv"
crick_df = pd.read_csv(url)

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Calculate win counts for each team
team_wins = crick_df['winning_team'].value_counts()

# Filter out 'NA' for no result or tie
team_wins = team_wins[team_wins.index != 'NA']

# Calculate winning percentages
winning_percentages = (team_wins / team_wins.sum()) * 100

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts = ax.pie(winning_percentages,
                       startangle=90,
                       textprops={'color': 'w'},
                       wedgeprops={'linewidth': 1, 'edgecolor': 'black'})

# Create color list with percentages
color_list = []
for i, wedge in enumerate(wedges):
    color = wedge.get_facecolor()
    team = winning_percentages.index[i]
    percentage = winning_percentages.iloc[i]
    color_list.append([color, team, percentage])

# Create a separate plot for the color list
fig_list, ax_list = plt.subplots(figsize=(3, 5))  # Adjust size as needed
ax_list.axis('off')  # Hide axes

# Add color boxes and text to the color list plot
for i, (color, team, percentage) in enumerate(color_list):
    rect = mpatches.Rectangle((0, 0.9 - i * 0.1),
                              0.2,
                              0.1,
                              facecolor=color,
                              edgecolor='black')
    ax_list.add_patch(rect)
    ax_list.text(0.25,
                 0.9 - i * 0.1 + 0.05,
                 f"{team} ({percentage:.1f}%)",
                 va='center')

# Set title for the color