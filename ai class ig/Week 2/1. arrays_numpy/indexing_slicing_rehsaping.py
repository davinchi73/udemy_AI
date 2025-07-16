import numpy as np

# indexing
arr = np.array([10, 20, 30, 40, 50, 60])
# arr[2] = 30
# arr[-1] = 60

# slicing
# arr[1:4] = get items from 1 to 4 excluding 4th element
# arr[:3] get all nums till 3 excluding 3

# reshaping
reshaped = arr.reshape(2, 3)
# reshapes to 2x3 array from 1x6