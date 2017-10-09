import numpy as np 

data = np.array([4, 2, 3, 5, 6, 3, 5, 7, 7, 6, 6, 8])

n_quarter = 4
n_year = 3

########## a. ##########
# quarter moving average
mv_aver = []
for i in range(n_quarter * (n_year - 1) + 1):
    mv_aver.append(np.mean(data[i:i + n_quarter]))
mv_aver = np.array(mv_aver)

# centered moving average
cent_mv_aver = []
for i in range(len(mv_aver) - 1):
    cent_mv_aver.append(np.mean(mv_aver[i:i + 2]))
cent_mv_aver = np.array(cent_mv_aver)
print 'a. '
print 'quarter moving average: ' + str(mv_aver)
print 'centered moving average: ' + str(cent_mv_aver)
print '-' * 30

########## b. ##########
# deseasonalize
deseasonalized = []
for i, d in enumerate(cent_mv_aver):
    deseasonalized.append(data[2 + i] / d)
print deseasonalized

quarters = [3, 4, 1, 2]
seasonal_index = range(4)
for i in range(4):
    sum = 0.0
    quarter = quarters[i]
    for j in range(2):
        sum += deseasonalized[i + j * n_quarter]
    seasonal_index[quarter - 1] = sum / 2
print 'b. '
print 'seasonal index: ' + str(seasonal_index)