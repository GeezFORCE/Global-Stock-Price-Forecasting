''' mainOverview.py : Page for navigating the various overview pages'''


# External Imports
import streamlit as st

# Internal Imports
from . import companyOverview
from . import financialsOverview
from . import stockCharts
from .searchticker import name_convert

# Function calling Overview Pages
def mainOverview():
    companyName =  st.sidebar.text_input('Enter Company Name' , value='State Bank Of India', max_chars=None, key=None, type='default', help="Returns Ticker of Company")
    tickerInformation = st.sidebar.selectbox(label='Ticker Information',
                        options=['Ticker Information', 'Financials', 'Charts'],
                        help='Get information about ticker')
    with st.spinner('Fetching Data'):
        ticker = name_convert(companyName).upper()
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