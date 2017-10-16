import numpy as np 
from scipy import stats

n_treatment = 3
n_sample = 6

alpha = 0.05
data = np.array([162,142,165,145,148,174,142,156,124,142,136,152,126,122,138,140,150,128], dtype=np.float)
data = data.reshape(n_treatment, n_sample)

x_bar_tot = data.sum() / data.size
x_bar_treatment = data.sum(axis=1) / n_sample
x_bar_sample = data.sum(axis=0) / n_treatment

print x_bar_tot
print x_bar_sample
print x_bar_treatment

# a.
print 'a.'
sstr = np.sum((x_bar_treatment - x_bar_tot) ** 2) * n_sample
print 'sstr: {:.3f}'.format(sstr)

# b.
print 'b.'
df_treatment = n_treatment - 1
mstr = sstr / df_treatment
print 'mstr: {:.3f}'.format(mstr)

# c.
print 'c.'
s_sample = np.std(data, axis=1, ddof=1)
sse = np.sum(s_sample ** 2) * (n_sample - 1)
print 'sse: {:.3f}'.format(sse)

# d.
print 'd.'
df_error = data.size - n_treatment
mse = sse / df_error
print 'mse: {:.3f}'.format(mse)

# f.
print 'f.'
F = mstr / mse

p = stats.f.sf(F, df_treatment, df_error)
print 'F: {:.2f}, p: {:.3f}'.format(F, p)
if p < alpha:
    print 'reject'
else:
    print 'do not reject'
