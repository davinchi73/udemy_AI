import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Create a line plot"""

# years = [2010, 2011, 2012, 2013]
# sales = [100, 120, 140, 160]
# plt.plot(years, sales, label="Sales Trend", color="blue", marker="o")
# plt.title("Sales over the years")
# plt.xlabel("buns")
# plt.ylabel("burgers")
# plt.legend()
# plt.show()

"""Create a bar chart"""
categories = ["Electronics", "Clothing", "Groceries"]
revenue = [250, 400, 150]
plt.bar(categories, revenue, color="green")
plt.title("revenue by category")
plt.show()