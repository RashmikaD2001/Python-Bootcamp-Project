import pandas as pd
import matplotlib.pyplot as plt

# Load the data
url = "https://raw.githubusercontent.com/RashmikaD2001/Python-Bootcamp-Project/refs/heads/task_2/filtered_data.csv"

crick_df = pd.read_csv(url)

# Filter for finals
final_matches = crick_df[crick_df['match_category'] == 'Final']

# Group by 'winning_team' and count wins
final_wins = final_matches.groupby('winning_team')['winning_team'].count().sort_values(ascending=False)

# Create the horizontal bar chart using plt.barh()
plt.figure(figsize=(12, 6))  # Adjust figsize if needed
plt.barh(final_wins.index, final_wins.values, edgecolor='black')  

plt.title('Horizontal Bar Chart of Wins in Finals by Team')
plt.ylabel('Team')  # ylabel is now 'Team'
plt.xlabel('Number of Wins')  # xlabel is now 'Number of Wins'

plt.tight_layout()
plt.show()