#  write your code here 

import pandas as pd

df = pd.read_csv('/Users/alexeysobolev/PycharmProjects/Data Analysis for Hospitals/Topics/Reading data in pandas/Max values/data/dataset/input.txt',
                 delimiter=',')

print(max(df['Age']))