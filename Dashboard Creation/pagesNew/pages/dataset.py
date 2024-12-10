import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path='/dataset', name="Dataset 📋")

####################### LOAD DATASET #############################
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)


####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(data=df.to_dict('records'),
                         page_size=20,
                         style_cell={"background-color": "lightgrey", "border": "solid 1px white", "color": "black", "font-size": "11px", "text-align": "left"},
                         style_header={"background-color": "dodgerblue", "font-weight": "bold", "color": "white", "padding": "10px", "font-size": "18px"},
                        ),
])