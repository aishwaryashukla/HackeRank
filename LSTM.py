import yfinance as yf

# Define the stock symbol
symbol = 'AAPL'

# Get the stock data
stock_data = yf.Ticker(symbol)

# Get the latest stock price
latest_price = stock_data.info['regularMarketPrice']

# Get the latest stock volume
latest_volume = stock_data.info['regularMarketVolume']

# Print the latest stock price and volume
print(f"The latest price of {symbol} is ${latest_price:.2f} and the latest volume is {latest_volume:,}")
