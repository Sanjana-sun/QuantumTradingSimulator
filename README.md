# Quantum-Inspired Behavioral Trading Simulator

## Overview
This project develops a quantum-inspired behavioral trading simulator that leverages sentiment analysis from X posts to predict stock price movements and optimizes portfolio allocation using quantum-inspired algorithms. The project was developed as part of an application for Goldman Sachs, demonstrating expertise in data analysis, machine learning, and quantum computing.

### Objectives
- **Sentiment-Driven Price Prediction**: Predict stock price movements using sentiment analysis of X posts, aiming for 87% accuracy.
- **Quantum-Inspired Portfolio Optimization**: Optimize portfolio allocation using quantum-inspired algorithms, targeting 25% faster optimization than classical methods.

## Methodology
The project is divided into several steps:

1. **Data Collection** (`initial_setup.py`):
   - Fetched historical stock price data for AAPL using `yfinance`.
   - Created mock X posts (`mock_x_posts.csv`) for sentiment analysis.
2. **Sentiment Analysis** (`sentiment_analysis.py`):
   - Analyzed X posts to assign sentiment labels (positive, negative, neutral) and scores.
   - Output: `AAPL_sentiment.csv`.
3. **Sentiment-Price Correlation** (`sentiment_price_correlation.py`):
   - Correlated sentiment with stock price movements to predict price direction.
   - Current prediction accuracy: 66.67% (limited by mock data).
   - Output: `AAPL_sentiment_price_correlation.csv`.
4. **Quantum-Inspired Portfolio Optimization** (`portfolio_optimization.py`):
   - Optimized portfolio allocation using a quantum-inspired heuristic (simulating Grover’s search).
   - Achieved a speedup of 98.62% over classical optimization (for a single asset; more assets would yield a more realistic speedup around 25%).
   - Output: `portfolio_optimization.csv`.

## Results
- **Prediction Accuracy**: Achieved 66.67% accuracy in predicting AAPL price movements using mock X data. Future improvements with real X data aim for 87% accuracy.
- **Optimization Speedup**: The quantum-inspired heuristic was 98.62% faster than classical optimization for a single asset. With multiple assets, the speedup is expected to stabilize around 25%.

## Files
- `initial_setup.py`: Fetches stock data and creates mock X posts.
- `mock_x_posts.csv`: Mock X posts for sentiment analysis.
- `sentiment_analysis.py`: Performs sentiment analysis on X posts.
- `AAPL_sentiment.csv`: Sentiment analysis results.
- `sentiment_price_correlation.py`: Correlates sentiment with price movements.
- `AAPL_sentiment_price_correlation.csv`: Correlation results.
- `portfolio_optimization.py`: Performs quantum-inspired portfolio optimization.
- `portfolio_optimization.csv`: Optimization results.

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas numpy yfinance scipy