from turtle import color

import numpy as np
import matplotlib.pyplot as plt

a = 0.66
b = 1.3
c = 1
d = 1
dt = 0.001
#t is time
n = 10000

x = np.zeros((n))  #rabbbit population
y = np.zeros((n))  #fox population

x[0] = 0.9
y[0] = 1.8

#rabbit    x(t + dt) = x(t) + ( α x − βxc )dt

x[1] = x[0] + a * x[0] * dt - b * x[0] * y[0] * dt

#fox y(t + dt) = y(t) + (-cy + dxy)dt

y[1] = y[0] + d * x[0] * y[0] * dt - c * y[0] * dt 

T=[]
T.append(0)
for t in range(n - 1):
    x[t+1] = x[t] + a * x[t] * dt - b * x[t] * y[t] * dt
    y[t+1] = y[t] + d * x[t] * y[t] * dt - c * y[t] * dt
    T.append(t)
#print(x)
#print(y)






plt.plot(T, x, linestyle = 'dotted')

            
plt.plot(T, y, linestyle = 'solid')



plt.xlabel("time")
plt.ylabel("population")
plt.show()
