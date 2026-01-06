
import numpy as np

movie = np.array([
    [1, 2, 2.5],
    [0, 5, 4],
    [0, 0, 2.5]
])

weight = np.array([9, 7, 5])

print(np.dot(movie, weight))
