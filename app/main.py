# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('../data/csv/pokedex.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Pokemon Dashboard'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.pie(df, names='generation', values='pokedex_number'))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)