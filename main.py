# Importing required modules

import streamlit as st
import pandas as pd
import numpy as np

url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

# Reading csv file

df=pd.read_csv(url)
st.table(df.head())