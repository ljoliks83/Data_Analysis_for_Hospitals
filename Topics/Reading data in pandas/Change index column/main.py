#  write your code here 

import pandas as pd

df = pd.read_csv('/Users/alexeysobolev/PycharmProjects/Data Analysis for Hospitals/Topics/Reading data in pandas/Change index column/data/dataset/input.txt',
                 index_col='Name')

print(df.head(10))