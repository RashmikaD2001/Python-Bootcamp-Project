import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/RashmikaD2001/Python-Bootcamp-Project/refs/heads/main/cleaned_data.csv"
crick_df = pd.read_csv(url)

#!pip install plotly==5.15.0
import plotly.express as px

# Assuming 'crick_df' is your DataFrame
category_counts = crick_df['match_category'].value_counts()

fig = px.pie(
    values=category_counts.values, 
    names=category_counts.index, 
    title='Distribution of Match Categories'
)
fig.show()