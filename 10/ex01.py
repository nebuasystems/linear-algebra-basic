#최소제곱법(Method of Least Square)
import sys
import os
import numpy as np
from pathlib import Path

try:
    sys.path.append('C:/Users/GX701GXR/PycharmProjects/linear-algebra-basic/lib')
    from common import method_least_square
except ImportError:
    print('lib ??')

from matplotlib import pyplot as plt



#data
times = [2, 4, 6, 8]
score = [81, 93, 91, 97]

a, b = method_least_square(times, score)

print(f'직선 y = {a}x + {b}')

#predict
scores_predict = [(a * t) + b for t in times]
print(scores_predict)

fig, splt = plt.subplots()

splt.plot(times, scores_predict)
splt.scatter(times, score)

plt.show()