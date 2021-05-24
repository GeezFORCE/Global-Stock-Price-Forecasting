''' mainOverview.py : Page for navigating the various overview pages'''


# External Imports
import streamlit as st

# Internal Imports
from . import companyOverview
from . import financialsOverview
from . import stockCharts

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
        try:
            st.write('Close Price')
            st.plotly_chart(stockCharts.getStockChart(ticker, ['Close'], 'Close Price'))
            st.write('Volume Traded')
            st.plotly_chart(stockCharts.getStockChart(ticker, ['Volume'], 'Volume'))

        except :
            st.warning("Warning !!! Check Parameters.") 