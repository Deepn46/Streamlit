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

page_selected=st.sidebar.radio('Select Page',['Demo','Cases','Deaths'])       #'Recovered'
selected_country=st.sidebar.selectbox('Select Country',list(df1['Country/Region'].unique()))
date_series= df1[df1['Country/Region']==selected_country]['Date'].tail(1)
for i in date_series:
    date=i
st.sidebar.write('Update on : ',date)

#Demo page creation
if page_selected=='Demo':
    st.subheader('Daily cases')
    date_series= df1[df1['Country/Region']==selected_country]['Date'].tail(1)
    for i in date_series:
        date=i
    col1,col2= st.columns(2)
    with col1:
        st.write('Total cases in {} is'.format(selected_country))
    with col2:
        st.write('Updated till ')

    col1,col2= st.columns(2)
    with col1:
        st.subheader(int(df1[df1['Country/Region']==selected_country]['Running total'].tail(1)))
    with col2:
        st.subheader(date) 

   
#Cases page creation
if page_selected=='Cases':
    st.header('Cases')
    #selected_country=st.selectbox('Select Country',list(df1['Country/Region'].unique()))
    st.write('Total cases in ',selected_country,' is')
    st.subheader(int(df1[df1['Country/Region']==selected_country]['Running total'].tail(1)))
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
    fig = px.line(df2[df2['Country/Region']==selected_country],x = 'Date',y = 'Daily_cases',)
    fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    st.plotly_chart(fig)
    st.write('Below table shows the last five days cases ')
    df3= df2[['Country/Region','Date','Daily_cases']].tail()
    df3=df3.reset_index()
    st.table(df3[['Country/Region','Date','Daily_cases']])
  

#Deaths page creation
if page_selected=='Deaths':
    st.header('Deaths')
    df_d=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    recovered_df=df_d.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='Date',value_name='Cummulative')
    #selected_country=st.selectbox('Select Country',list(recovered_df['Country/Region'].unique()))

    country_df=recovered_df[recovered_df['Country/Region']==selected_country]
    nl=list(country_df['Cummulative'])
    nl.pop()
    nl.insert(0,0)
    country_df['Dummy']=nl
    country_df['Daily_Death']=country_df['Cummulative']-country_df['Dummy']

    
    st.write('Total death in ',selected_country,' is')
    
    st.subheader(int(country_df[country_df['Country/Region']==selected_country]['Cummulative'].tail(1)))
    
    fig = px.line(country_df,x = 'Date',y = 'Daily_Death')
    fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    st.plotly_chart(fig)

    st.write('The below table shows the last five days death cases ')

    df4=country_df[['Country/Region','Date','Daily_Death']].tail()
    df4=df4.reset_index()
    st.table(df4[['Country/Region','Date','Daily_Death']])