# Simple return calculation (Used with more than just 1 stock)

import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

y_symbols = ['TSLA', 'AAPL']
startdate = '2021-01-05'
enddate = '2021-01-20'

data = pdr.get_data_yahoo(y_symbols, start=startdate, end=enddate)['Adj Close']
returns = data.pct_change()        #pct is an integrated function within the pandas_datareader module (percentage change)

print(returns)