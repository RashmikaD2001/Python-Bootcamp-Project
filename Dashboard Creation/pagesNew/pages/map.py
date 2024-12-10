import pandas as pd
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px

dash.register_page(__name__, path="/heatmap", name="Heatmap Analysis 🔥")

# Load the dataset
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)

# Preprocess the data
# Create a unified column for teams to simplify grouping
df_teams = pd.melt(
    df, 
    id_vars=['world_cup_year'], 
    value_vars=['team_1', 'team_2'], 
    var_name='team_type', 
    value_name='team'
)

# Aggregate data by year and team
df_grouped = df_teams.groupby(['world_cup_year', 'team']).size().reset_index(name='matches_played')

# Define layout
layout = html.Div([
    html.H2("Heatmap of Matches Played by Teams in World Cups", style={'textAlign': 'center'}),
    dcc.Graph(id='heatmap', style={'height': '75vh'}),
])

@callback(
    Output('heatmap', 'figure'),
    Input('heatmap', 'id')  # Trigger on page load
)
def generate_heatmap(_):
    # Pivot table to create heatmap data
    heatmap_data = df_grouped.pivot(index='team', columns='world_cup_year', values='matches_played').fillna(0)

    # Generate heatmap using Plotly Express
    fig = px.imshow(
        heatmap_data,
        labels=dict(x="World Cup Year", y="Team", color="Matches Played"),
        x=heatmap_data.columns,
        y=heatmap_data.index,
        color_continuous_scale='Viridis'
    )
    fig.update_layout(title="Heatmap of Matches Played by Teams in World Cups")
    return fig
