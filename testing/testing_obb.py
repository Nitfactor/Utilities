import yfinance as yf
from pydantic import BaseModel

# stock = yf.Ticker("RELIANCE.NS")

# current_price = stock.fast_info['last_price']
# print(f"₹{current_price}") 

stock_tcs = yf.Ticker("TCS.NS")
current_price_tcs = stock_tcs.fast_info['last_price']
# Download the entire historical data for TCS.NS and save to a CSV file
historical_data_tcs = stock_tcs.history(period="max")
# Define the format of each row using Pydantic
from typing import Optional
import pandas as pd

class StockData(BaseModel):
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Volume: Optional[float]
    Dividends: Optional[float]
    Stock_Splits: Optional[float]

# Reset index to make 'Date' a column
historical_data_tcs_reset = historical_data_tcs.reset_index()

# Rename columns to match our Pydantic model if necessary
historical_data_tcs_reset = historical_data_tcs_reset.rename(columns={"Stock Splits": "Stock_Splits"})

# Validate and format each row
validated_rows = []
for row in historical_data_tcs_reset.to_dict(orient="records"):
    try:
        record = StockData(**row)
        validated_rows.append(record.dict())
    except Exception as e:
        print(f"Row validation error: {e}, row: {row}")

# Create a DataFrame from the validated rows
df_formatted = pd.DataFrame(validated_rows)

# Save the formatted, validated data to CSV
df_formatted.to_csv("TCS_historical_data.csv", index=False)