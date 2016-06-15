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

def img_average(train_data,train_id):
    A = np.zeros((10,256))
    id_len = train_id.size
    count = np.zeros((1,10))
    for s in range(id_len):
        pos = train_id[s]
        A[pos-1,:] += train_data[s,:]
        count[0][pos-1] += 1
    for t in range(10):
        A[t,:] = A[t,:]/count[0][t]
    return A

def square_least(r_A,test_data,test_id):
    id_len = test_id.size
    diff = np.zeros((10,256))
    correct = 0
    for x in range(id_len):
        diff = np.linalg.norm(r_A[0,:] - test_data[x,:])
        num = 0
        for y in range(1,10):
            diff_v = np.linalg.norm(r_A[y,:] - test_data[x,:])
            if diff > diff_v:
                diff = diff_v
                num = y
        if test_id[x] == num+1:
            correct += 1
    return (correct/id_len)*100

result = img_average(train_data,train_id)
pca = square_least(result,test_data,test_id)
print(pca)
