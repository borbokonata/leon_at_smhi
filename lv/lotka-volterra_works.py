import numpy as np
import matplotlib.pyplot as plt

a = 1.0
b = 0.1
c = 0.75
d = 0.075
dt = 0.001
n = 30000

x = np.zeros((n)) 
y = np.zeros((n)) 

x[0] = 5.0
y[0] = 5.0

x[1] = x[0] + (a * x[0] - b * x[0] * y[0]) * dt
y[1] = y[0] + d * x[0] * y[0] * dt - c * y[0] * dt 

T = np.linspace(0, n-1, n)
for t in range(n - 1):
    x[t+1] = x[t] + a * x[t] * dt - b * x[t] * y[t] * dt
    y[t+1] = y[t] + d * x[t] * y[t] * dt - c * y[t] * dt
print(x)
print(y)

plt.plot(T, x, label='rabbits', linestyle = 'dotted')
plt.plot(T, y, label='foxes', linestyle = 'solid')
plt.xlabel("time")
plt.ylabel("population")
plt.show()