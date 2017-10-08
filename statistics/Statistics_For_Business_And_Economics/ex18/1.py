import numpy as np

# data
data = np.array([8, 13, 15, 17, 16, 9])

# a.
print 'a.'
len = 3
preds = []
for i in range(3, 7):
    pred = np.mean(data[i - 3: i])
    preds.append(pred)
    print str(i + 1) + ': ' + str(pred)
print '-' * 30
preds = np.array(preds)

# b.
print 'b.'
mse = np.mean((data[3:] - preds[0:-1]) ** 2)
print 'mse: ' + str(mse)
print '-' * 30

# c
print 'c.'
alpha = 0.2
preds = []

pred = data[0]
for i, dat in enumerate(data):
    pred = pred + alpha * (dat - pred)
    preds.append(pred)
    print str(i + 1) + ': ' + str(pred)
print '-' * 30
preds = np.array(preds)

# d
print 'd.'
mse = np.mean((data[1:] - preds[0:-1]) ** 2)
print 'mse: ' + str(mse)
print '-' * 30

# e
print 'e.'
alpha = 0.4
preds = []

pred = data[0]
for i, dat in enumerate(data):
    pred = pred + alpha * (dat - pred)
    preds.append(pred)
    print str(i + 1) + ': ' + str(pred)
preds = np.array(preds)
mse = np.mean((data[1:] - preds[0:-1]) ** 2)
print 'mse: ' + str(mse)
print '-' * 30

