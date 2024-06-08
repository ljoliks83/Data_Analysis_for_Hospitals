# Your code here. 
# The dataset is already loaded, the variable that contains the DataFrame is called penguins_example
import pandas as pd

adelie = {
    'species': 'Adelie',
    'bill_length_mm': 45.7,
    'bill_depth_mm': 15.5
}

penguins_example = pd.concat([penguins_example, pd.DataFrame.from_records([adelie])], ignore_index=True)

print(penguins_example)