import pandas as pd

df = pd.read_csv('/Users/alexeysobolev/PycharmProjects/Data Analysis for Hospitals/Topics/Handling missing values/Replace with the mode/data/dataset/input.txt',
                 sep=',')

mode_loc = df['location'].mode()[0]
df['location'] = df['location'].fillna(mode_loc)

print(df.head(5))