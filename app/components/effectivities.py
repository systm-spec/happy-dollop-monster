from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import os

df = pd.read_csv('../../data/csv/pokedex.csv', sep=',')
types_df = df[['pokedex_number',
               'german_name',
               'type_1',
               "type_2",
               'against_fire',
               'against_bug',
               'against_dark',
               'against_dragon',
               'against_electric',
               'against_fairy',
               'against_fight',
               'against_flying',
               'against_ghost',
               'against_grass',
               'against_ice',
               'against_ground',
               'against_normal',
               'against_poison',
               'against_psychic',
               'against_rock',
               'against_steel',
               'against_water']]

print('Init...\n')
# print(os.path.abspath('../../data/csv/pokedex.csv'))
# print(df.shape, df.head(2))

app = Dash()


def generate_effectivity_plot(pkmn):
    active_mon = types_df[types_df['german_name'] == pkmn]
    fig = px.imshow(active_mon[5:], zmin=0, zmax=4)
    return html.Div([
        html.H3(f"Name: {active_mon['german_name'].values[0]}"),
        html.P(f"Pokedex Nummer: {active_mon['pokedex_number'].values[0]}"),

        dcc.Graph(id='effectivity-content', figure=fig)
    ])


app.layout = html.Div([
    html.H2(children='A beautiful headline'),
    generate_effectivity_plot('Pikachu')
])

if __name__ == '__main__':
    app.run(debug=True)
