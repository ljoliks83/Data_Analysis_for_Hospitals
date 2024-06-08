import pandas as pd

df = pd.read_csv('/Users/alexeysobolev/PycharmProjects/Data Analysis for Hospitals/Topics/Handling missing values/Handle missing values/data/dataset/input.txt',
                 sep=',')

df.dropna(axis=1, thresh=7, inplace=True)
medians = []

for i in range(len(df.columns)):
    medians.append(df.iloc[:, i].median())
    df.iloc[:, i] = df.iloc[:, i].fillna(medians[i])

print(df.head())
