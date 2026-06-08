import numpy as np

#Daily returns for a strat
np.random.seed(42)
daily_returns = np.random.normal(0.0005, 0.01, 252)

#risk free rate (daily)
rf_annual = 0.05
rf_daily = rf_annual/252

#excess returns
excess_returns = daily_returns - rf_daily

#daily sharpe
daily_sharpe = excess_returns.mean()/excess_returns.std()

annual_sharpe = daily_sharpe * np.sqrt(252)

#–––––––––––––––
#2. correlation
#–––––––––––––––

#4 assets 100 days
market = np.random.normal(0.001, 0.02, 100)

#assets w different correlations to market
assets = np.array([
    market,
    0.8*market + 0.2*np.random.normal(0, 0.02, 100), #high corr
    0.3 * market + 0.7 * np.random.normal(0, 0.02, 100), # Low correlation
    -0.5 * market + 0.5 * np.random.normal(0, 0.02, 100) # Negative correlation
])

corr_matrix = np.corrcoef(assets)

labels = ['Market', 'High', 'Low', 'Negative']
print("Correlation Matrix:")
for i, label in enumerate(labels):
  row = ' '.join([f"{corr_matrix[i,j]:6.2f}" for j in range(4)])
  print(f"{label:10} {row}")

