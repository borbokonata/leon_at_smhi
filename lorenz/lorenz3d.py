import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

a = 28
b = 10
c = 8/3
dt = 0.01
n = 10000

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
fig = plt.figure()
ax = fig.add_subplot(projection ='3d')
ax.view_init(elev=20, azim=120)
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_zlim(np.min(z), np.max(z))

#three lines
#plt.plot(T, x, label='the rate of fluid flow', linestyle = 'solid')
#plt.plot(T, y, label='temperature difference betweem the rising and falling air currents', linestyle = 'solid')
#plt.plot(T, z, label='distortion of the vertical temperature profile from a linear one', linestyle = 'solid')
artists = []
#for t in range(n):
#  if t == 0:
#    container1, = ax.plot(x[0], y[0], z[0], marker='o')
#    artists.append([container1])
#  else:
#    container1, = ax.plot(x[t-1], y[t-1], z[t-1], marker='o')
#    container2, = ax.plot(x[0:t], y[0:t], z[0:t], color = 'k', linestyle = 'solid')
#    artists.append([container1, container2])
t=n
ax.plot(x[0:t], y[0:t], z[0:t], color = 'k', linestyle = 'solid')


#ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=1)
plt.show()
#ani.save("lorenz.mp4")
