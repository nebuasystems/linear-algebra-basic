#경사하강법(해석편미분)

import os
import sys
from pathlib import Path
try:
    sys.path.append('C:/Users/GX701GXR/PycharmProjects/linear-algebra-basic/lib')
    from common import mean_squares_error, gradient_descent
except ImportError:
    print('Library Module Can Not Found')
import numpy as np


def analytic_gradient(x, data_training):
    dx = np.zeros_like(x)

    n = len(data_training[0])
    data_y_hat = x[0] * data_training[0] + x[1]
    error = data_y_hat - data_training[1]

    dx[0] = (2/n) * np.sum(error * data_training[0])
    dx[1] = (2/n) * np.sum(error)

    return  dx

# data
times = [2, 4, 6, 8]
scores = [81, 93, 91, 97]

#경사하강법
x = np.array([0., 0.]) #시작데이타
lr = 0.01
epoch = 5000

for i in range(epoch):
    gradient = analytic_gradient(x, (np.array(times), np.array(scores)))

    print(f'epock={i+1}, gradient={gradient}, x={x}')

    x -= lr *gradient

a, b = tuple(x)
print(f'직선 y = {a}x + {b}')

print(f'오차(평균제곱오차):{mean_squares_error(np.array([a, b]), (times, scores))}')