import pandas as pd
import yfinance as yf
import pprint
pp = pprint.PrettyPrinter(indent=4)


def get_best_investment_day(stock_symbol):
    # Download historical stock data from Yahoo Finance
    stock = yf.Ticker(stock_symbol)
    historical_data = stock.history(start='2023-01-01', end='2023-06-30')
    # historical_data['date_obj'] = pd.to_datetime(historical_data['Date'])
    historical_data['weekday'] = historical_data.index.day_name()
    print(historical_data.index)
    historical_data.to_csv("APPL.csv")

    # Calculate average returns for each day of the month
    average_returns = {}
    for index, row in historical_data.iterrows():
        day = index.day
        # day = row['weekday']

        close_price = row['Close']
        if day in average_returns:
            average_returns[day].append(close_price)
        else:
            average_returns[day] = [close_price]

    # Calculate the mean returns for each day
    for day, prices in average_returns.items():
        average_returns[day] = sum(prices) / len(prices)
        pp.pprint(f'day = {day} and sum(prices) = {sum(prices)} and len(prices) = {len(prices)} {average_returns[day]} \n')

    # Find the day with the highest average returns
    best_day = min(average_returns, key=average_returns.get)
    # pp.pprint(average_returns)
    return best_day


# Example usage
stock_symbol = "CYIENT.NS"  # Replace with your desired stock symbol
best_investment_day = get_best_investment_day(stock_symbol)
print(f"The best day of the month to invest in {stock_symbol} is: {best_investment_day}")
