import numpy as np 
from scipy import stats 

x = np.array([3, 12, 6, 20, 14], dtype=np.float)
y = np.array([55, 40, 55, 10, 15], dtype=np.float)
alpha = 0.05
n = x.shape[0]

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

print y 
print y_est

# a.
print 'a.'
sse = np.sum((y - y_est) ** 2)
mse = sse / (n - 2)
print 'mse: {:3f}'.format(mse)
print '-' * 30
# b.
print 'b.'
s = np.sqrt(mse)
print 's: {:3f}'.format(s)
print '-' * 30
# c.
print 'c.'
s_b1 = s / np.sqrt(np.sum((x - x.mean()) ** 2))
print 's_b1: {:3f}'.format(s_b1)
print '-' * 30
# d.
print 'd.'
t = np.abs(b1 / s_b1)
p = stats.t.sf(t, (n - 2)) + stats.t.cdf(-t, (n - 2))
print 't: {:3f}, p: {:3f}'.format(t, p)
if p < alpha:
    print 'reject h0, sig'
else:
    print 'do not reject h0, insig'
print '-' * 30
# e.
print 'e.'
ssr = np.sum((y_est - y.mean()) ** 2)
msr = ssr / 1
F = msr / mse
p = stats.f.sf(F, 1, (n - 2))
print 'F: {:3f}, p: {:3f}'.format(F, p)
if p < alpha:
    print 'reject h0, sig'
else:
    print 'do not reject h0, insig'
