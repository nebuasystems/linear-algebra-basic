#최소제곱법(Method of Least Square) 시험
import sys
import os
import numpy as np
from pathlib import Path

try:
    sys.path.append('C:/Users/GX701GXR/PycharmProjects/linear-algebra-basic/lib')
    from common import method_least_squares
    from common import mean_squares_error
except ImportError:
    print('lib ??')

from matplotlib import pyplot as plt



#data
times = [2, 4, 6, 8]
scores = [81, 93, 91, 97]

a, b = method_least_squares(times, scores)

print(f'직선 y = {a}x + {b}')

print(f'오차(평균제곱오차):{mean_squares_error(np.array([a, b]), times, scores)}')

# predict
scores_predict = [(a * t) + b for t in times]
print(scores_predict)

# 그래프
fig, splt = plt.subplots()
splt.scatter(times, scores)
splt.plot(times, scores_predict)
plt.show()