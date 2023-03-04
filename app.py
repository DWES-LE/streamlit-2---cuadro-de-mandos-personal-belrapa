import pandas as pd
import streamlit as st

data = pd.read_csv('conc.csv')

st.write(data)
data.columns