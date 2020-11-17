import numpy as np



x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

v = np.diag(x)

print(v)

m = np.eye(3, 3, k=0)
print(m)

y = np.identity(3)
print(y)

print(np.arange(1,10).shape)