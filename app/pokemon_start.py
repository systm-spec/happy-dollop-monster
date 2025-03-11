

import pandas as pd
import plotly.express as px
import streamlit as st

# Dataframe laden:
pokemon = pd.read_csv('pokemon.csv')
pokemon = pokemon.dropna()
# Spalten für x-Achse:
categorical_cols = ['name', 'pokedex_number']
# Spalten für y-Achse:
numerical_cols = ['attack',
       'base_egg_steps','base_happiness', 'base_total', 'defense']
col2 = pokemon.columns


st.set_page_config(page_title='Pokemon')

st.title('Pokemon-App!')

# Bündelt verschiedene grafische Elemente zu einem zusammenhängenden Formular
# Nutzerangaben können übergeben und dann per Knopfdruck alle verarbeitet werden
with st.form('analysis_form'):
    col1, col2 = st.columns(2)

    # Leitet ein, was in Spalte 1 erscheint:
    with col1:
        # Selectbox erstellt einen Dropdown mit auswählbaren Werten:
        cat_selection = st.selectbox('Welche Kategorie interessiert dich?',
                                     categorical_cols)
    with col2:
        # Radio buttons mit anklickbaren Werten:
        target_selection = st.radio('Von was willst du die Mittelwerte sehen?',
                                    numerical_cols)

    # Übermittlungsknopf hinzufügen (ohne Knopf nicht sinnvoll):
    st.form_submit_button('Diagramm erstellen', type='primary')

# Säulendiagramm dynamisch generieren:
scores_by_pokemon= (pokemon.groupby(cat_selection)
                        [target_selection]
                        .mean()
                        .sort_values(ascending=False))

scores_pokemon_barchart = px.bar(
    scores_by_pokemon,
    scores_by_pokemon.index,
    target_selection,
)

st.plotly_chart(scores_pokemon_barchart)

# Expander, um Dataframe ein- und auszublenden:
with st.expander('Daten anschauen', expanded=False):
    st.dataframe(pokemon)