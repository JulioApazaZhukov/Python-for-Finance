import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf

style.use('ggplot')

df = pd.read_csv('MMM.csv', header=[0,1], parse_dates=True, index_col=0)

print(df)
df.plot(figsize=(12, 6))
df['Open'].plot(figsize=(12, 6))
print(df[['Open','High']].head())

plt.show()