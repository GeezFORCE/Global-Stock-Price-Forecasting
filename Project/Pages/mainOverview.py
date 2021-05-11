# External Imports
# External Imports
from Project.constants import TICKER_TO_PREDICT
import streamlit as st
import yfinance as yf

# Internal Imports
from . import companyOverview
from . import financialsOverview
from . import stockCharts
from .. import constants

# Function calling Overview Pages
def mainOverview():
    ticker = st.sidebar.text_input(label='Ticker', value='GOOG', help='Input the ticker')
    tickerInformation = st.sidebar.selectbox(label='Ticker Information',
                        options=['Ticker Information', 'Financials', 'Charts'],
                        help='Get information about ticker')
    if tickerInformation == 'Ticker Information':
        companyOverview.getCompanyOverview(ticker)
    elif tickerInformation == 'Financials':
        financialsOverview.getFinancialsOverview(ticker)
    elif tickerInformation == 'Charts':
        st.write('Close Price')
        st.plotly_chart(stockCharts.getStockChart(ticker, ['Close'], 'Close Price'))
        st.write('Volume Traded')
        st.plotly_chart(stockCharts.getStockChart(ticker, ['Volume'], 'Volume'))