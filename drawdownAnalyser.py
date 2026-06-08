import numpy as np

def analyse_drawdowns(prices):
    '''computes drawdown stats from a price series'''
    running_max = np.maximum.accumulate(prices)
    drawdowns = (prices - running_max)/running_max

    max_dd = drawdowns.min()
    max_dd_idx = drawdowns.argmin()
    peak_idx = np.argmax(prices[:max_dd_idx+1])

    return {
        'max_dd' : max_dd, 
        'peak_price' : prices[peak_idx], 
        'trough_price' : prices[max_dd_idx],
        'peak_day' : peak_idx,
        'trough_day' : max_dd_idx
    }


#Test it
np.random.seed(42)
returns = np.random.normal(0.0005, 0.015, 252)  # 1 year
prices = 100 * np.cumprod(1 + returns)

stats = analyse_drawdowns(prices)
print(f"Max Drawdown: {stats['max_dd']:.2%}")
print(f"Peak: ${stats['peak_price']:.2f} on day {stats['peak_day']}")
print(f"Trough: ${stats['trough_price']:.2f} on day {stats['trough_day']}")