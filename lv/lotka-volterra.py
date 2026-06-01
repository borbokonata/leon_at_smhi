from turtle import color

import numpy as np
import matplotlib.pyplot as plt

a = 1.0

b = 0.1
c = 0.75
d = 0.075
dt = 0.001
#t is time
n = 10000

x = np.zeros((n))  #rabbbit population
y = np.zeros((n))  #fox population

x[0] = 5.0
y[0] = 5.0

#rabbit    x(t + dt) = x(t) + ( α x − βxc )dt

#fox        y(t + dt) = y(t) + (-cy + dxy)dt

T=[]
T.append(0)
for t in range(n - 1):
    x[t+1] = x[t] + a * x[t] * dt - b * x[t] * y[t] * dt
    y[t+1] = y[t] + d * x[t] * y[t] * dt - c * y[t] * dt
    T.append(t)
print(x)
print(y)

#T is vertical and represents time, x/y is horizontal and represents the population
plt.plot(T, x, label='rabbits', linestyle = 'dotted')

plt.plot(T, y, label='foxes', linestyle = 'solid')

#labels
plt.xlabel("time")
plt.ylabel("population")
plt.grid()
plt.show()

print("hello world")