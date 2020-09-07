# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:00:25 2020

@author: A16438
"""

#######
# Here we'll use the mpg.csv dataset to demonstrate
# how multiple inputs can affect the same graph.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

rankings = [1,2,3,4]

app.layout = html.Div([

        html.Div(
                [
                html.Div(id='blank',children='Ranking',                         
                         style={'width': '150px', 'display': 'inline-block','margin-right':0, 'float':'left'}
),                    
                #"Ranking :",
                html.Div(
                         [
                            dcc.Dropdown(
                            id='ranking',
                            options=[{'label': i, 'value': i} for i in rankings],
                            value='ranking_no')                                                          
                         ],
                         style={'width': '150px', 'display': 'inline-block','margin-left':0, 'float':'left'}

                         )
                ],
        style={'width': '100%', 'display': 'inline-block','margin-bottom':50, 'float':'top'}
        ),

        #html.Br(id='blank'),
        #html.Div(id='blank',style={'height':'5px'}),

        html.Div([
                    dcc.Input(id='rate', value='', type='text')
                 ],
                style={'width': '10%',  'display': 'inline-block','margin-top':50}
                ),

        html.Div(id='probability-result')
], style={'padding':10})

@app.callback(
    Output('probability-result', 'children'),
    [Input('ranking', 'value'),
     Input('rate', 'value')])
def update_graph(ranking, rate):
    return float(rate)*ranking
if __name__ == '__main__':
    app.run_server()




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 07:36:13 2020

@author: doguctan
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:00:25 2020

@author: A16438
"""

#######
# Here we'll use the mpg.csv dataset to demonstrate
# how multiple inputs can affect the same graph.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

rankings = [1,2,3,4]

app.layout = html.Div([

        html.Div(
                [
                html.Div(
                         [
                            html.Table([
                                html.Tr([
                                    html.Td(
                                            'Ranking :'
                                            ),
                                    html.Td(
                                            dcc.Dropdown(
                                            id='ranking',
                                            options=[{'label': i, 'value': i} for i in rankings],
                                            value='ranking_no')
                                            )
                                        ])
                                        ])                                                          
                         ],
                         style={'width': '50%', 'display': 'inline-block','margin-left':0, 'float':'left'}

                         )
                ],
        style={'width': '100%', 'display': 'inline-block','margin-bottom':50, 'float':'left'}
        ),

        #html.Br(id='blank'),
        #html.Div(id='blank',style={'height':'5px'}),

        html.Div([
                    dcc.Input(id='rate', value='', type='text')
                 ],
                style={'width': '10%',  'display': 'inline-block','margin-top':50}
                ),

        html.Div(id='probability-result')
], style={'padding':10})

@app.callback(
    Output('probability-result', 'children'),
    [Input('ranking', 'value'),
     Input('rate', 'value')])
def update_graph(ranking, rate):
    return float(rate)*ranking
if __name__ == '__main__':
    app.run_server()

