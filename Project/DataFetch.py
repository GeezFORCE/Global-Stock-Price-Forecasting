"""DataFetch.py: Fetches the stock data from Yahoo Finance"""


# External Imports
import yfinance as yf
import pandas as pd

# Internal Imports
from . import constants
from . import SaveData
from . import CurrencyConversion

# Function to fetch data based on Tickers provided


def getData():
    stocks = pd.DataFrame()
    stocks = yf.download(tickers=constants.TICKER_SET, 
                         period=constants.PERIOD, 
                         interval=constants.INTERVAL,
                         group_by='Ticker', 
                         auto_adjust=True, 
                         prepost=False, 
                         threads=True, 
                         proxy=None)

    SaveData.saveCSV(stocks, "OrginalStocks")

    stocks = stocks.drop(['Low', 'Open', 'High'], axis=1, level=1)  # Deleting columns we donot want
    stocks = stocks.fillna(stocks.mean())   # Fill the NaN values with the mean of columns

    stocks = CurrencyConversion.convertCurrency(stocks)

    SaveData.saveCSV(stocks, "stocks")

    return stocks
