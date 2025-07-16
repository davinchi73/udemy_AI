import pandas as pd

# stupid data creation for sake of examples
data = {"name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)


'''
data transformations (renaming columns / changing
data types / creating or modifying columns)
'''

# how to rename columns in df
df = df.rename(columns={"old_col_name": "new_col_name"})

# change data type of a column
df["column_name"] = df["column_name"].astype("float")

# converts data in columns to date time format
df["column_name"] = pd.to_datetime(df["column_name"])

# modify existing column (multiply values in old column by 2)
df["new_column"] = df["existing_column"] * 2


'''
combining and merging dataframes
- concatenation
- merging
- joining
'''

# combine data along rows (0) or columns (1)
combined = pd.concat([df1, df2], axis=0)
combined = pd.concat([df1, df2], axis=1)

# merging dataframes based on a commmon column (primary or foreign keys?)
merged = pd.merge(df1, df2, on="common_column_to_merge_on")

# specify left join, you can also do inner or outer etc
merged = pd.merge(df1, df2, how="left", on="common_col")

# using joins (basically uses merging with indexes)
joined = df1.join(df2, how="inner")