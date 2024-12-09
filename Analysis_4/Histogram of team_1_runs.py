import pandas as pd
import matplotlib.pyplot as plt
# Read the new CSV file into a Pandas DataFrame
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
crick_df = pd.read_csv(url)

# Convert 'team_1_runs' and 'team_2_runs' to numeric, handling errors
crick_df['team_1_runs'] = pd.to_numeric(crick_df['team_1_runs'], errors='coerce')
crick_df['team_2_runs'] = pd.to_numeric(crick_df['team_2_runs'], errors='coerce')

# Filter out rows with NaN values in 'team_1_runs' or 'team_2_runs'
crick_df_filtered = crick_df.dropna(subset=['team_1_runs', 'team_2_runs'])


# Specify the column for the histogram
column_name = 'team_1_runs'  # Replace with desired column name

# Plot the histogram
plt.figure(figsize=(8, 6))  # Adjust figure size if needed
plt.hist(crick_df_filtered[column_name], bins=20, color='blue', edgecolor='black')
plt.title(f'Histogram of {column_name}')
plt.xlabel(column_name)
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()