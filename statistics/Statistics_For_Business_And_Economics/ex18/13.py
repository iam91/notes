import numpy as np

import simple_linear_regression as slr

# data format
y = np.array([205, 202, 195, 190, 191, 188, -1])
n = len(y)
n_train = 6

x = np.arange(n) + 1

slr.simple_linear_regression(x, y, n_train)