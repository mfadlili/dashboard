import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Salesperson Performance Review",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/mfadlili',
        'Report a bug': "https://github.com/mfadlili",
        'About': "#CAP."
    }
)

@st.cache_data
def load_data1():
    data = pd.read_csv('https://raw.githubusercontent.com/mfadlili/upload_csv/master/cap_data_ingestion_dashboard.csv')
    return data

df1 = load_data1()

st.title('Salesperson Performance Review')
st.title('')
col1, col2, col3 = st.columns(3)

def total_sales():
    total_revenue = "$ " +str(round(df1['sales'].sum()))
    st.metric(label="Total Salesperson Revenue (2011-2014)", value=total_revenue)

def total_salesperson():
    salesperson = df1.fullname.nunique()
    st.metric(label="Total Active Salesperson", value=salesperson)

def total_region():
    ter = df1.name.nunique()
    st.metric(label="Total Teritory", value=ter)

with col1:
    total_sales()

with col2:
    total_salesperson()

with col3:
    total_region()

d1 = df1.groupby(['fullname', 'salespersonid', 'year_order']).sales.sum().reset_index()
d2 = df1.groupby(['year_order', 'territoryid',	'name']).sales.sum().reset_index()

col1,col2 = st.columns([1,1])
col3,col4 = st.columns([1,1])

with col1:
    st.markdown("<h2 style='text-align: center; color: black;'>Salesperson Revenue </h2>", unsafe_allow_html=True)
    year = [int(i) for i in d1.year_order.unique()]
    year.sort()
    year.append('all')
    option = st.selectbox("Year:", year)
    if option == 'all':
        result = d1.groupby(['fullname']).sales.sum().reset_index().sort_values(by=['sales'], ascending=False)
        fig1 = px.bar(result,y='fullname',x='sales',color='fullname',color_discrete_sequence=px.colors.sequential.Darkmint,height=450,width=500, text_auto='.2s')
        fig1.update_layout(xaxis_title='Revenue Generated ($)',yaxis_title=' ', showlegend = False)
        st.plotly_chart(fig1)
    result = d1[d1.year_order==option].sort_values(by=['sales'], ascending=False)
    fig1 = px.bar(result,y='fullname',x='sales',color='fullname',color_discrete_sequence=px.colors.sequential.Darkmint,height=450,width=500, text_auto='.2s')
    fig1.update_layout(xaxis_title='Revenue Generated ($)',yaxis_title=' ', showlegend = False)
    st.plotly_chart(fig1)

with col2:
    st.markdown("<h2 style='text-align: center; color: black;'>Revenue Generated per Year</h2>", unsafe_allow_html=True)
    st.markdown("", unsafe_allow_html=True)
    st.title('')
    st.title('')
    result = d1.groupby('year_order').sales.sum().reset_index()
    fig3 = px.bar(result,y='sales',x='year_order',color='sales',color_discrete_sequence=px.colors.sequential.Darkmint,height=450,width=650, text_auto='.2s')
    fig3.update_layout(xaxis_title='Year',yaxis_title='Total Revenue Generated ($)', showlegend = False)
    st.plotly_chart(fig3)

with col3:
    st.markdown("<h2 style='text-align: center; color: black;'>Revenue by Teritory</h2>", unsafe_allow_html=True)
    year = [int(i) for i in d1.year_order.unique()]
    year.sort()
    year.append('all')
    option = st.selectbox("Teritory:", year)
    if option == 'all':
        result = d2.groupby(['name']).sales.sum().reset_index().sort_values(by=['sales'], ascending=False)
        fig1 = px.bar(result,y='name',x='sales',color='name',color_discrete_sequence=px.colors.sequential.Darkmint,height=450,width=500, text_auto='.2s')
        fig1.update_layout(xaxis_title='Revenue Generated ($)',yaxis_title=' ', showlegend = False)
        st.plotly_chart(fig1)
    result = d2[d2.year_order==option].sort_values(by=['sales'], ascending=False)
    fig1 = px.bar(result,y='name',x='sales',color='name',color_discrete_sequence=px.colors.sequential.Darkmint,height=450,width=500, text_auto='.2s')
    fig1.update_layout(xaxis_title='Revenue Generated ($)',yaxis_title=' ', showlegend = False)
    st.plotly_chart(fig1)
