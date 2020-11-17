# y = ax + b 일차 방정식 결정하기

from matplotlib import pyplot as plt

data_x = [2, 6]
data_y = [81, 91]

a = (data_y[1] - data_y[0]) / (data_x[1] - data_x[0])
b = data_y[0] - a*data_x[0]

print(f'직선 y = {a}x + {b}')

fig, splot = plt.subplots()
splot.plot(data_x, data_y)



x = [2, 4, 6, 8]
y1 = [81, 93, 91, 97]
y2 = [a * i + b for i in x]
splot.scatter(x, y1)
splot.plot(x, y2, 'r-')


plt.show()