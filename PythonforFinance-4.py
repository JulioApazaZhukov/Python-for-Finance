import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 

df = pd.read_csv('MMM.csv', header=[0,1], parse_dates=True, index_col=0)
df['Close'].plot(figsize=(12, 6))
plt.show()