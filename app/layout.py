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
        html.Div(className='flex-col', children=[

            html.Div(id='header',className='panel flex', children=[
                html.Img(src='/assets/img/pika_tile.png'),
                html.H1('Pokemon Dashboard')
            ]),

            html.Div(id='search-bar', className='panel flex-col', children=[
                html.H2('Search Your Pokemon'),
                html.Div(className='', children=[
                    html.Button(className='', children='Search',id="search-btn"),
                    dcc.Input(
                        value='',
                        id="search-input",
                        type="search",
                        placeholder="Suchbegriff eingeben...",
                        debounce=True,  # Verhindert zu viele Updates bei jedem Tastenanschlag
                        style={"width": "300px", "padding": "10px", "fontSize": "16px"}
                    ),
                ])

            ]),
            html.Div(id='pokemon-panel-one', className='panel flex', children=[
                html.Div(className="thumbnail_pokemon", children=[
                    html.Img(src='assets/img/Icons/gen_1/025-Pikachu.72.png')
                ]),

                html.Div(className='', children=[
                    html.H2('Pikachu'),
                    html.P('Mouse Pokemon'),

                ])

            ])

        ])
    ])
]

# Run
if __name__ == '__main__':
    app.run(debug=True)