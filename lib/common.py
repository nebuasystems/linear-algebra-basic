import numpy as np

def numerical_gradient(f, x):
    h = 1e-4
    gradient = np.zeros_like(x)


    for i in range(x.size):
        tmp = x[i]

        x[i] = tmp + h
        h1 = f(x)

        x[i] = tmp - h
        h2 = f(x)

        gradient[i] = (h1 - h2) / (2 * h)

        x[i] = tmp

    return gradient

def gradient_descent(f, x, lr=0.01, epoch=100):
    for i in range(epoch):
        gradient = numerical_gradient(f, x)

        print(f'epoch={i+1}, gradient={gradient}, x={x}')

        x -= lr * gradient
    return x

def method_least_square(x, y):
    mx = sum(x)/len(x)
    my = sum(y)/len(y)

    s1 = 0
    s2 = 0

    s1 = sum([(i - mx)*(j - my) for i, j in zip(x, y)])
    s2 = sum([(i - mx)**2 for i in x])


    mls_a = s1 / s2
    mls_b = my - (mx * mls_a)

    return mls_a, mls_b