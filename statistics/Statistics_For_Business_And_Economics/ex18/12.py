import numpy as np

import simple_linear_regression as slr

# data format
y = np.array([6, 11, 9, 14, 15, -1])
n = len(y)
n_train = 5

x = np.arange(n) + 1

slr.simple_linear_regression(x, y, n_train)