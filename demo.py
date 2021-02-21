from os import getcwd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json

with open('column_names.json') as json_file:
    column_names = json.load(json_file)

filepath = getcwd() + "/data/2021-01-27_12.33.32-17.12.41.csv"

df = pd.read_csv(filepath, sep="\t", parse_dates=True).drop(['Date'], axis='columns')

df = df.rename(columns = column_names)

df_new = df.melt(id_vars=['timestamp'],value_vars=df.columns[1:])

fig = px.line(df_new,x="timestamp",y="value", color="variable")
fig.show()