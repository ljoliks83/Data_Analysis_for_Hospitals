import pandas as pd

df = pd.read_csv('/Users/alexeysobolev/PycharmProjects/Data Analysis for Hospitals/Topics/Handling missing values/Guess the meaningful replacement/data/dataset/input.txt',
                 sep=',')

df['totsp'] = df['totsp'].fillna(df['livingsp'] + df['nonlivingsp'])

print(int(df.agg({'totsp': 'sum'}).iloc[0]))
