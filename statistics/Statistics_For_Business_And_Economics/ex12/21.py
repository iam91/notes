import numpy as np 
from scipy import stats

alpha = 0.05
x = np.array([17,21,23,18,22,15,24,24,19,23,23,23,18,43,22,29,20,27,13,26,11,30,21,28,18,33,20,23,21,29])

x_bar = np.mean(x)
s = np.std(x, ddof=1)

cuts = stats.norm.ppf(np.arange(1, 6) * (1.0 / 6), x_bar, s)

x_neg_inf = np.min([x.min(), cuts.min()])
x_pos_inf = np.max([x.max(), cuts.max()])

lower = np.vstack(np.append(np.array([x_neg_inf]), cuts))
higher = np.vstack(np.append(cuts, np.array([x_pos_inf])))

bins = [(tuple(bin), 0) for bin in np.hstack((lower, higher))]
bins = dict(bins)


for data in x:
    for bin in bins:
        if data >= bin[0] and data < bin[1]:
            bins[bin] += 1

f = np.array(bins.values())
e = np.ones(6) * 5

chi2 = np.sum(((f - e) ** 2) / e)
df = 6 - 2 - 1
p = 1 - stats.chi2.cdf(chi2, df)

print f
print e

print 'p: {:.3f}, chi2: {:.2f}'.format(p, chi2)
if p < alpha:
    print 'is not normal'
else:
    print 'is normal'