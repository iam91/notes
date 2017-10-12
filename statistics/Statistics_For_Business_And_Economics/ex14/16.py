import numpy as np 

x = np.array([3, 12, 6, 20, 14])
y = np.array([55, 40, 55, 10, 15])
y_est = 68 - 3 * x 

y_mean = np.mean(y)

# a
sse = np.sum((y - y_est) ** 2)
sst = np.sum((y - y_mean) ** 2)
ssr = np.sum((y_est - y_mean) ** 2)

print 'a.'
print 'sse: {:f}, sst: {:f}, ssr: {:f}'\
    .format(sse, sst, ssr)
print '-' * 30

# b
r2 = float(ssr) / sst 
print 'b.'
print 'r2: {:f}'.format(r2)
print '-' * 30

# c
n = len(x)

x_mean = np.mean(x)

sigma_x = np.sum((x.astype(np.float) - x_mean) ** 2) / (n - 1)
sigma_x = np.sqrt(sigma_x)
sigma_y = np.sum((y.astype(np.float) - y_mean) ** 2) / (n - 1)
sigma_y = np.sqrt(sigma_y)
cov_xy = np.sum((x.astype(np.float) - x_mean) * (y.astype(np.float) - y_mean)) / (n - 1)

rel = cov_xy / (sigma_x * sigma_y)

print 'c.'
print 'rel: {:f}, rel2: {:f}, r2: {:f}'.format(rel, rel ** 2, r2)