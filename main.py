# Importing required modules

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

# Reading csv file

df=pd.read_csv(url)

#Un-pivoting datas 

df1=df.melt(id_vars=['Country/Region','Province/State','Lat','Long'],var_name='Date',value_name='Running total')  

page_selected=st.sidebar.radio('Select Page',['Demo','Cases','Deaths','Recovered'])

#Demo page creation
if page_selected=='Demo':
    st.header('Covid19')
    st.text('Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.')
    st.subheader('Daily cases')
    selected_country=st.selectbox('Select Country',list(df1['Country/Region'].unique()))
    st.write('Total cases till today in ',selected_country,' is')
    df1[df1['Country/Region']=='India'][['Date','Running total']].tail(1)
    st.subheader(int(df1[df1['Country/Region']=='India']['Running total'].tail(1)))
    st.table(df1[df1['Country/Region']==selected_country].tail(1).reset_index())

#Cases page creation
if page_selected=='Cases':
    st.header('Cases')
    selected_country=st.selectbox('Select Country',list(df1['Country/Region'].unique()))
    st.write('Total cases till today in ',selected_country,' is')
    st.subheader(int(df1[df1['Country/Region']=='India']['Running total'].tail(1)))
    # Created new DataFrame inorder to calculate the dail cases count
    df2=df1[df1['Country/Region']==selected_country]
    # Created a list and stored the running total values
    l=list(df2['Running total'])
    # Inserted 0 at 0 th index
    l.insert(0,0)
    # Removed last element in the list
    l.pop()
    # created new column in the dataframe df2 with the values in the list l
    df2['new_value']=l
    # Calculation for to find the daiy count and updated that calculated value as a column in df2
    df2['Daily_cases']=df2['Running total']-df2['new_value']
    st.write('Below table shows the last five days cases ')
    st.table(df2[['Country/Region','Date','Daily_cases']].tail().reset_index())
    fig = px.line(df2[df2['Country/Region']==selected_country],x = 'Date',y = 'Daily_cases',)
    st.plotly_chart(fig)

#Cases page creation
#if page_selected=='Deaths':




