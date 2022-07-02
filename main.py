# Importing required modules

import streamlit as st
import pandas as pd
import numpy as np

url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

# Reading csv file

df=pd.read_csv(url)

#Un-pivoting datas 

df1=df.melt(id_vars=['Country/Region','Province/State','Lat','Long'],var_name='Date',value_name='Running total')  

page_selected=st.sidebar.radio('Select Page',['Demo','Cases','Deaths','Recovered'])

if page_selected=='Demo':
    st.header('Covid19')
    st.text('Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.')
    st.subheader('Daily cases')
    selected_country=st.selectbox('Select Country',list(df1['Country/Region'].unique()))
    st.write('Total cases till today in ',selected_country,' is')
    df1[df1['Country/Region']=='India'][['Date','Running total']].tail(1)
    st.subheader(int(df1[df1['Country/Region']=='India']['Running total'].tail(1)))
    st.table(df1[df1['Country/Region']==selected_country].tail(1).reset_index())
    

