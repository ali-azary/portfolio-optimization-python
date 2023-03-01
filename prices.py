import pandas as pd
from binance.client import Client
from datetime import datetime


# Read the CSV file into a DataFrame
df = pd.read_csv('tickers.csv')
# Calculate the market cap for each ticker
# note: the total trading volume for the ticker in the quote currency (in this case, USDT), not the circulating supply of the token
df['marketCap'] = df['lastPrice'] * df['quoteVolume']
# Print the first 5 rows of the DataFrame
# print(df.head())

# Sort the DataFrame by marketCap column in descending order and get the top 10 rows
top_10 = df.sort_values('marketCap', ascending=False).head(10)

# Print the top 10 market cap coins
# print(top_10.symbol)

# Replace YOUR_API_KEY and YOUR_API_SECRET with your actual API key and secret
client = Client(api_key='YOUR_API_KEY', api_secret='YOUR_API_SECRET')

symbol=top_10.symbol[0]
klines=client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1DAY, '1month ago UTC')
price=pd.DataFrame(columns=['date',symbol])
price['date'] = [pd.to_datetime(int(x[0]),unit='ms') for x in klines]
price.set_index('date', inplace=True)
price[symbol] = [float(x[4]) for x in klines]
for symbol in top_10.symbol[1:]:
    klines=client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1DAY, '1month ago UTC')
    try:
        price[symbol] = [float(x[4]) for x in klines]
    except:
        pass
price.to_csv('prices.csv')