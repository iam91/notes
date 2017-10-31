import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats 


x = np.array([6, 11, 15, 18, 20], dtype=np.float)
y = np.array([6, 8, 12, 20, 30], dtype=np.float)
n = len(x)
alpha = 0.05
x_bar = x.mean()

# a.
print 'a.'
sum_x = x.sum()
sum_y = y.sum()
sum_xx = (x ** 2).sum()
sum_xy = (x * y).sum()

b1 = sum_xy - (sum_x * sum_y) / n
b1 /= (sum_xx - sum_x ** 2 / n) 
b0 = y.mean() - b1 * x.mean()

print 'y = {:3f} {:+3f}x'.format(b0, b1)
print '-' * 30

# b.
print 'b.'
y_est = b0 + b1 * x
res = y - y_est
print res
print '-' * 30

zeros = np.zeros(n)

# c.
print 'c.'
plt.scatter(x, res)
plt.plot(x, zeros)
plt.show()
print '-' * 30

# d.
print 'd.'
h = (x - x_bar) ** 2
h = h / h.sum()
h = h + 1. / n

sse = np.sum(res ** 2)
mse = sse / (n - 2)
s = np.sqrt(mse)

s_res = s * np.sqrt(1 - h)
res_std = res / s_res
print res_std
print '-' * 30

# e.
print 'e.'
plt.scatter(x, res_std)
plt.plot(x, zeros)
plt.show()
print '-' * 30