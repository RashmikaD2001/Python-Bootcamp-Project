import pandas as pd

url = "https://raw.githubusercontent.com/RashmikaD2001/Python-Bootcamp-Project/refs/heads/task_2/filtered_data.csv"
crick_df = pd.read_csv(url)




import matplotlib.pyplot as plt

# Filter data for matches where 'match_category' is 'Final'
final_matches = crick_df[crick_df['match_category'] == 'Final']

# Group by 'pom' and count the number of awards for each player in finals
pom_awards_in_finals = final_matches.groupby('pom')['pom'].count().sort_values(ascending=False)

# Create the bar chart
plt.figure(figsize=(12, 6))  # Adjust figure size as needed
plt.bar(pom_awards_in_finals.index, pom_awards_in_finals.values)
plt.title('Bar Chart of Player of the Match Awards in Finals')
plt.xlabel('Player')
plt.ylabel('Number of Awards')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
plt.tight_layout()
plt.show()
