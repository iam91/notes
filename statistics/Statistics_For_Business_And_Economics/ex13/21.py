import numpy as np 
from scipy import stats

n_treatment = 3
n_block = 5
n_tot = 3 * 5

df_treatment = n_treatment - 1
df_block = n_block - 1
df_err = df_treatment * df_block
df_tot = n_tot - 1

alpha = 0.05
data = np.array([10,12,18,20,8,9,6,15,18,7,8,5,14,18,8], \
    dtype=np.float)
data = data.reshape(n_treatment, n_block)

x_bar_tot = data.sum() / n_tot
x_bar_treatment = data.sum(axis=1) / n_block
x_bar_block = data.sum(axis=0) / n_treatment

sst = np.sum((data - x_bar_tot) ** 2)
sstr = n_block * np.sum((x_bar_treatment - x_bar_tot) ** 2)
ssbl = n_treatment * np.sum((x_bar_block - x_bar_tot) ** 2)
sse = sst - sstr - ssbl

mstr = sstr / df_treatment
mse = sse / df_err

F = mstr / mse

p = stats.f.sf(F, df_treatment, df_err)

print 'sst: {:.2f}, sstr: {:.2f}, ssbl: {:.2f}, sse: {:.2f}'\
    .format(sst, sstr, ssbl, sse)
print 'mstr: {:.2f}, mse: {:.2f}'.format(mstr, mse)
print 'F: {:.2f}, p: {:.3f}'.format(F, p)
if p < alpha:
    print 'reject'
else:
    print 'do not reject'