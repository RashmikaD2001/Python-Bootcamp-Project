import pandas as pd
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px

# Register the page
dash.register_page(__name__, path="/map", name="World Cup Host Countries 🌍")

# Load the dataset
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)

# Map "England" to "United Kingdom" and other potential mismatches
country_name_mapping = {
    "England": "United Kingdom",
    # Add other mappings here if needed
}
df['host_country'] = df['host_country'].replace(country_name_mapping)

# Preprocess the data
df_host_countries = df[['world_cup_year', 'host_country']].drop_duplicates()

# Group by host_country and aggregate years into a single string
host_country_data = (
    df_host_countries
    .groupby('host_country')
    .agg(
        occurrences=('world_cup_year', 'size'),
        years=('world_cup_year', lambda x: ', '.join(sorted(x.astype(str))))
    )
    .reset_index()
)

# Define the layout for the map page
layout = html.Div([
    html.H2("World Cup Host Countries (1975-2023)", style={'textAlign': 'center'}),
    dcc.Graph(id='world-map')
])

# Define the callback for updating the map
@callback(
    Output('world-map', 'figure'),
    Input('world-map', 'id')  # Dummy input to trigger map generation
)
def display_host_countries(_):
    # Create the choropleth map
    fig = px.choropleth(
        host_country_data,
        locations='host_country',
        locationmode='country names',
        color='occurrences',
        hover_name='host_country',
        hover_data={'occurrences': False, 'years': True},
        title='World Cup Host Countries (1975-2023)',
        color_continuous_scale='Viridis',
    )
    fig.update_geos(
        showcountries=True,
        projection_type='natural earth'
    )
    fig.update_layout(
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial")
    )
    return fig
