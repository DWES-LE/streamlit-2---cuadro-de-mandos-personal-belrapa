import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
import plotly as pl

data = pd.read_csv('conc.csv')

st.title('Comparativa de conciertos en Aragón y España')
st.write(data)
data.shape
data.columns

# data[['Año','Música clásica Conciertos de música','Música popular Conciertos de música']]

st.title('Datos sobre los conciertos de música clásica y popular en Aragón')
data_ar = data[ data['Territorio'] == 'Aragón']
data_ar

st.write('Datos sobre la suma de la recaudación en miles de euros de los conciertos de música clásica en España en general')
data_es = data[ data['Territorio'] == 'España']['Música clásica Recaudación (miles de euros)'].sum()
data_es

st.title('Gráfica sobre el gasto medio por espectador en conciertos de música clasica en comparación con la popular')
chart = alt.Chart(data).mark_circle().encode(
    x = 'Música clásica Gasto medio por espectador (euros)',
    y = 'Música popular Gasto medio por espectador (euros)',
    color = 'Año',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)

name = st.slider('¿De que año quieres saber los conciertos?', 2003, 2020, 2003)
st.write('Has elegido el año ', name)

st.text('Rango desde el número minimo de espectadores en música clásica hasta el máximo')
values = st.slider(
    'Selecciona un rango',
    129, 332, (129, 232))
st.write('Rango entre:', values)

st.title('Lugar del evento')
ter = st.select_slider(
    'Selecciona el territorio donde se realizaron los conciertos',
    options=[ 'Aragón', 'España'])
st.write('Has elegido el territorio', ter)

tert = st.radio("Selecciona el Territorio que deseas ver", data['Territorio'].unique())
st.write("Has selecciona el territorio de:", tert)

st.title('Gráfica sobre la recaudación en miles de euros, comparando los conciertos de música clásica con los de música popular')
chart = alt.Chart(data).mark_circle().encode(
    x = 'Música clásica Recaudación (miles de euros)',
    y = 'Música popular Recaudación (miles de euros)',
    color = 'Año',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)
