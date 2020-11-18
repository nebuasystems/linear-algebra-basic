import sys
import os
import numpy as np
from pathlib import Path

try:
    sys.path.append('C:/Users/GX701GXR/PycharmProjects/linear-algebra-basic/lib')
    from common import gradient_descent
except ImportError:
    print('lib ??')


def f(x):
    return np.sum(x**2, axis=0)

gradient_descent(f, np.array([-3., 4.]), lr=0.1)
#gradient_descent(f, np.array([-3., 4.]), lr=0.001,epoch=10000)