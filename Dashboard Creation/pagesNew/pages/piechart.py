import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/piechart', name="PIECHART 📊")


####################### LOAD DATASET #############################
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)

####################### PIECHARTS ###############################

def create_distribution(col_name= "host_country"):
    # Group data by the specified column and count occurrences
    grouped_data = df.groupby(col_name).size().reset_index(name='count') 
    
    # Create a pie chart using Plotly Express
    fig = px.pie(grouped_data, values='count', names=col_name, title=f'Distribution of {col_name}')  
    
    return fig

####################### WIDGETS ################################
columns = [ "match_status","winning_team", "match_category", "host_country"]
dd = dcc.Dropdown(id="dist_column", options=columns, value="world_cup_year", clearable=False)


####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.P("Select Column:"),
    dd,
    dcc.Graph(id="piechart")
   
])

####################### CALLBACKS ################################
@callback(Output("piechart", "figure"), [Input("dist_column", "value"), ])
def update_pie(dist_column):
    return create_distribution(dist_column)