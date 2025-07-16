import pandas as pd

'''
EX 1: load and explore a dataset
'''

#  data url: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# Load data
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# explore structure of the data
# print("Print first 5 rows: \n", data.head(5))
# print("Print last 5 rows: \n", data.tail(5))
# print("Print basic information: \n", data.info())
# print("Print statistical information: \n", data.describe())


'''
EX 2 select specific columnus and filter the rows
'''

# select columns
selected_columns = data[["species", "sepal_length"]]
print("Selected columns \n", selected_columns)

# filtering rows
filtered_rows = data[(data["sepal_length"] > 5.2) & (data["species"] == "setosa")]
print("Filtered rows: \n", filtered_rows)