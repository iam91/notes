import numpy as np 

from scipy import stats

x = np.arange(5, dtype=np.float) + 1
y = np.array([3, 7, 5, 11, 14], dtype=np.float)
n = len(x)
alpha = 0.05

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
de = np.sqrt(np.sum((x - x.mean()) ** 2))
s_b1 = s / de   
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
    print 'sig'
else:
    print 'insig'