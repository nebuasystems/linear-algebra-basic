import sys
import os
import numpy as np
from pathlib import Path

try:
    print(os.path.join(Path(os.getcwd()).parent, 'lib'))    #이렇게 출력-> C:\Users\GX701GXR\PycharmProjects\linear-algebra-basic\lib 그런데 바로 넣으면 안됨. /나 \\로 해야함
    sys.path.append('C:/Users/GX701GXR/PycharmProjects/linear-algebra-basic/lib')
    #sys.path.append('..\lib')
    #sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    import common as cm
except ImportError:
    print('lib ??')

def f(v):
    return np.sum(v**2, axis=0)



print(cm.numerical_gradient(f, np.array([3., 4.])))