import sys
import os

try:
    sys.path.append('C:/Users/GX701GXR/PycharmProjects/linear-algebra-basic/lib')
    from common import numerical_diff
    from common import numerical_partial_diff
except ImportError:
    print('lib ??')

# 수치미분 (Numerical Diffirentiation)
# 이차함수 y=20(x-2)^2 + 500

def f(x):
    return 20*(x-2)**2+500


import numpy as np


print(f'Diffirentiation Value:{numerical_diff(f, np.array([2.]))}')
print(f'Diffirentiation Value:{numerical_partial_diff(f, np.array([1.9]))}')    #이곳의 f는 단일 변수