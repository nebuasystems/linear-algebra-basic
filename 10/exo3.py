#경사하강법(수치미분)

import sys
import os
import numpy as np
from pathlib import Path

try:
    sys.path.append('C:/Users/GX701GXR/PycharmProjects/linear-algebra-basic/lib')
    from common import method_least_square
    from common import mean_square_error
    from common import gradient_descent_linear_regression
except ImportError:
    print('lib ??')

from matplotlib import pyplot as plt

#data
times = [2, 4, 6, 8]
score = [81, 93, 91, 97]

#경사하강법
result = gradient_descent_linear_regression(mean_square_error, np.array([0., 0.]), epoch=4000, data_training=(times, score))

print(result)