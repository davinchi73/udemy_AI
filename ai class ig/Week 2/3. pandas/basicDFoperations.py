import pandas as pd

s = pd.Series([10, 20, 30], index = ["a", "b" ,"c"])

data = {"name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

'''
Basic Operations:
'''

# print first 5 rows of dataframe
print(df.head())

# print last 5
print(df.tail())

# statistical summary
print(df.describe())


'''
Selecting:
'''

# print name column
print(df["name"])

# printing multiple columns
print(df[["name", "age"]])

# data at position (first ROW by position)
print(df.iloc[0])

# data at position (first COLUMN by position)
print(df.iloc[:, 0])

# print name column
print(df.iloc[:, "Name"])

'''
Filtering:
'''

# filter rows age > 25
print(df[df["age"] > 25])

