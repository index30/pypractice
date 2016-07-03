import numpy as np
import scipy as sp
import scipy.io
import matplotlib.pyplot as plt

fea_data = scipy.io.loadmat("./USPS.mat")['fea']
gnd_data = scipy.io.loadmat("./USPS.mat")['gnd']

train_data = fea_data[1:1707,:]
train_id = gnd_data[1:1707]
test_data = fea_data[7292:7292+2006,:]
test_id = gnd_data[7292:7292+2006]

n = 6
find_num = [i for i, x in enumerate(train_id) if x == n]
temp = train_data[find_num[0],:]
for s in range(1,len(find_num)):
    temp = np.vstack((temp,train_data[find_num[s],:]))
A = temp.transpose()
U,s,V = np.linalg.svd(A)

plt.imshow(U[:,0].reshape((16,16)),cmap='Greys_r')
plt.show()
