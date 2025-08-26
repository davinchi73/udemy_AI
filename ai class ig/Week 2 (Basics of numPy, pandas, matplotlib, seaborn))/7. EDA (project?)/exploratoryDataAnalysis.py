import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

""" Load titanic dataset """
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dataFrame = pd.read_csv(url)

""" Inspect Data here """
# print(dataFrame.info())
# print(dataFrame.describe())
# print(dataFrame.head())

""" Handle the missing values """
dataFrame["Age"] = dataFrame["Age"].fillna(dataFrame["Age"].median())
dataFrame["Embarked"] = dataFrame["Embarked"].fillna(dataFrame["Embarked"].mode()[0])

""" Remove Duplicates """
dataFrame = dataFrame.drop_duplicates()

""" Filter data: passengers in first class """
first_class = dataFrame[dataFrame["Pclass"] == 1]
print("First class Passengers: \n", first_class.head())

""" Display a bar chart """
# survival rate by class
# survival_by_class = dataFrame.groupby("Pclass")["Survived"].mean()
# survival_by_class.plot(kind="bar", color="skyblue")
# plt.title("Survival rate by class")
# plt.ylabel("Survival Rate")
# plt.show()

""" Histogram """
# histogram of age distribution
# sns.histplot(dataFrame["Age"], kde=True, bins=20, color="purple")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

""" ScatterPlot """
# age vs fare
plt.scatter(dataFrame["Age"], dataFrame["Fare"], alpha=0.1, color="red")
plt.title("Age vs Fare")
plt.ylabel("Fare")
plt.xlabel("Age")
plt.show()