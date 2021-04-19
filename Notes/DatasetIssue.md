#### Datset Issue

- Dataset was not splitting into validation and stock data with the following code
- ```

    last20Percent= Dates[-int(0.2*len(Dates))]
    validationStocks = Stocks[(Stocks.index >= last20Percent)]
    Stocks = Stocks[(Stocks.index < last20Percent)]

  ```

- It is replaced with loc implementation

- ```
    last20Percent = Dates[-int(0.20*len(Dates))]
    validationStocks = stocks.loc[stocks.index.values >= last20Percent]
    stocks = stocks.loc[stocks.index.values < last20Percent]
  ```
