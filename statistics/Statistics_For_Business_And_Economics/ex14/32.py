import numpy as np 
from scipy import stats 


x = np.arange(5, dtype=np.float) + 1
y = np.array([3, 7, 5, 11, 14], dtype=np.float)
n = len(x)
alpha = 0.05
x_bar = x.mean()

sum_x = x.sum()
sum_y = y.sum()
sum_xx = (x ** 2).sum()
sum_xy = (x * y).sum()

b1 = sum_xy - (sum_x * sum_y) / n
b1 /= (sum_xx - sum_x ** 2 / n) 
b0 = y.mean() - b1 * x.mean()

print b0
print b1

y_est = b0 + b1 * x

xp = 4
yp_est = b0 + b1 * xp 

sse = np.sum((y - y_est) ** 2)
mse = sse / (n - 2)

adj = (xp - x_bar) ** 2
adj /= np.sum((x - x_bar) ** 2)

s_p_est2 = mse * (1.0 / n + adj)
s_p_est = np.sqrt(s_p_est2)

# a.
print 'a.'
print 's_p_est: {:3f}'.format(s_p_est)
print '-' * 30
# b.
print 'b.'
t = stats.t.isf(alpha / 2, n - 2)
print 'CI: [{:3f}, {:3f}]'.format(yp_est - t * s_p_est, yp_est + t * s_p_est)
print '-' * 30
# c.
print 'c.'
s_ind2 = mse + s_p_est2
s_ind = np.sqrt(s_ind2)
print 's_ind: {:3f}'.format(s_ind)
print '-' * 30
# d.
print 'd.'
t = stats.t.isf(alpha / 2, n - 2)
print 'CI: [{:3f}, {:3f}]'.format(yp_est - t * s_ind, yp_est + t * s_ind)
