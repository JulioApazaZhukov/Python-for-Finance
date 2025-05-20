import pandas as pd
import matplotlib as plt
import datetime as dt
from matplotlib import style

style.use('ggplot')

df = pd.read_csv('MMM.csv', header=[0,1], parse_dates=True, index_col=0)

df.plot()
plt.show()