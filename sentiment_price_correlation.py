import pandas as pd
import numpy as np
from datetime import datetime

# Load the stock price data
stock_data = pd.read_csv("AAPL_market_data.csv")
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data.set_index('Date', inplace=True)

# Load the sentiment data
sentiment_data = pd.read_csv("AAPL_sentiment.csv")
sentiment_data['created_at'] = pd.to_datetime(sentiment_data['created_at'])

# Aggregate sentiment by day
sentiment_data['date'] = sentiment_data['created_at'].dt.date
daily_sentiment = sentiment_data.groupby('date').agg({
    'sentiment_score': 'mean',
    'sentiment': lambda x: x.mode()[0]  # Most common sentiment label
}).reset_index()
daily_sentiment['date'] = pd.to_datetime(daily_sentiment['date'])

# Calculate stock price changes
stock_data['Price_Change'] = stock_data['Close'].pct_change()  # Daily percentage change in closing price
stock_data['Price_Direction'] = stock_data['Price_Change'].apply(lambda x: 1 if x > 0 else 0)  # 1 for up, 0 for down

# Merge sentiment and stock data
merged_data = stock_data.reset_index().merge(daily_sentiment, left_on='Date', right_on='date', how='inner')
print("Merged data shape:", merged_data.shape)
print("Merged data columns:", merged_data.columns)

# Predict price direction based on sentiment
def predict_price_direction(row):
    # Ensure row['Date'] is a datetime object
    row_date = pd.to_datetime(row['Date'])
    if row['sentiment_score'] > 0.7 and row['sentiment'] == 'positive':
        return 1
    elif row['sentiment_score'] > 0.7 and row['sentiment'] == 'negative':
        return 0
    else:
        # Use the previous day's direction if available, otherwise default to 0
        prev_day = stock_data[stock_data.index < row_date].tail(1)
        if not prev_day.empty:
            price_direction = prev_day['Price_Direction'].iloc[0]
            print(f"Previous day direction for {row_date}: {price_direction}")
            return int(price_direction)  # Ensure it’s an integer
        return 0

# Apply the prediction function
merged_data['Predicted_Direction'] = merged_data.apply(predict_price_direction, axis=1)

# Calculate prediction accuracy
accuracy = (merged_data['Price_Direction'] == merged_data['Predicted_Direction']).mean()
print(f"Prediction accuracy: {accuracy * 100:.2f}%")

# Save the results
output_file = "AAPL_sentiment_price_correlation.csv"
merged_data[['Date', 'Close', 'Price_Change', 'Price_Direction', 'sentiment', 'sentiment_score', 'Predicted_Direction']].to_csv(output_file, index=False)
print(f"Correlation results saved to {output_file}")