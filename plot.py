import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('prices.csv')

# Plot the BTCUSDT prices as a line chart
plt.figure(figsize=(10,6))
plt.plot(df['date'], df['BTCUSDT'])
plt.title('BTCUSDT Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('BTCUSDT.jpg')
