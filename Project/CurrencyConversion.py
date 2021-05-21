"""CurrencyConversion.py: Convert Non-USD stock data to USD and vice-versa"""


# External Imports
import yfinance as yf
from py_currency_converter import convert

# Internal Imports
from . import constants

# Function to convert Non-USD stocks values into USD


def convertCurrency(stocks):
    for ticker in stocks.columns.levels[0]:
        # Fetch the currency of ticker
        tickerCurrency = yf.Ticker(ticker).info['currency']
        if tickerCurrency != 'USD':
            conversionRate = convert(
                base=tickerCurrency, amount=1, to=['USD'])['USD']
            # Convert returns a dictionary with {currencyName : exchangeRate}
            # we take the exchange rate out of the dictionary
            stocks[ticker, 'Close'] = (stocks[ticker]['Close']).apply(
                lambda x: x*conversionRate)
    return stocks


# Function to convert the values back

def inverseConvertCurrency(val):
    earliertickercurrency = yf.Ticker(constants.TICKER_TO_PREDICT).info['currency']
    if earliertickercurrency != 'USD':
        conversionRate = convert(base='USD',amount=1, to=[earliertickercurrency])[earliertickercurrency]
        val=val*conversionRate
    return val
    
