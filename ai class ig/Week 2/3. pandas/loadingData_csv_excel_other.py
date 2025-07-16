import pandas as pd

# # series
# s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# # data frame
# data = {"name": ["Alice", "Bob"], "Age": [25, 30]}
# df = pd.DataFrame(data)

df = pd.read_csv("filename.csv")
df = pd.read_excel("filename.xlsx")
