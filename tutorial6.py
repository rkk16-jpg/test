import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import altair as alt
from datetime import datetime
import datetime
import time

st.title('SARs Data Visualisation')

metrics =['table view', 'biggest spike','positive values','negative values','blanks']
cols = st.selectbox('Metric to view', metrics)
# let's ask the user which column should be used as Index
if cols in metrics:
    metric_to_show_in_covid_Layer = cols

if cols == "table view":
    st.header("This is the table view")

@st.cache
def load_data():
    data = pd.read_csv('SAR_data_cleaning.csv')
    return data
df = load_data()

a = df.max()
# c = alt.Chart(df).mark_circle().encode()
# st.altair_chart(c, width=-1)

st.write(df)

