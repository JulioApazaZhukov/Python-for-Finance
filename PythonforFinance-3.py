import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

style.use('ggplot')

df = pd.read_csv('^GSPC_L.csv', parse_dates=True, index_col=0)

#   df['100ma'] = df['Adj Close'].rolling(window=100).mean()
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df['200ma'] = df['Adj Close'].rolling(window=200, min_periods=0).mean()

#   df.dropna(inplace=True)

print(df.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax1.plot(df.index, df['200ma'])
ax2.bar(df.index, df['Volume'])

plt.show()