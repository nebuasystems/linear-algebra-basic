import sys
import os
import numpy as np

try:
    sys.path.append('C:/Users/GX701GXR/PycharmProjects/linear-algebra-basic/lib')
    from common import numerical_partial_diff
except ImportError:
    print('lib ??')

# 수치미분(Numerical Diffierentiation) VS 해석미분(Analytic Diffierentiation)

def f(x):
    return 20*(x-2)**2+500


def analytic_diff(x):
    return 40 * x - 80



print(f'Numerical Diffirentiation Value:{numerical_partial_diff(f, np.array([5., 9]))}')
print(f'Analytic Diffirentiation Value:{analytic_diff(5)}')