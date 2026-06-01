import numpy as np
import matplotlib.pyplot as plt

#coordiantes

a = np.linspace(0, 2 * np.pi, 100)
b = np.linspace (0, np.pi, 50)
c, b = np.meshgrid(a, b)
#theta, phi 
r = 1

num_points = 1
a_points = np.random.uniform(0, 2 * np.pi, num_points)
b_points = np.random.uniform(0, np.pi, num_points)

x_points = r * np.sin(b_points) * np.cos(a_points)
y_points = r * np.sin(b_points) * np.sin(a_points)
z_points = r * np.sin(b_points) 

#radius


#covert coordinates!?!

x = r * np.sin(b) * np.cos(a)
y = r * np.sin(b) * np.sin(a)
z = r * np.cos(b)

#?
#figure?
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection ='3d')
ax.plot_surface(x, y, z, cmap='gist_earth_r', alpha=0.6)
ax.scatter(1.5+x_points, 1.5+y_points, 1.5+z_points, c='grey', s= 4000)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(' 3d sphere attempt')
ax.set_box_aspect((1, 1, 1))
plt.show()
