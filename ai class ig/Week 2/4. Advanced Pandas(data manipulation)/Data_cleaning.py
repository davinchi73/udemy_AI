import pandas as pd

# create dumn df
data = {"name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

'''
dropping missing values
'''

# drop rows without values
df = df.drapna()

# drop columns with missing values
df = df.dropna(axis=1)


'''
filling missing values
'''

# replace na/empty values in column with 0
df["column_name"] = df["column_name"].fillna(0)

# backward and forward fill for filling na
df.fillna(method="ffill")
df.fillna(method="bfill")

# will fill values based on interpolation
df["column_name"] = df["column_name"].interpolate()