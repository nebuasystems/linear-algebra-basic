import numpy as np

m1 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

m2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

v = np.array([10, 100])

m3 = m1 @ v
print(m3, m3.shape)

m4 = v @ m2
print(m4, m4.shape)