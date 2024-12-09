import pandas as pd
import re

# Load datasets
datasets = [
    pd.read_csv(f"WorldCup_Stats/{year}_Match_Stats.csv") for year in 
    [1975, 1979, 1983, 1987, 1992, 1996, 1999, 2003, 2007, 2011, 2015, 2019, 2023]
]
crick_df = pd.concat(datasets, axis=0)

# Initial cleanup: Drop fully empty rows and duplicates across all columns
crick_df = crick_df.dropna(axis=0, how='all')  # Drop fully empty rows
crick_df = crick_df.fillna('NA')  # Replace missing values with 'NA'

# Add match status
crick_df.loc[crick_df['result'] == 'No result', 'match_status'] = 'abandoned'
crick_df.loc[crick_df['result'] != 'No result', 'match_status'] = 'played'

# Extract winning team
def extract_winning_team(result_sentence):
    match = re.match(r"(\w+|\w+\s\w+)\swon", result_sentence)
    return match.group(1) if match else 'NA'

crick_df['winning_team'] = crick_df['result'].apply(extract_winning_team)

# Process best bowlers and batters
def process_best_bowlers(crick_df):
    crick_df['best_bowlers'] = crick_df['best_bowlers'].str.replace(r"[\[\]']", "", regex=True).str.strip()
    crick_df[['bowler_one_data', 'bowler_two_data']] = crick_df['best_bowlers'].str.split(', ', expand=True)

    crick_df['bowler_one'] = crick_df['bowler_one_data'].str.split(' - ').str[0].str.strip().fillna('NA')
    crick_df['bowler_one_wicket'] = (
        crick_df['bowler_one_data']
        .str.split(' - ').str[1]
        .str.replace(r"[^\d]", "", regex=True)
        .fillna(0)
        .astype(int)
    )
    crick_df['bowler_two'] = crick_df['bowler_two_data'].str.split(' - ').str[0].str.strip().fillna('NA')
    crick_df['bowler_two_wicket'] = (
        crick_df['bowler_two_data']
        .str.split(' - ').str[1]
        .str.replace(r"[^\d]", "", regex=True)
        .fillna(0)
        .astype(int)
    )
    crick_df = crick_df.drop(columns=['bowler_one_data', 'bowler_two_data'])  # Drop intermediate columns
    return crick_df

def process_best_batters(crick_df):
    crick_df['best_batters'] = crick_df['best_batters'].str.replace(r"[\[\]']", "", regex=True).str.strip()
    crick_df[['batter_one_data', 'batter_two_data']] = crick_df['best_batters'].str.split(', ', expand=True)

    crick_df['batter_one'] = crick_df['batter_one_data'].str.split(' - ').str[0].str.strip().fillna('NA')
    crick_df['batter_one_score'] = (
        crick_df['batter_one_data']
        .str.split(' - ').str[1]
        .str.replace(r"[^\d]", "", regex=True)
        .fillna(0)
        .astype(int)
    )
    crick_df['batter_two'] = crick_df['batter_two_data'].str.split(' - ').str[0].str.strip().fillna('NA')
    crick_df['batter_two_score'] = (
        crick_df['batter_two_data']
        .str.split(' - ').str[1]
        .str.replace(r"[^\d]", "", regex=True)
        .fillna(0)
        .astype(int)
    )
    crick_df = crick_df.drop(columns=['batter_one_data', 'batter_two_data'])  # Drop intermediate columns
    return crick_df

# Apply processing functions
crick_df = process_best_bowlers(crick_df)
crick_df = process_best_batters(crick_df)

# Check and print column names for deduplication
print("Columns in the DataFrame: ", crick_df.columns)

# Remove duplicates based on specific columns, keeping the first occurrence
# Use 'team_1' and 'team_2' for teams, 'date' for match date
crick_df = crick_df.drop_duplicates(subset=['team_1', 'team_2', 'date'], keep='first')  # Keep the first occurrence

# Clean and normalize text (e.g., stripping spaces)
crick_df = crick_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Drop any unnamed columns generated from merging
crick_df = crick_df.loc[:, ~crick_df.columns.str.contains('^Unnamed')]

# Final column cleanup (remove unwanted columns)
crick_df = crick_df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0', 'commentary_line', 'best_batters', 'best_bowlers', 'result'], errors='ignore')

# Save the cleaned data
output_file_path = "cleaned_data.csv"
crick_df.to_csv(output_file_path, index=False)

print(f"Cleaned data saved to {output_file_path}")


# Load the cleaned data
input_file_path = "cleaned_data.csv"
crick_df = pd.read_csv(input_file_path)

# Define the teams to filter out
teams_to_remove = ["Australia", "Pakistan", "India", "Bangladesh"]

# Remove rows where team_1 column contains these teams
crick_df = crick_df[~crick_df['team_1'].isin(teams_to_remove)]

# Save the updated dataset
output_file_path = "filtered_data.csv"
crick_df.to_csv(output_file_path, index=False)

print(f"Filtered data saved to {output_file_path}")



