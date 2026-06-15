import numpy as np

# 0 = fail, 1 = pass
x = np.array([
    [2, 3],
    [1, 5],
    [6, 2],
    [7, 3],
    [8, 1],
    [3, 6],
], dtype=float)
y = np.array([0, 0, 1, 1, 1, 0], dtype=float)
x=np.c_[np.ones(len(x)),x]
weights=np.zeros(x.shape[1])
def sigmoid(z):
    return 1/(1+np.exp(-z))
lr=0.01
for epoch in range(1000):
    z=x@weights
    p=sigmoid(z)
    gradient=x.T@(p-y)/len(x)
    weights-=lr*gradient
    loss=-np.mean(y * np.log(p) + (1-y) * np.log(1-p))
    if loss>=0.5:
         print(1)
    else:
        print(0)
    if epoch %100==0:
        print(f"Epoch:{epoch},Loss:{loss}")