import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# define the list of tickers
tickers = ['RELIANCE.NS', 'SBIN.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS',  'MARUTI.NS', 'TATASTEEL.NS', 'ONGC.NS', 'ITC.NS']

# download historical stock price data from Yahoo Finance
data = yf.download(tickers, period='1mo', group_by='ticker')

# extract the closing prices
close_prices = pd.DataFrame()
for ticker in tickers:
    close_prices[ticker] = data[ticker]['Close']

# compute the correlation matrix
corr_matrix = close_prices.corr()

# create a heatmap of the correlation matrix using Seaborn
sns.set(style='white')
fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', vmin=-1, vmax=1, ax=ax)

# set the axis labels and title
ax.set_xlabel('Stock Tickers')
ax.set_ylabel('Stock Tickers')
ax.set_title('10x10 Correlation Matrix of Stock Prices (20-day period)')

# display the plot
plt.show()