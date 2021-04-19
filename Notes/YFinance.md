# YFinance

## Installation

- Install using `pip install yfinance`
- Import using `import yfinance as yf`

## Tickers

- Ticker is a stock symbol used to uniiquely identify the stock.
- Every stock in Yahoo Finance has a ticker symbol.
- Eg : Microsoft - MSFT, Nifty50 - ^NSEI

### Import Data using Ticker

- `stockName = yf.Ticker(tickerName)`
- eg: `microsoft = yf.Ticker("MSFT") nifty = yf.Ticker("^NSEI")`

#### Full Information of Stock

- `stockName.info`
- For a field `stockName.info['FieldName']`

#### Other Functions

##### get historical market data

`hist = msft.history(period="max")`

##### show actions (dividends, splits)

`msft.actions`

##### show dividends

`msft.dividends`

##### show splits

`msft.splits`

##### show financials

`msft.financials`
`msft.quarterly_financials`

##### show major holders

`msft.major_holders`

##### show institutional holders

`msft.institutional_holders`

##### show balance sheet

`msft.balance_sheet`
`msft.quarterly_balance_sheet`

##### show cashflow

`msft.cashflow`
`msft.quarterly_cashflow`

##### show earnings

`msft.earnings`
`msft.quarterly_earnings`

##### show sustainability

`msft.sustainability`

##### show analysts recommendations

`msft.recommendations`

##### show next event (earnings, etc)

`msft.calendar`

##### show ISIN code - _experimental_

##### ISIN = International Securities Identification Number

`msft.isin`

##### show options expirations

`msft.options`

##### get option chain for specific expiration

`opt = msft.option_chain('YYYY-MM-DD')`

#### Documentation

`https://pypi.org/project/yfinance/`
