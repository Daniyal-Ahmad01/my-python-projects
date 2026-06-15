import numpy as np
x=np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
actual = np.array([3, 7, 11, 15])
weights = np.zeros(3)
lr=0.01
x=np.c_[np.ones(4),x]

for epoch in range(1000):
    pred=x @ weights
    error=pred-actual
    mse=np.mean(error**2)

    gradient=x.T@error
    weights -= lr*gradient/len(x)
    print(weights)