import pandas as pd
import matplotlib.pyplot as plt

# Read the new CSV file into a Pandas DataFrame
url = "https://raw.githubusercontent.com/RashmikaD2001/Python-Bootcamp-Project/refs/heads/main/cleaned_data.csv"
crick_df = pd.read_csv(url)



# Plotting the histogram for 'team_2_runs'
plt.figure(figsize=(8, 6))  # Adjust figure size if needed

# Convert 'team_2_runs' to numeric, coercing errors to NaN
crick_df['team_2_runs'] = pd.to_numeric(crick_df['team_2_runs'], errors='coerce')

# Filter out rows with NaN values in 'team_2_runs'
crick_df_filtered = crick_df.dropna(subset=['team_2_runs'])

# Specify the column for the histogram
column_name2 = 'team_2_runs'

# Plot the histogram using crick_df_filtered
plt.hist(crick_df_filtered[column_name2], bins=20, color='blue', edgecolor='black')
plt.title(f'Histogram of the total runs scored by Team 2 in their innings')
plt.xlabel(column_name2)
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()