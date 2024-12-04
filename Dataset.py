import pandas as pd

dataset1 = pd.read_csv('WorldCup_Stats/1975_Match_Stats.csv')
dataset2 = pd.read_csv('WorldCup_Stats/1979_Match_Stats.csv')
dataset3 = pd.read_csv('WorldCup_Stats/1983_Match_Stats.csv')
dataset4 = pd.read_csv('WorldCup_Stats/1987_Match_Stats.csv')
dataset5 = pd.read_csv('WorldCup_Stats/1992_Match_Stats.csv')
dataset6 = pd.read_csv('WorldCup_Stats/1996_Match_Stats.csv')
dataset7 = pd.read_csv('WorldCup_Stats/1999_Match_Stats.csv')
dataset8 = pd.read_csv('WorldCup_Stats/2003_Match_Stats.csv')
dataset9 = pd.read_csv('WorldCup_Stats/2007_Match_Stats.csv')
dataset10 = pd.read_csv('WorldCup_Stats/2011_Match_Stats.csv')
dataset11 = pd.read_csv('WorldCup_Stats/2015_Match_Stats.csv')
dataset12 = pd.read_csv('WorldCup_Stats/2019_Match_Stats.csv')
dataset13 = pd.read_csv('WorldCup_Stats/2023_Match_Stats.csv')

crick_df = pd.concat([dataset1, dataset2, dataset3, dataset4,dataset5,dataset6,dataset7,dataset8,dataset9, dataset10, dataset11, dataset12, dataset13], axis=0)

crick_df.info()

crick_df = crick_df.dropna(axis=0, how='all')
     

crick_df = crick_df.drop_duplicates(keep=False)
     

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