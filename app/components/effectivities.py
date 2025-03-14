from dash import Dash, html
import pandas as pd
import os


df = pd.read_csv('../../data/csv/pokedex.csv', sep=',', )
print('Init...\n')
#print(os.path.abspath('../../data/csv/pokedex.csv'))
#print(df.shape, df.head(2))

app = Dash()

def generate_effectivity_plot(pkmn):
    active_mon = df[df['german_name'] == pkmn]
    return html.Div([
        html.H3(f"Name: {active_mon['german_name'].values[0]}"),
        html.P(f"Pokedex Nummer: {active_mon['pokedex_number'].values[0]}")
    ])


app.layout = html.Div([
    html.H2(children='A beautiful headline'),
    generate_effectivity_plot('Pikachu')
])

if __name__ == '__main__':
    app.run(debug=True)
