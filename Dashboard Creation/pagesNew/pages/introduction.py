import dash
from dash import html

dash.register_page(__name__, path='/', name="Introduction 😃")


####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("ICC Men’s Cricket World Cup - A Journey Through History"),
        "This case study is about analysing all the ICC Men’s Cricket World Cup matches held from 1975-2023.",
        html.Br(),html.Br(),
        " For the analysis and visualization, you will be provided a folder “WorldCup_Stats” which contains  csv files each corresponding to a World Cup series.",
        ]),
          html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        "Number of Instances: 528",html.Br(),
        "Number of Attributes: 22 ",

        html.Br(),html.Br(),
        html.B("- date"),
        html.Br(),
        html.B("- venue"),
        html.Br(),
        html.B("- match_category"),
        html.Br(),
        html.B("- team_1"),
        html.Br(),
        html.B("- team_2"),
        html.Br(),
        html.B("- team_1_runs"),
        html.Br(),
        html.B("- team_1_wickets"),
        html.Br(),
        html.B("- team_2_runs"),
        html.Br(),
        html.B("- team_2_wickets"),
        html.Br(),
        html.B("- pom(player of the match)"),
        html.Br(),
        html.B("- world_cup_year"),
        html.Br(),
        html.B("- host_country"),
        html.Br(),
        html.B("- match_status"),
        html.Br(),
        html.B("-winning_team"),
        html.Br(),
        html.B("-bowler_one"),
        html.Br(),
        html.B("-bowler_one_wicket"),
        html.Br(),
        html.B("-bowler_two"),
        html.Br(),
        html.B("-bowler_two_wicket"),
        html.Br(),
        html.B("-batter_one"),
        html.Br(),
        html.B("-batter_one_score"),
        html.Br(),
        html.B("-batter_two"),
        html.Br(),
        html.B("-batter_two_score"),
        ])

], className="p-4 m-2", style={"background-color": "#e3f2fd"})
