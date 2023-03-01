import requests
from binance.client import Client
import csv

# Replace YOUR_API_KEY and YOUR_API_SECRET with your actual API key and secret
client = Client(api_key='YOUR_API_KEY', api_secret='YOUR_API_SECRET')

exchange_info = requests.get("https://api.binance.com/api/v1/exchangeInfo").json()

symbols = [symbol['symbol'] for symbol in exchange_info['symbols']]
pairs = []

for symbol in symbols:
    if symbol.endswith('USDT'):
        ticker = client.get_ticker(symbol=symbol)
        pairs.append(ticker)

# Get the column headers for the CSV file from the keys of the first ticker dictionary
headers = list(pairs[0].keys())

# Write the tickers to a CSV file
with open('tickers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for ticker in pairs:
        writer.writerow(ticker.values())
