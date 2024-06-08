import pandas as pd

df = pd.read_csv('/Users/alexeysobolev/PycharmProjects/Data Analysis for Hospitals/Topics/Reshaping and Pivot Tables/Mean/data/dataset/input.txt',
                 sep=',')

df = df.pivot_table(index='labels', values=['null_deg', '60_deg', '90_deg', '180_deg', '240_deg'])
print(df.loc['R', 'null_deg'].round(2))
