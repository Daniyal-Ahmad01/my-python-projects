import numpy as np

x = np.array([10, 20, 30, 40])     # units consumed
y = np.array([50, 100, 150, 200]) # actual prices

weight = 0.1
lr = 0.001

for step in range(50):
    pred = weight * x                  # prediction
    error = pred - y                   # error
    gradient = np.mean(error * x)      # gradient
    weight = weight - lr * gradient    # update

    if step % 10 == 0:
        print(f"step {step}: weight={weight:.4f} {error}")
