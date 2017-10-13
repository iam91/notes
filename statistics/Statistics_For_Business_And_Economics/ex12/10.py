import numpy as np 
from scipy import stats 

alpha = 0.05 
contingency = np.asarray(np.c_[
    [20, 30, 20],
    [30, 60, 25],
    [10, 15, 30]
], dtype=np.float)

print contingency

category = contingency.sum(0)
var_tot = np.vstack(contingency.sum(1))

prob = category / category.sum() 

e = var_tot * prob 

df = (contingency.shape[0] - 1) * (contingency.shape[1] - 1)
chi2 = ((contingency - e) ** 2) / e
chi2 = chi2.sum()

p = 1 - stats.chi2.cdf(chi2, df)

print 'p: {:.3f}, chi2: {:.2f}'.format(p, chi2)
if p < alpha:
    print 'reject'
else:
    print 'do not reject'