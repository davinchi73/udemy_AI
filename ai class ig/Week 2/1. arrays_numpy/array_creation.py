import numpy as np

arr = np.array([1, 2, 3, 4])
# print(arr)

# 3x3 matrix of 0s
zeros = np.zeros((3, 3))
# print(zeros)

# 2x4 matrix of 1s
ones = np.ones((2, 4))

# one to ten at interval of 2, X to Y int of Z
range_arr = np.arrange(1, 10, 2)

# 5 evenly spaced numbers, between 1 anad 0, 
linspace_array = np.linspace(0, 1, 5)

# reshapes the array from 1x6 to 2x3
array = np.array([1, 2, 3, 4, 5, 6])
# reshaped = array.reshape([2, 3]) # make sure dimensions work

# expands array into new dimension (first input)
expanded = array[:, np.newaxis] # you might need to learn more about this lol

