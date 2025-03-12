# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('../data/csv/pokedex.csv')


# Init App
app = Dash()

farbe = {
    'background':'#38324e',
    'panel':'#403a60',
    'ac_pink':"#e34e8d",
    'ac_cyan':"#45c7f0",
    'ac_green':"#26cba9",
}

# App layout
app.layout = [
    html.Div(children=[

        html.Div(className='panel', children=[
            html.H1('Pokemon Dashboard')
        ])
    ], className='flex')
]

# Run
if __name__ == '__main__':
    app.run(debug=True)