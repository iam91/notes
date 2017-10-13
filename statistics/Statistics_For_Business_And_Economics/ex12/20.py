import numpy as np 
from scipy import stats

alpha = 0.05
occur = np.arange(5)
f = np.array([39, 30, 30, 18, 3])
n = f.sum()

mu = np.sum(occur * f).astype(np.float) / f.sum()

# expected frequency
e = stats.poisson.pmf(occur, mu) * n
print e

# ex[4] = 3.89 < 5, thus adjust
f = np.append(f[:3], f[-2:].sum())
e = np.append(e[:3], e[-2:].sum())

df = len(f) - 1 - 1
chi2 = np.sum(((f - e) ** 2) / e)

p = 1 - stats.chi2.cdf(chi2, df)

print 'p: {:3f}, chi2: {:.2f}'.format(p, chi2)
if p < alpha:
    print 'is not poisson distribution'
else:
    print 'is poisson distribution'