import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

a = 28
b = 10
c = 8/3
dt = 0.01
n = 5000

x = np.zeros((n))           #the rate of fluid flow
y = np.zeros((n))           #the temperture between the rising and falling air currentents
z = np.zeros((n))          #the distortion of the vertical temperature profile from a linear one



#"prognostic" equations
#x(t + dt) = x(t) + b(y - x)dt
#y(t + dt) = y(t) + (ax - y -xz)dt
#z(t + dt) = z(t) + (xy -cz)dt 

x[0] = 0
y[0] = 10
z[0] = 0



#x[1] = x[0] + b * (y[0] - x[0]) * dt
#y[1] = y[0] + (a * x[0] - y[0] - x[0] * z[0]) * dt
#z[1] = z[0] + (x[0] * y[0] - c * z[0]) * dt 

T = np.linspace(0, n-1, n)
for t in range (n - 1):
  x[t+1] = x[t] + b * (y[t] - x[t]) * dt
  y[t+1] = y[t] + (a * x[t] - y[t] - x[t] * z[t]) * dt
  z[t+1] = z[t] + (x[t] * y[t] - c * z[t]) * dt 

#??

#make 3d

x2 = np.zeros((n))           #the rate of fluid flow
y2 = np.zeros((n))           #the temperture between the rising and falling air currentents
z2 = np.zeros((n))          #the distortion of the vertical temperature profile from a linear one


x2[0] = 0.000001
y2[0] = 10
z2[0] = 0


T = np.linspace(0, n-1, n)
for t in range (n - 1):
  x2[t+1] = x2[t] + b * (y2[t] - x2[t]) * dt
  y2[t+1] = y2[t] + (a * x2[t] - y2[t] - x2[t] * z2[t]) * dt
  z2[t+1] = z2[t] + (x2[t] * y2[t] - c * z2[t]) * dt 

















#three lines
plt.plot(T, x, label='the rate of fluid flow', linestyle = 'solid')
plt.plot(T, y, label='temperature difference betweem the rising and falling air currents', linestyle = 'solid')#plt.plot(T, z, label='distortion of the vertical temperature profile from a linear one', linestyle = 'solid')
fix = plt.figure()
fig, axs = plt.subplots(3)
axs[0].plot(T, x, 'blue', label='rabbits', linestyle = 'solid', linewidth = 3)
axs[0].plot(T, x2, 'blue', label='rabbits', linestyle = 'dotted', linewidth = 3)

axs[1].plot(T, y, 'green', label='rabbits', linestyle = 'solid', linewidth = 3)
axs[1].plot(T, y2, 'green', label='rabbits', linestyle = 'dotted', linewidth = 3)

axs[2].plot(T, z, 'red',label='rabbits', linestyle = 'solid', linewidth = 3)
axs[2].plot(T, z2, 'red',label='rabbits', linestyle = 'dotted', linewidth = 3)

#artist = []



#t=n
#ax.plot(x[0:t], y[0:t], z[0:t], color = 'k', linestyle = 'solid')


#ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=1)


plt.show()

fig, axs = plt.subplots(3)
axs[0].axhline(y=0, color='gray', linestyle='-')
axs[0].plot(T, x-x2, 'blue', label='rabbits', linestyle = 'solid')
axs[1].axhline(y=0, color='gray', linestyle='-')
axs[1].plot(T, y-y2, 'green', label='rabbits', linestyle = 'solid')
axs[2].axhline(y=0, color='gray', linestyle='-')
axs[2].plot(T, z-z2, 'red',label='rabbits', linestyle = 'solid')

plt.show()
