# Logarithmic return calculation (Used with just 1 stock without too much volatility)

import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

y_symbols = ['TSLA', 'AAPL']
startdate = '2020-01-01'
enddate = '2021-01-20'

data = pdr.get_data_yahoo(y_symbols, start=startdate, end=enddate)['Adj Close']

returns = data.pct_change()        #pct is an integrated function within the pandas_datareader module
log_returns = np.log(1+data.pct_change())

# Mean

log_returns.mean()

#Annualized. 252 refers to the usually tradeable days within a year

S = log_returns.mean()*252

# Covariance

log_returns.cov()

#Annualized

D = log_returns.cov()*252

#Correlation matrix

X = log_returns.corr()

print(log_returns)

print("\nMean of logarithmic returns: \n\n", S)
print("\nCovariance matrix: \n\n", D)
print("\nCorrelation matrix: \n\n", X)