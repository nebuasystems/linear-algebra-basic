from inspect import signature


def f1(a):
    return a

def f2(a, b):
    return a+b

def test(f):
    param_count = len(signature(f).parameters)

    return param_count


print(test(f1))
print(test(f2))

def f3():
    print('f3')


def f4():
    print('f4')

a= 10
if a == 10:
    f3()
else:
    f4()


f3() if a == 10 else f4()


