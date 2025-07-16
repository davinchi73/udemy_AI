import pandas as pd

'''
pandas data structures:

- series
    - one dimensional array

- data frames
    - like a table, 2d
'''

# series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# data frame
data = {"name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

print(df)