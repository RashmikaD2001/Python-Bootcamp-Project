import pandas as pd

url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
crick_df = pd.read_csv(url)



import matplotlib.pyplot as plt

# Filter data for matches where 'match_category' is 'Final'
final_matches = crick_df[crick_df['match_category'] == 'Final']

# Group by 'winning_team' and count the number of wins for each team in finals
final_wins = final_matches.groupby('winning_team')['winning_team'].count().sort_values(ascending=False)

# Create the histogram
plt.figure(figsize=(12, 6))
plt.hist(final_wins.index, weights=final_wins.values, bins=len(final_wins), edgecolor='black')
plt.title('Histogram of Wins in Finals by Team')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


