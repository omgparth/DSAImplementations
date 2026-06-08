import pandas as pd
#provides dataframes, they behave like excel sheets and operations 
#are vectorised. 

#each col has a name

#––––––––––––––––––––––––––––––––
#1. Creating a dataframe
#––––––––––––––––––––––––––––––––
#use dictionary
data = {
  'ticker': ['AAPL', 'GOOGL', 'MSFT'],
  'price': [178.50, 141.25, 378.90],
  'shares': [100, 50, 25]
}

df = pd.DataFrame(data)

#from a np array
#5days of price data
import numpy as np
prices = np.array([
  [150.0, 75.0, 200.0],
  [152.3, 76.2, 198.5],
  [151.8, 74.8, 201.0],
  [154.2, 77.1, 203.2],
  [153.5, 76.5, 202.8]
])

df = pd.DataFrame(prices, columns = ['AAPL', 'GOOGL', 'MSFT'])

#––––––––––––––––––––––––––––
# 2. Accesing cols
#––––––––––––––––––––––––––––

df = pd.DataFrame({
  'ticker': ['AAPL', 'GOOGL', 'MSFT'],
  'price': [178.50, 141.25, 378.90],
  'shares': [100, 50, 25]
})

#bracker notation always works
print (df['price'])
#dot notation cleaner but only for simple names
print(f"Tickers: {df.ticker.tolist()}")
#multicols by passing a list
subset = df[['ticker', 'price']]
print(subset)

##Important: df['price'] returns list, df[['price']] returns dataframe (2d table w 1col)
#–––––––––––––––––––––––––
#3. Accesing rows
#–––––––––––––––––––––––––

#use iloc
print(df.iloc[0]) #first row and so on
#uses integer location of rows

#,loc[] for label based access
#first set ticker as the index aka rowlabel
df = df.set_index('ticker') #now each ticker labels the row
print(f"\nAAPL price: {df.loc['AAPL', 'price']}")
print(df.loc[['GOOGL', 'MSFT']])

#–––––––––––––––––––––––
#4. Filtering data
#–––––––––––––––––––––––
expensive = df[df['price']>150]
print(f"stocks above 150: {expensive}")
filtered = df[(df['price']>150) and (df['ticker']=='AAPL')]
#parentheses required when creating conditionals

#†ø add new cols just write df['colname'] = df['val1']*df['val2'] or whatever calc
#or for a constant just = constant

#to compute simple return just
df['return'] = df['close'].pct_change()
#common stats given by df.mean(), df.std(), df.describe() for all

#all np functions work on df

