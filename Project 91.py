import numpy as np
a=np.array([
    [5,4],
    [6,7],
    [4,5],
    [7,8]
])
a=np.c_[np.ones(len(a)),a]
y=np.array([0,1,0,1])
weights=np.zeros(a.shape[1])
lr=0.01
def sigmoid(z):
    return 1/(1+np.exp(-z))
for epoch in range(1000):
    z=a@weights
    p=sigmoid(z)
    loss=-np.mean(y*np.log(p) + (1-y) * np.log(1-p))
    gradient=a.T @ (p-y)/len(a)
    weights-=lr*gradient
    if epoch %100==0:
        print(f"Epoch:{epoch}\tLoss:{loss}")
print(weights)