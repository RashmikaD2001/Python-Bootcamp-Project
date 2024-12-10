
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
crick_df = crick_df.fillna('NA')  # Replace missing values with 'NA


crick_df.info()

crick_df = crick_df.dropna(axis=0, how='all')
     

crick_df = crick_df.drop_duplicates(subset=['team_1', 'team_2', 'date'], keep='first')
     
crick_df['team_1'] = crick_df['team_1'].replace({'Australia': 'AUS', 'Pakistan' : 'PAK' , 'India' : 'IND', 'Bangladesh' : 'BAN' })
crick_df['team_2'] = crick_df['team_2'].replace({'West Indies': 'WI', 'Bangladesh' : 'BAN' ,'Sri Lanka' : 'SL' , 'New Zealand' : 'NZ'})
crick_df = crick_df.fillna('NA')
     

crick_df.loc[crick_df['result'] == 'No result', 'match_status'] = 'abandoned'
crick_df.loc[crick_df['result'] != 'No result', 'match_status'] = 'played'
     

import re

def extract_winning_team(result_sentence):
    match = re.match(r"(\w+|\w+\s\w+)\swon", result_sentence)
    if match:
        return match.group(1)
    return 'NA'

crick_df['winning_team'] = crick_df['result'].apply(extract_winning_team)
     

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

crick_df = crick_df.drop(columns=['bowler_one_data', 'bowler_two_data'])
     

crick_df['best_batters'] = crick_df['best_batters'].str.replace(r"[\[\]']", "", regex=True).str.strip()


# Split the data into two parts based on ', ' separator
crick_df[['batter_one_data', 'batter_two_data']] = crick_df['best_batters'].str.split(', ', expand=True)

# Extract and clean batter names and scores for the first batter
crick_df['batter_one'] = crick_df['batter_one_data'].str.split(' - ').str[0].str.strip().fillna('NA')
crick_df['batter_one_score'] = (
    crick_df['batter_one_data']
    .str.split(' - ').str[1]  # Extract the score portion
    .str.replace(r"[^\d]", "", regex=True)  # Remove non-digit characters
    .fillna(0)
    .astype(int)  # Convert to integer
)

# Extract and clean batter names and scores for the second batter
crick_df['batter_two'] = crick_df['batter_two_data'].str.split(' - ').str[0].str.strip().fillna('NA')
crick_df['batter_two_score'] = (
    crick_df['batter_two_data']
    .str.split(' - ').str[1]  # Extract the score portion
    .str.replace(r"[^\d]", "", regex=True)  # Remove non-digit characters
    .fillna(0)
    .astype(int)  # Convert to integer
)

# Drop intermediate columns if not needed
crick_df = crick_df.drop(columns=['batter_one_data', 'batter_two_data'])
     

crick_df = crick_df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0', 'commentary_line', 'best_batters', 'best_bowlers', 'result'])

output_file_path = "cleaned_data.csv"
crick_df.to_csv(output_file_path, index=False)

print(f"Cleaned data saved to {output_file_path}")