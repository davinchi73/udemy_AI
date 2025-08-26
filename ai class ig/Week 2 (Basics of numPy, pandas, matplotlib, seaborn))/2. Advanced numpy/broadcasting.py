import numpy as np

'''
notes:

broadcasting: 
performing operations on arrays of different shapes/sizes.
smaller arrays will be expanded to match size of larger

Rules of broadcasting:
dimensions are aligned from the right
dimensions are compatible if:
    - matches other arrays dimension
    - one of the dimensions is 1   
'''

# array and scalar broadcasting
arr = np.array([1, 2, 3])
# print(arr + 10) # adds 10 to each element in the array

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0, 1])
print(matrix + vector)

