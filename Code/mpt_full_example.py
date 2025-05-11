# Import necessary libraries
import numpy as np
import pandas as pd
import portfolio_params as params
import portfolio_optimisers as opt
import allocations as alloc
import plotting as plot
import results as results
from Individual_Functions import price_data, returns_data
import warnings
import re

# CvxPy gives us a warning when a solution may be inaccurate, we will ignore this message but this block can be deleted if one wants to keep the message
warnings.filterwarnings("ignore",
                        category=UserWarning,
                        message=re.escape("Solution may be inaccurate. Try another solver, adjusting the solver settings, or solve with verbose=True for more information.")
                       )

# Get price data for all stocks from csv file and then drop those we do not have a full historical price data for
full_df = pd.read_csv('S&P500_Prices.csv', index_col=0)
valid_tickers = full_df.dropna(axis=1).columns.tolist()

# Check we have at least n valid tickers
n = 25
if len(valid_tickers) >= n:
    # Randomly sample n from valid tickers
    np.random.seed(0)
    chosen_tickers = sorted(np.random.choice(valid_tickers, size=n, replace=False))
    df = full_df[chosen_tickers]
else:
    raise ValueError(f"Only {len(valid_tickers)} tickers have full data — not enough for {n}.")

# Call return function
ret_df = returns_data(df)

# Calculate expected returns, covariance and correlation matrices using our Parameters class
parameters = params.parameters(ret_df, frequency=252, risk_free_rate=0.041)
mu = parameters.expected_returns_capm()
cov,cov_df = parameters.covariance_matrix_ledoit_wolf()
corr_df = parameters.correlation_matrix()

# Plot our covariance and correlation matrices as heatmaps
plot.heatmap(cov_df)
plot.heatmap(corr_df)

# Calculate the optimal weights for a given strategy
opts = opt.optimisers(mu, cov, weight_bounds=[-1,1])
ret_maxret, risk_maxret, weights_maxret = opts.maximise_return(results=True)
ret_minrisk, risk_minrisk, weights_minrisk = opts.minimise_risk(target_return = 0, results=True)
ret_maxsr, risk_maxsr, weights_maxsr = opts.maximise_sharpe_ratio(risk_free_rate=0.046, results=True)

# Plot these weights
plot.weights(mu, cov, weight_bounds=[-1,1], risk_free_rate=0.046)

# Plot Efficient Frontier
plot.efficient_frontier(mu, cov, risk_free_rate=0.046, weight_bounds=[-1,1])

# Find the optimal allocation and leftover amount for a given strategy
allocation, leftover = alloc.allocation(df.iloc[-1], weights_maxsr, total_investment=10_000, short_ratio=0.2, reinvest=False, remove_zero_investments=False, results=True)

# Plot the allocations of strategies
plot.allocations(df, mu, cov, weight_bounds=[-1,1], risk_free_rate=0.046, total_investment=10_000)

# Full results of everything
metrics, distributions, leftovers = results.full_results(df, mu, cov, weight_bounds=[-1,1], risk_free_rate=0.046, total_investment=10_000, short_ratio=0.2, results=True)