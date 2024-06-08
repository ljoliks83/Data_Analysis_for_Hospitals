import pandas as pd

df = pd.DataFrame({'a': [1, 4], 'b': [2, 5]})

# Your code here

df['c'] = {0: 3, 1: 6, 2: 9}
df = pd.concat([df, pd.DataFrame.from_records([{'a': 7, 'b': 8, 'c': 9}])], ignore_index=True)
