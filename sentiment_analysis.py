import pandas as pd
from transformers import pipeline
from datetime import datetime

# Debug: Print contents of AAPL_market_data.csv before running
print("Contents of AAPL_market_data.csv before running:")
try:
    market_data = pd.read_csv("AAPL_market_data.csv")
    print(market_data.head())
except Exception as e:
    print(f"Error reading AAPL_market_data.csv: {e}")

# Load the mock X posts dataset
x_posts = pd.read_csv("mock_x_posts.csv")

# Initialize the sentiment analysis pipeline with a pre-trained BERT model
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to analyze sentiment of each post
def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    label = result['label']  # POSITIVE or NEGATIVE
    score = result['score']  # Confidence score
    # Map BERT labels to our desired labels: positive, negative, neutral
    if label == "POSITIVE" and score > 0.7:
        return "positive", score
    elif label == "NEGATIVE" and score > 0.7:
        return "negative", score
    else:
        return "neutral", score

# Apply sentiment analysis to each post
x_posts['sentiment'], x_posts['sentiment_score'] = zip(*x_posts['text'].apply(analyze_sentiment))

# Save the results to a new CSV file
output_file = "AAPL_sentiment.csv"
print(f"Writing to {output_file}...")
x_posts.to_csv(output_file, index=False)
print(f"Sentiment analysis results saved to {output_file}")

# Debug: Print contents of AAPL_market_data.csv after running
print("Contents of AAPL_market_data.csv after running:")
try:
    market_data = pd.read_csv("AAPL_market_data.csv")
    print(market_data.head())
except Exception as e:
    print(f"Error reading AAPL_market_data.csv: {e}")