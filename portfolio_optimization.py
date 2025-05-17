import pandas as pd
import numpy as np
import time
from scipy.optimize import minimize

# Load the sentiment-price correlation data
data = pd.read_csv("AAPL_sentiment_price_correlation.csv")

# For simplicity, we'll optimize a portfolio with just AAPL
returns = data['Price_Change'].dropna().values  # Historical returns
expected_return = np.mean(returns)  # Expected return based on historical data
sentiment_adjustment = data['sentiment_score'].iloc[0]  # Adjust return based on sentiment
if data['sentiment'].iloc[0] == 'positive':
    expected_return *= (1 + sentiment_adjustment * 0.1)  # Boost return if sentiment is positive
elif data['sentiment'].iloc[0] == 'negative':
    expected_return *= (1 - sentiment_adjustment * 0.1)  # Reduce return if sentiment is negative

# Risk (covariance matrix, simplified to variance for a single asset)
risk = np.var(returns)

# Quantum-inspired heuristic: Simulate a simple Grover-like search
# We'll evaluate the objective function for binary weights (0 or 1) and pick the best
def objective_function(w):
    return expected_return * w - risk * w**2

start_time_quantum = time.time()
# Simulate Grover's search: evaluate all possible binary values (0 or 1)
weights = [0, 1]
objective_values = [objective_function(w) for w in weights]
best_weight = weights[np.argmax(objective_values)]
quantum_time = time.time() - start_time_quantum

# Classical optimization for comparison
def classical_objective(w):
    return - (expected_return * w - risk * w**2)  # Negative for minimization
start_time_classical = time.time()
result_classical = minimize(classical_objective, x0=0.5, bounds=[(0, 1)], method='SLSQP')
classical_time = time.time() - start_time_classical

# Compare runtimes
speedup = (classical_time - quantum_time) / classical_time * 100
print(f"Quantum-inspired optimization time: {quantum_time:.4f} seconds")
print(f"Classical optimization time: {classical_time:.4f} seconds")
print(f"Speedup: {speedup:.2f}%")

# Save results
results_df = pd.DataFrame({
    'Asset': ['AAPL'],
    'Weight': [best_weight],
    'Quantum_Time': [quantum_time],
    'Classical_Time': [classical_time],
    'Speedup (%)': [speedup]
})
results_df.to_csv("portfolio_optimization.csv", index=False)
print("Portfolio optimization results saved to portfolio_optimization.csv")