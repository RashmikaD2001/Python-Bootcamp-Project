import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

# Register the page for line chart
dash.register_page(__name__, path="/linechart02", name="Multiple Lines in one Chart📈")

# Load the dataset
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)

# Get unique countries
countries = df['team_1'].unique()

# Function to get scores for a country
def get_country_scores(country_name):
    batting_first = df[(df['team_1'] == country_name)]['team_1_runs'].groupby(df['world_cup_year']).sum().reset_index()
    batting_second = df[(df['team_2'] == country_name)]['team_2_runs'].groupby(df['world_cup_year']).sum().reset_index()
    
    batting_first['scenario'] = 'Batting First'
    batting_second['scenario'] = 'Batting Second'
    
    # Concatenate the data for both scenarios
    yearly_scores = pd.concat([batting_first, batting_second], ignore_index=True)
    yearly_scores['country'] = country_name
    
    return yearly_scores

# Get scores for each country
country_scores = {country: get_country_scores(country) for country in countries}

# Define the layout for the line chart page
layout = html.Div([
    html.H2("Line Chart: Runs for Each Team Over Time (Batting First vs. Batting Second)", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value=countries[0],  # Default to the first country
        multi=False,
    ),
    dcc.Graph(id='line-chart')
])

# Define the callback for updating the line chart
@callback(
    Output('line-chart', 'figure'),
    Input('country-dropdown', 'value')
)
def update_line_chart(selected_country):
    if not selected_country:
        return {}

    yearly_scores = country_scores[selected_country]
    
    # Create a line chart with two lines for 'Batting First' and 'Batting Second'
    fig = px.line(
        yearly_scores, 
        x='world_cup_year', 
        y=['team_1_runs', 'team_2_runs'],  # Use both runs columns for 'Batting First' and 'Batting Second'
        color='scenario',  # Color by scenario
        title=f"Runs for {selected_country} Over Time (Batting First vs. Batting Second)",
        labels={'world_cup_year': 'World Cup Year', 'value': 'Total Runs'}
    )
    
    return fig
