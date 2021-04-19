# External Imports
import streamlit as st
import plotly.express as px
import yfinance as yf

# Function to draw Close and Open Prices of ticker

def getStockChart(ticker, parameterList, title):
    tickerData = yf.Ticker(ticker).history(period='max')
    fig = px.line(tickerData, x=tickerData.index , y=parameterList, title=title)
    fig.layout.update(xaxis_rangeslider_visible=True)
    return fig
