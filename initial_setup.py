import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Define the date range for historical stock data
end_date = datetime(2025, 4, 22)
start_date = end_date - timedelta(days=5)

# Fetch AAPL stock data
stock = yf.download('AAPL', start=start_date, end=end_date)
stock.reset_index(inplace=True)

# Handle MultiIndex columns if present
if isinstance(stock.columns, pd.MultiIndex):
    # Flatten the MultiIndex by taking the first level (Price)
    stock.columns = [col[0] for col in stock.columns]

# Reorder columns to match expected order
expected_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
stock = stock[expected_columns]  # Reorder columns

# Validate the data
if list(stock.columns) != expected_columns:
    raise ValueError(f"Unexpected columns in stock data: {stock.columns}. Expected: {expected_columns}")

# Ensure numerical columns are of the correct type
numerical_columns = ['Open', 'High', 'Low', 'Close']
for col in numerical_columns:
    stock[col] = pd.to_numeric(stock[col], errors='coerce')
stock['Volume'] = stock['Volume'].astype(int)

# Save the stock data
print("Writing to AAPL_market_data.csv...")
stock.to_csv("AAPL_market_data.csv", index=False)
print("Stock data saved to AAPL_market_data.csv")

# Verify the saved file
saved_data = pd.read_csv("AAPL_market_data.csv")
print("Contents of AAPL_market_data.csv after writing:")
print(saved_data.head())

# Create mock X posts
mock_posts = pd.DataFrame({
    'text': [
        "AAPL earnings beat expectations, stock is a buy!",
        "Loving the new AAPL product, definitely a game-changer!",
        "AAPL stock looks overvalued, might sell soon.",
        "AAPL is killing it today, great performance!",
        "Mixed feelings about AAPL’s latest move, holding for now.",
        "AAPL stock dropping, not a good sign.",
        "Disappointing AAPL update, selling my shares.",
        "AAPL looks risky right now, I’m out.",
        "AAPL might recover, but I’m cautious.",
        "Not sure about AAPL’s future, staying neutral.",
        "AAPL is soaring today, great earnings report!",
        "Not impressed with AAPL's latest product launch, might sell my shares.",
        "AAPL stock looks stable, holding for now.",
        "Wow, AAPL just hit a new all-time high, amazing!",
        "Concerned about AAPL’s supply chain issues, could impact stock price."
    ],
    'created_at': [
        "2025-04-17 10:00:00", "2025-04-17 11:00:00", "2025-04-17 12:00:00", "2025-04-17 13:00:00", "2025-04-17 14:00:00",
        "2025-04-21 10:00:00", "2025-04-21 11:00:00", "2025-04-21 12:00:00", "2025-04-21 13:00:00", "2025-04-21 14:00:00",
        "2025-04-22 10:00:00", "2025-04-22 11:00:00", "2025-04-22 12:00:00", "2025-04-22 13:00:00", "2025-04-22 14:00:00"
    ],
    'user': ['user1', 'user2', 'user3', 'user4', 'user5', 'user1', 'user2', 'user3', 'user4', 'user5', 'user1', 'user2', 'user3', 'user4', 'user5']
})
mock_posts.to_csv("mock_x_posts.csv", index=False)
print("Mock X posts saved to mock_x_posts.csv")