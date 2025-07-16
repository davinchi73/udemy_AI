import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))

# ^ etc

# filtering

arr[arr > 3] = 0 # all elements greater than 3 set to 0

arr[arr % 2 == 0] # all even elements

