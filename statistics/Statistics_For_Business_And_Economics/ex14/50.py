import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([135,110,130,145,175,160,120], dtype=np.float)
y = np.array([145,100,120,120,130,130,110], dtype=np.float)

n = len(x)

sum_x = x.sum()
sum_y = y.sum()
sum_xx = (x ** 2).sum()
sum_xy = (x * y).sum()

b1 = sum_xy - (sum_x * sum_y) / n
b1 /= (sum_xx - sum_x ** 2 / n) 
b0 = y.mean() - b1 * x.mean()
y_est = b0 + b1 * x

print 'y = {:3f} {:+3f}x'.format(b0, b1)
x_bar = x.mean()
x_diff = (x - x_bar) ** 2
h = 1. / n + x_diff / x_diff.sum()

res = y - y_est

sse = np.sum(res ** 2)
mse = sse / (n - 2)

s = np.sqrt(mse)
s_res = s * np.sqrt(1 - h)

# a.
print 'a.'
res_std = res / s_res
print res_std
print '-' * 30

# b.
print 'b.'
plt.scatter(y_est, res_std)
plt.plot(y_est, np.zeros(n))
plt.show()
print '-' * 30
# c.
print 'c.'
plt.scatter(x, y)
plt.show()
