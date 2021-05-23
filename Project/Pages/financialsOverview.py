''' financialsOverview.py : Get Quarterly financials, major and institutional 
                            holders about the ticker selected'''


# External Imports
import streamlit as st
import yfinance as yf
import plotly.express as px

# Function to get financials related to ticker
def getFinancialsOverview(ticker):
    st.header('Financials')

    # st.subheader('Quarterly Financials')
    # st.write((yf.Ticker(ticker)).financials)

    try:
        st.subheader('Major Holders')
        majorHolders = yf.Ticker(ticker).major_holders
        st.plotly_chart(px.pie(majorHolders, values=majorHolders.index , names=list(majorHolders[1])))
        st.subheader('Instituional Holders')
        institutionalHolders = yf.Ticker(ticker).institutional_holders
        st.plotly_chart(px.bar(institutionalHolders, x='Holder', y='Shares'))
        
    except KeyError :
        st.write("Please provide a Valid Ticker !")