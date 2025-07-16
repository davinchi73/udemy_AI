import pandas as pd

# fake data
data = {
    "Class": ["A", "B", "A", "B", "C", "C"],
    "Score": [85, 90, 88, 72, 95, 80],
    "Age": [15, 16, 15, 17, 16, 15]
}

'''
ex 1: group data by a categorical column
'''

# into dataframe
df = pd.DataFrame(data)

# print og data
print("Original Dataset: \n", df)

# group data
grouped = df.groupby("Class").mean()
# print(grouped)


'''
ex 2: calculate summary statistics for grouped data
'''

# get various stats across the data
stats = df.groupby("Class").agg(
    {"Score": ["mean", "max", "min"], "Age": ["mean", "max", "min"]}
)

print(stats)