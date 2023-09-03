import requests

def get_stock_price(symbol):
    url = "https://api.nseindia.com/api/quote/get-quote?symbol=" + symbol
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["lastPrice"]
    else:
        raise Exception("Error fetching stock price")


if __name__ == "__main__":
    symbol = input("Enter stock symbol: ")
    price = get_stock_price(symbol)
    print("Current price of {} is {}".format(symbol, price))
