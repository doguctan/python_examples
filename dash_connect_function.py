#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:53:37 2020

@author: doguctan
"""


import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input,Output

app=dash.Dash()

app.layout=html.Div([
            dcc.Input(id='my-id', value='Initial Text', type='text'),
            html.Div(id='my-div',style={'border':'2px blue solid'})
])


@app.callback(Output(component_id='my-div',component_property='children'),
              [Input(component_id='my-id',component_property='value')])
def update_output_div(input_value):
    return "You entered : {}".format(input_value)


if __name__=='__main__':
    app.run_server()

#-------------------------

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 20:58:40 2020

@author: doguctan
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


df=pd.read_csv('gapminderDataFiveYear.csv')

app=dash.Dash()

year_options=[{'label':str(year),'value':year} for year in df['year'].unique()]



app.layout=html.Div([
                dcc.Graph(id='graph'),
                dcc.Dropdown(id='year_picker', options=year_options,
                             value=df['year'].min())
    
])

@app.callback(Output(component_id='graph',component_property='figure'),
              [Input(component_id='year_picker',component_property='value')])
def update_figure(selected_year):
    
    
    #DATA ONLY FOR SELECTED YEAR FROM DROPDOWN
    filtered_df=df[df['year']==selected_year]
    traces=[]
    
    for continent_name in filtered_df['continent'].unique():
        df_by_continent=filtered_df[filtered_df['continent']==continent_name]
        traces.append(go.Scatter(
                    x=df_by_continent['gdpPercap'],
                    y=df_by_continent['lifeExp'],
                    mode='markers',
                    opacity=0.7,
                    marker={'size':15},
                    name=continent_name
            
            ))
    
    
    return {'data':traces, 
            'layout':go.Layout(title='My Plot',
                               xaxis={'title':'GDP Per Cap','type':'log'},
                               yaxis={'title':'Life Expectancy'})}

if __name__=='__main__':
    app.run_server()

#-------------------------------------
