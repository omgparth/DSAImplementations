import pandas as pd

#instead of being indexed by integers 0, 1, 2
#finance data is indexed by timestamps

prices_no_dates = pd.DataFrame({'close': [100, 102, 101]})

# DatetimeIndex - now we know exactly when
dates = pd.to_datetime(['2024-01-02', '2024-01-03', '2024-01-04'])
prices_with_dates = pd.DataFrame({'close': [100, 102, 101]}, index=dates)

#with this we can select data by data df['2024-01'] for all of january
#can resample to convert daily to weekly or monthly 
#align series by date
#handle missing days
##### for finance always use dates as index

#––––––––––––––––––––––––––––––––––––––––––––
# 1. Creating DatetimeIndex
#––––––––––––––––––––––––––––––––––––––––––––

#convert strings to datetime with pd.to_datetime()
date_strings = ['2024-01-02', '2024-01-03']
dates = pd.to_datetime(date_strings)
#df=df.set_index('date')


#convert a range of dates with pd.date_range()

#5 calendar days
calendar_days = pd.date_range('2024-01-01', periods = 5, freq='D')
business_days = pd.date_range('2024-01-01', periods=5, freq='B')
month_ends = pd.date_range('2024-01-01', periods=3, freq='ME')
print(f"Month ends: {month_ends.tolist()}")

#D= calendar day, 'B' = business day, 'W'=week, ME = month end
#MS - month start, YE year end. Use B since most markets close on weekned

#––––––––––––––––––––––––––
# 2. time based selections
#––––––––––––––––––––––––––
import numpy as np
#select rows by date using loc

#create a year of daily data
dates = pd.date_range('2024-01-01', '2024-12-31', freq="B")
np.random.seed(42)
df = pd.DataFrame({
    'close': 100*np.cumprod(1+np.random.normal(0.0003, 0.01, len(dates)))
}, index=dates)

#select a specific date
print(df.loc['2024-06-03'])
#select a month by partial string match
print(df.loc['2024-06'].head())
#daterange
q1 = df.loc['2024-01':'2024-03']
#.loc[] is inclusive on both ends remember, unlike list indexing

#–––––––––––––––––––––––––––––
# 3. resampling (convert one freq to other)
#–––––––––––––––––––––––––––––

#daily data for 3 months
dates = pd.date_range('2024-01-01', periods = 63, freq="B")
np.random.seed(500)
df = pd.DataFrame({
    'close' : 100*np.cumprod(1+np.random.normal(0.0005, 0.01, len(dates)))
}, index=dates)

#resample to weekly by taking last price each week
weekly = df.resample('W').last()
print("Weekly closes:")
print(weekly.head())

#resample to monthly 
monthly = df.resample('ME').last()

#for ohclv
dates = pd.date_range('2024-01-01', periods=21, freq='B')
np.random.seed(42)
df = pd.DataFrame({
  'open': 100 + np.random.randn(21).cumsum(),
  'high': 102 + np.random.randn(21).cumsum(),
  'low': 98 + np.random.randn(21).cumsum(),
  'close': 100 + np.random.randn(21).cumsum(),
  'volume': np.random.randint(100000, 500000, 21)
}, index=dates)

# Weekly OHLCV - different agg for each column
weekly = df.resample('W').agg({
  'open': 'first',
  'high': 'max',
  'low': 'min',
  'close': 'last',
  'volume': 'sum'
})
print(weekly)
#remember downsampling (daily to weekly) aggregate multiple rows to one
#use .last(), first, mean, sum or agg
#upsampling (weekly to daily) create more rows with.ffill()

#–––––––––––––––––––––––––––––––––
# 4. Rolling windows compute stats over a moving window
#–––––––––––––––––––––––––––––––––

dates = pd.date_range('2024-01-01', periods=60, freq='B')
np.random.seed(42)
prices = 100 * np.cumprod(1 + np.random.normal(0.0005, 0.015, 60))
df = pd.DataFrame({'close': prices}, index=dates)

#20 day sma 
df['sma_20'] = df['close'].rolling(20).mean()
#20 day rolling std
df['std_20'] = df['close'].rolling(20).std()

print(df.tail(10))

#daily returns
df['return'] = df['close'].pct_change()
#20 day rolling vol annuallised
df['vol_20'] = df['return'].rolling(20).std() * np.sqrt(252)
df['sharpe_20'] = (df['return'].rolling(20).mean() * 252)/df['vol_20']

#shift and lag allow you to access previous or future vals with .shift()

df['prev_close'] = df['close'].shift(1)
df['return'] = (df['close']-df['prev_close'])/df['prev_close']
#same as pct change

#predict next returns for Machine learning targets
df['next_return'] = df['return'].shift(-1) #negative shift

#NaN at boundaries .shift(1) creates first row Nan (no previous val)
#shift(-1) does last row nan, rolling(20) first 19 nans. use dropna