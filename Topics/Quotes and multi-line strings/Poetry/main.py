import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/alexeysobolev/Documents/My/PythonTmp/2015.csv')

df.plot(y=['Family', 'Freedom'], kind='hist', alpha=0.5)

plt.show()
