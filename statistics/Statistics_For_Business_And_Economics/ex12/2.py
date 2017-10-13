import numpy as np 
from scipy import stats 

alpha = 0.05
prob = np.ones(4) * 0.25
f = np.array([85, 95, 50, 70])

e = f.sum() * prob
df = len(f) - 1

chi2 = np.sum(((f - e) ** 2) / e)
p = 1. - stats.chi2.cdf(chi2, df)

print 'p: {:.3f}, chi2: {:.2f}'.format(p, chi2)
if p < alpha:
    print 'reject'
else:
    print 'do not reject'