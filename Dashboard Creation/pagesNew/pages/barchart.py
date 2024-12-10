import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

# Initialize Dash app (only for this page)
app = dash.Dash(__name__)

# Register the page (this needs to be done after app instantiation)
dash.register_page(__name__, path="/barchart", name="Matches Bar Chart")

# Load the dataset
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)

# Define the layout for the bar chart page
layout = html.Div([
    html.H2("Matches Bar Chart", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in sorted(df['world_cup_year'].unique())],
        placeholder="Select a World Cup Year",
        multi=True,
    ),
    dcc.Graph(id='matches-bar-chart')
])


# Define the callback for updating the bar chart
@callback(
    Output('matches-bar-chart', 'figure'),
    Input('year-dropdown', 'value')
)
def update_bar_chart(selected_years):
    filtered_df = df
    if selected_years:
        filtered_df = filtered_df[filtered_df['world_cup_year'].isin(selected_years)]

    matches_bar_chart = px.bar(
        filtered_df.groupby('world_cup_year').size().reset_index(name='matches'),
        x='world_cup_year', y='matches',
        title="Number of Matches Played by Year",
        labels={'world_cup_year': 'World Cup Year', 'matches': 'Number of Matches'},
        color='world_cup_year'
    )
    return matches_bar_chart


# Run the app (only for this script page)
if __name__ == '__main__':
    app.run_server(debug=True)
