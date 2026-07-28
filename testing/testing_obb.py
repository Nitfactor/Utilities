import yfinance as yf

stock = yf.Ticker("RELIANCE.NS")

current_price = stock.fast_info['last_price']
print(f"₹{current_price}")