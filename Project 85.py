import numpy as np

a = np.array([4, 3, 5])          # features
weights = np.array([7.0, 5.0, 10.0])
actual = 30
lr = 0.01

for step in range(15):
    pred = np.dot(a, weights)     # recompute prediction
    error = pred - actual         # recompute error
    weights = weights - lr * error * a  # correct update

    print(f"step {step}: pred={pred:.2f}, error={error:.2f}, weights={weights}")
