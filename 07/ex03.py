#편미분 설명 - x0, x1에 대한 미분
import sys
import os
import numpy as np

try:
    sys.path.append('C:/Users/GX701GXR/PycharmProjects/linear-algebra-basic/lib')
    from common import numerical_partial_diff
except ImportError:
    print('lib ??')

#y = x0**2 + x1**2
# f(x0, x1):
def f(x):
    return x[0]**2 + x[1]**2

#(x0 ,x1) = (2, 4)
print(f'Diffirentiation Value:{numerical_partial_diff(f, np.array([2, 4]))}')

#(x0 ,x1) = (3, 1)
print(f'Diffirentiation Value:{numerical_partial_diff(f, np.array([3, 1]))}')

#(x0 ,x1) = (8, 2)
print(f'Diffirentiation Value:{numerical_partial_diff(f, np.array([8, 2]))}')