#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:06:49 2020

@author: doguctan
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


df=pd.read_csv('mpg.csv')

app=dash.Dash()

features=df.columns

app.layout=html.Div([
                html.Div([
                    dcc.Dropdown(id='xaxis',
                                 options=[{'label':i,'value':i} for i in features],
                                 value='displacement')
                    ],style={'width':'48%','display':'inline-block'}),
                html.Div([
                    dcc.Dropdown(id='yaxis',
                                 options=[{'label':i,'value':i} for i in features],
                                 value='mpg')
                    ],style={'width':'48%','display':'inline-block'}),
                dcc.Graph(id='feature-graphic')

    
], style={'padding':10})


@app.callback(Output(component_id='feature-graphic', component_property='figure'),
              [Input('xaxis','value'),
               Input('yaxis','value')])
def update_graph(x_axis_name,y_axis_name):
    return{'data':[go.Scatter(x=df[x_axis_name],
                              y=df[y_axis_name],
                              text=df['name'],
                              mode='markers',
                              marker={'size':15,
                                      'opacity':0.5,
                                      'line':{'width':0.5,'color':'white'}})]
           
           
           ,'layout':go.Layout(title='My Dashboard for MPG',
                               xaxis={'title':x_axis_name},
                               yaxis={'title':y_axis_name},
                               hovermode='closest')
           }





if __name__=='__main__':
    app.run_server()
