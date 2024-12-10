import pandas as pd
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px

dash.register_page(__name__, path='/bubblechart', name="Bubble Chart 🎈")

####################### LOAD DATASET #############################
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)


####################### BUBBLE CHART FUNCTION #####################
def create_bubble_chart(year=None):
    # Filter data for a specific year if provided
    if year:
        filtered_df = df[df["world_cup_year"] == year]
    else:
        filtered_df = df

    # Count Player of the Match awards
    pom_counts = filtered_df.groupby(["pom", "world_cup_year"]).size().reset_index(name="count")

    # Aggregate total runs scored by players
    player_runs = filtered_df.groupby("pom")["batter_one_score"].sum().reset_index(name="total_runs")

    # Merge data
    merged_df = pd.merge(pom_counts, player_runs, on="pom", how="left")

    # Create bubble chart
    fig = px.scatter(
        merged_df,
        x="world_cup_year",
        y="count",
        size="total_runs",
        color="pom",
        hover_name="pom",
        title="Player of the Match Analysis by Year",
        labels={"count": "Player of the Match Awards", "total_runs": "Total Runs"},
        height=600
    )

    # Update layout to fix y-axis range
    fig.update_layout(
        xaxis_title="World Cup Year",
        yaxis_title="Player of the Match Awards",
        yaxis=dict(range=[0, merged_df["count"].max() + 1])  # Set y-axis range to start from 0
    )

    return fig


####################### WIDGETS #############################
year_dropdown = dcc.Dropdown(
    id="bubble_year",
    options=[{"label": year, "value": year} for year in sorted(df["world_cup_year"].unique())],
    value=None,
    placeholder="Select a World Cup Year",
    clearable=True
)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.P("Select Year:"),
    year_dropdown,
    dcc.Graph(id="bubble_chart")
])


####################### CALLBACK #############################
@callback(Output("bubble_chart", "figure"), [Input("bubble_year", "value")])
def update_bubble_chart(year):
    return create_bubble_chart(year)
