import pandas as pd

# # series
# s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# # data frame
# data = {"name": ["Alice", "Bob"], "Age": [25, 30]}
# df = pd.DataFrame(data)

# examples to load data into diff formats
df = pd.read_csv("filename.csv")
df.to_csv("filename.csv", index = False)

df = pd.read_excel("filename.xlsx")
df.to_excel("filename.xlsx", index = False)