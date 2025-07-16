import pandas as pd

data = {"name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

# syntax for group by
grouped = df.groupby("column_name")

# printing the name and group
for name, group in grouped:
    print(name)
    print(group)

# aggregation
grouped.mean()
grouped.sum()

# aggregation functions
'''
using groupby alongside functions
'''

# gives mean of a column based on grouped by
df.groupby("caregory_column")["numeric_column"].mean()

# gives us aggregation metrics
df.groupby("category_column").agg({"numeric_coolumn": ["mean", "max", "min"]})

# pivoting data
pivot = df.pivot_table(
    values="numeric_column",
    index="category_columnn",
    aggfunc="mean"
)

# custom aggregation
def range_function(x):
    return x.max() - x.min()

# uses range_function ^ as custom aggregation function for the operation
df.groupby("category_col")["numeric_col"].agg(range_function)

