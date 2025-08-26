import numpy as np

""" Identity matrix, zero matrix, Diagonal """

# Create Identity Matrix
identity = np.eye(3)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Multiplication(dot product) should eval to A: \n", A.dot(identity))

# Create Diagonal and Zero matrix
diagonal = np.diag([1, 7, 9])
zero = np.zeros((3, 3))
print("Diag: \n", diagonal)
print("zero: \n", zero)