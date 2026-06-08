import numpy as np
#––––––––––––––––––
#1. Log returns
#––––––––––––––––––

#simple returns are non additive over time
#we use log

prices = np.array([100.0, 150.0, 75.0])
simple_returns = np.diff(prices) / prices[:-1]

log_returns = np.log(prices[1:]/prices[:-1])
#since log return = ln(P_t/P_t-1)

#interconversion
simple_return = 0.10
log_return = np.log(1+simple_return)
back_to_simple = np.exp(log_return)-1
#use simple returns for reporting, weights, modelling

#–––––––––––––––––––
#2. Rolling Statistics
#––––––––––––––––––––
#20 days of return
np.random.seed(42)
returns = np.random.normal(0.001, 0.02, 20)

#manual rolling mean (window of 5)
window = 5
rolling_means = np.array([
    returns[i:i+window].mean()
    for i in range(len(returns) - window + 1)
])
#code up a helper function usually

#–––––––––––––––––––––
#3. Drawdowns
#–––––––––––––––––––––
#The largest peak to trough decline before a new peak is reached
#This is the worst case that actually happened


#simulate price path
np.random.seed(123)
returns = np.random.normal(0.001, 0.02, 100)
prices = 100*np.cumprod(1+returns)

#running maximum (peak at each point)
running_max = np.maximum.accumulate(prices)
#drawdown 
drawdowns = (prices-running_max)/running_max
