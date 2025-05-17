import yfinance as yf
import tweepy
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# X API credentials (commented out for now)
# X_API_KEY = os.getenv("X_API_KEY")
# X_API_SECRET = os.getenv("X_API_SECRET")
# X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
# X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

# # Initialize X API client
# auth = tweepy.OAuthHandler(X_API_KEY, X_API_SECRET)
# auth.set_access_token(X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to fetch market data using yfinance
def fetch_market_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    print(f"Fetched market data for {ticker}: {stock_data.shape[0]} rows")
    return stock_data[['Open', 'High', 'Low', 'Close', 'Volume']]

# Function to fetch X posts for a given ticker (commented out for now)
# def fetch_x_posts(ticker, num_posts=100):
#     query = f"${ticker} -filter:retweets"
#     tweets = []
#     for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(num_posts):
#         tweets.append({
#             'text': tweet.full_text,
#             'created_at': tweet.created_at,
#             'user': tweet.user.screen_name
#         })
#     tweet_df = pd.DataFrame(tweets)
#     print(f"Fetched {tweet_df.shape[0]} X posts for {ticker}")
#     return tweet_df

# Example usage
if __name__ == "__main__":
    # Define parameters
    ticker = "AAPL"
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    # Fetch market data
    market_data = fetch_market_data(ticker, start_date, end_date)
    market_data.to_csv(f"{ticker}_market_data.csv")
    print(f"Market data for {ticker} saved to {ticker}_market_data.csv")
    
    # Fetch X posts (commented out for now)
    # x_posts = fetch_x_posts(ticker)
    # x_posts.to_csv(f"{ticker}_x_posts.csv")
    # print(f"X posts for {ticker} saved to {ticker}_x_posts.csv")