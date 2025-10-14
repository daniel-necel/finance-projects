
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


ticker_symbol = input("Enter stock ticker (e.g. AAPL, TSLA, MSFT): ").upper()

try:
    data = yf.download(ticker_symbol, period="5d", interval="1h", progress=False)
except Exception as e:
    print(f"Error downloading data: {e}")
    exit()

if data.empty:
    print("No data found for that ticker symbol. Please try again.")
    exit()

latest = data.tail(1)
current_price = float(latest["Close"].iloc[0])
previous_close = float(data["Close"].iloc[-2])
change = current_price - previous_close
percent_change = (change / previous_close) * 100

print(f"\n===== {ticker_symbol} STOCK REPORT =====")
print(f"Current Price: £{current_price:.2f}")
print(f"Change: £{change:.2f} ({percent_change:.2f}%)")

avg_price = float(data["Close"].mean())
max_price = float(data["Close"].max())
min_price = float(data["Close"].min())

print(f"\nAverage Price (5 days): £{avg_price:.2f}")
print(f"Highest Price: £{max_price:.2f}")
print(f"Lowest Price: £{min_price:.2f}")

plt.figure(figsize=(8, 4))
plt.plot(data.index, data["Close"], marker='o', linestyle='-', color='blue')
plt.title(f"{ticker_symbol} – 5 Day Price Trend")
plt.xlabel("Date & Time")
plt.ylabel("Price (£)")
plt.grid(True)
plt.tight_layout()
plt.show()

save = input("\nWould you like to save this data as CSV? (y/n): ")
if save.lower() == "y":
    file_name = f"{ticker_symbol}_stock_data.csv"
    data.to_csv(file_name)
    print(f"Data saved as {file_name}")
