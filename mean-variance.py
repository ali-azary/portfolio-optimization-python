import pandas as pd
import numpy as np
from scipy.optimize import minimize

# Load the CSV file into a DataFrame
df = pd.read_csv('prices.csv', dtype=float, parse_dates=[0], index_col=0)


# Calculate the daily returns
returns_df = df.pct_change()

# Calculate the mean, variance, and covariance of the daily returns
mean_returns = returns_df.mean()
variances = returns_df.var()
covariances = returns_df.cov()


# Define the objective function (Sharpe ratio)
def objective(weights, mean_returns, covariances, risk_free_rate):
    port_return = np.dot(weights, mean_returns)
    port_std_dev = np.sqrt(np.dot(weights.T, np.dot(covariances, weights)))
    sharpe_ratio = (port_return - risk_free_rate) / port_std_dev
    return -sharpe_ratio

# Define the constraints
constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]
bounds = [(0, 1)] * len(mean_returns)

# Set the risk-free rate to 0
risk_free_rate = 0

# Use the optimizer to find the weights that maximize the Sharpe ratio
result = minimize(objective, np.ones(len(mean_returns)) / len(mean_returns), args=(mean_returns, covariances, risk_free_rate), bounds=bounds, constraints=constraints)
# result = minimize(objective, np.ones(len(mean_returns)) / len(mean_returns), args=(mean_returns, covariances, risk_free_rate), constraints=constraints)

weights=result.x




# Calculate expected return and standard deviation
expected_return = np.dot(weights.T, mean_returns)
portfolio_std = np.sqrt(np.dot(weights.T, np.dot(covariances, weights)))


# output results
with open('results.txt','w') as f:
    print("Mean returns:\n", mean_returns,file=f)
    print("Variances:\n", variances,file=f)
    print("Covariances:\n", covariances,file=f)
    # Print the optimized weights
    print("Optimized weights:\n", weights,file=f)
    print("Expected return: ", expected_return,file=f)
    print("Portfolio standard deviation: ", portfolio_std,file=f)

