import numpy as np

# set seed, output will be same every time, good for training and testing sets
np.random.seed(42)

# random array , 3x3, uniform dist from 0 to 1
rand_arr = np.random.rand(3, 3)

# matrix 2x3 rand ints from 0 to 10
random_ints = np.random.randint(0, 10, size=(2, 3))

