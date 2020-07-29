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

