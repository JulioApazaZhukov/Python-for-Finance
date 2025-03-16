import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf

style.use('ggplot')
start = dt.datetime(2000,1,1)
end = dt.datetime(2024,12,31)

df = yf.download('MMM', start=start, end=end)   # Data frame
# If the data is from a .csv
#   df = pd.read_csv('MMM.csv')
#   df = pd.read_csv('MMM.csv', parse_dates=True, index_col=0)

print(df.head())    # Prints the first 5 values by default
print(df.tail())    # Prints the last 5 values by default
print(df.head(3))   # Prints the 3 first values
print(df.tail(3))   # Prints the 3 last values

df.to_csv('MMM.csv')    # Downloads the data into a .csv file