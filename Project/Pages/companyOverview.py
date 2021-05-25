''' companyOverview.py : Get Overview about the ticker selected'''

# External Imports
import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import HTTPErrorProcessor, urlopen

# Internal Imports

# Function controlling company overview - displays ticker information
def getCompanyOverview(ticker):
    try :
        tickerInfo = yf.Ticker(ticker).info
        col1, col2  = st.beta_columns(2)

        with col1:
            try :
                st.image(Image.open(urlopen(tickerInfo['logo_url'])), use_column_width='auto')
                
            except :
                #Image Error
                st.write(tickerInfo['logo_url'])
                st.error("Something went wrong...  \nUnable to load the Logo")

        with col2:
            st.header(f'{tickerInfo["longName"]} ({tickerInfo["symbol"]})')
            try:
                st.subheader(tickerInfo['sector'])
            except KeyError :
                st.warning("Sector: Data not available.")
            try:
                st.write(tickerInfo['country'])
            except KeyError :
                st.warning("Country: Data not available.")
            try:
                st.write(tickerInfo['website'])
            except KeyError :
                st.warning("Website: Data not available.")
            try:
                st.write(tickerInfo['currency'])
            except KeyError :
                st.warning("Currency: Data not available.")
        
        try:
            st.write(tickerInfo['longBusinessSummary'])
        except KeyError :
            st.warning("longBusinessSummary:Data not avaialable")

        st.write("Previous Close : ", tickerInfo["previousClose"])
        st.write("Regular Market Previous Close : ", tickerInfo["regularMarketPreviousClose"])
        st.write("Open : ", tickerInfo["open"])
        st.write("Regular Market Open : ", tickerInfo["regularMarketOpen"])
    
    except ValueError :
        st.warning("Please provide a Valid Ticker !")
    except KeyError :
        st.warning("Either Ticker name is too long or that Isn't a valid Ticker!")
    except NameError :
        st.error("Ticker information not found")

