try:
    import matplotlib.pyplot as plt
except ImportError:
    print("matplotlib is not installed. Please install it with 'pip install matplotlib'.")
    plt = None

#most plotting done by ai, need to know basics tho

#–––––––––––––––––––––––
#1. basics figure and axes
#––––––––––––––––––––––––

#figure is the entire canvas, axes is the plot
#a figure can have multiple plots

fig, ax = plt.subplots(figsize = (8,4))

#plot
ax.plot([1,2,3,4], [10,20,15,25])
ax.set_title('My first plot')
ax.set_xlabel('day')
ax.set_ylabel('value')

#or pass an array to ax.plot

#–––––––––––––––––––––––––––
#2. plotting a timeseries
#–––––––––––––––––––––––––––

import numpy as np
import pandas as pd

dates = pd.date_range('2024-01-01', periods=60, freq='B')
np.random.seed(42)
prices = 100 * np.cumprod(1 + np.random.normal(0.0005, 0.015, 60))
df = pd.DataFrame({'close': prices}, index=dates)

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(dates, prices, color='blue', linewidth=1.5, label='AAPL')
ax.set_title('AAPL Stock Price')
ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100, freq='B')
returns = np.random.normal(0.0005, 0.015, 100)
prices = 100 * np.cumprod(1 + returns)

# 2 rows, 1 column
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# Top: Price
ax1.plot(dates, prices, color='#26804a')
ax1.set_title('Price')
ax1.set_ylabel('Price')
ax1.grid(True, alpha=0.3)

# Bottom: Returns
ax2.bar(dates, returns, color='#26804a', alpha=0.7, width=1)
ax2.axhline(y=0, color='red', linestyle='-', alpha=0.5)
ax2.set_title('Daily Returns')
ax2.set_ylabel('Return')
ax2.grid(True, alpha=0.3)

plt.tight_layout()



import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# 4 different return distributions
distributions = [
  ('Normal', np.random.normal(0, 0.02, 500)),
  ('Fat Tails', np.random.standard_t(3, 500) * 0.015),
  ('Skewed', np.random.exponential(0.015, 500) - 0.015),
  ('Bimodal', np.concatenate([np.random.normal(-0.02, 0.01, 250), np.random.normal(0.02, 0.01, 250)]))
]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()  # Makes indexing easier

for ax, (name, data) in zip(axes, distributions):
  ax.hist(data, bins=30, color='#26804a', alpha=0.7, edgecolor='white')
  ax.set_title(name)
  ax.axvline(x=0, color='red', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()