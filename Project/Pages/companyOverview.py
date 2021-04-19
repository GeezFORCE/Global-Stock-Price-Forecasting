# External Imports
import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen

# Internal Imports

# Function controlling company overview - displays ticker information
def getCompanyOverview(ticker):
    tickerInfo = yf.Ticker(ticker).info
    col1, col2  = st.beta_columns(2)

    with col1:
        st.image(Image.open(urlopen(tickerInfo['logo_url'])), use_column_width='auto')

    with col2:
        st.header(f'{tickerInfo["longName"]} ({tickerInfo["symbol"]})')
        st.subheader(tickerInfo['sector'])
        st.write(tickerInfo['country'])
        st.write(tickerInfo['website'])
        st.write(tickerInfo['currency'])
    
    st.write(tickerInfo['longBusinessSummary'])

    st.write("Previous Close : ", tickerInfo["previousClose"])
    st.write("Regular Market Previous Close : ", tickerInfo["regularMarketPreviousClose"])
    st.write("Open : ", tickerInfo["open"])
    st.write("Regular Market Open : ", tickerInfo["regularMarketOpen"])


