import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from pygments.lexers import go

dash.register_page(__name__, path='/linechart', name="Line Chart 📈")

####################### LOAD DATASET #############################
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)

####################### COUNTRY DROPDOWN #########################
country_dropdown = dcc.Dropdown(
    id="line_country_filter",
    options=[{"label": country, "value": country} for country in sorted(pd.concat([df["team_1"], df["team_2"]]).unique())],
    placeholder="Select Country",
    value=None,
    clearable=False
)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.P("Select Country:"),
    country_dropdown,
    html.Br(),
    html.Div([
        html.H4("Total Runs Over the Years"),
        dcc.Graph(id="runs_chart")
    ]),
    html.Div([
        html.H4("Total Wickets Over the Years"),
        dcc.Graph(id="wickets_chart")
    ])
])

####################### CALLBACKS ###############################
@callback(
    [Output("runs_chart", "figure"), Output("wickets_chart", "figure")],
    [Input("line_country_filter", "value")]
)
def update_charts(selected_country):
    if not selected_country:
        return go.Figure(), go.Figure()

    # Filter data for the selected country
    df_country = df[
        (df["team_1"] == selected_country) | (df["team_2"] == selected_country)
    ]

    # Calculate total runs and wickets for each year
    df_country["total_runs"] = df_country.apply(
        lambda row: row["team_1_runs"] if row["team_1"] == selected_country else row["team_2_runs"], axis=1
    )
    df_country["total_wickets"] = df_country.apply(
        lambda row: row["team_1_wickets"] if row["team_1"] == selected_country else row["team_2_wickets"], axis=1
    )

    # Group by year and calculate totals
    df_aggregated = df_country.groupby("world_cup_year").agg({
        "total_runs": "sum",
        "total_wickets": "sum"
    }).reset_index()

    # Create separate charts for runs and wickets
    runs_fig = px.line(
        df_aggregated,
        x="world_cup_year",
        y="total_runs",
        title=f"Total Runs by {selected_country} Over the Years",
        markers=True,
        labels={"world_cup_year": "World Cup Year", "total_runs": "Total Runs"}
    )
    runs_fig.update_layout(template="plotly_white")

    wickets_fig = px.line(
        df_aggregated,
        x="world_cup_year",
        y="total_wickets",
        title=f"Total Wickets by {selected_country} Over the Years",
        markers=True,
        labels={"world_cup_year": "World Cup Year", "total_wickets": "Total Wickets"}
    )
    wickets_fig.update_layout(template="plotly_white")

    return runs_fig, wickets_fig
