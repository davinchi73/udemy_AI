import numpy as np

# ex1: generate arrays for basic math operations
a = np.arange(1, 6) # = 1, 2, 3, 4, 5
b = np.arange(6, 11)

# print("Add: ", a + b)
# print("Sub: ", a - b)
# print("mult: ", a * b)
# print("div: ", a / b)


# ex2 create a 3x3 matrix and perform operations
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("OG matrix: \n", matrix)
# transpose operation
transpose = matrix.T
print("Transpose: \n", transpose)