import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

x = np.arange(0, 50, 0.1)
y = np.sin(x)
z = np.cos(x)

ax = plt.axes(projection="3d")
ax.plot(x, y) # , z)
ax.set_title("3D Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
# ax.set_zlabel("Z")
plt.show() 

ax = plt.axes(projection="3d")
ax.plot(x, y, z)
ax.set_title("3D Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show() 

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, Z, cmap="Spectral")
ax.set_title("Surface Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show() 

# heads_tails = [0, 0]
# for _ in range(1000000):
#     heads_tails[random.randint(0, 1)] += 1
#     plt.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])
#     plt.pause(0.001)
# plt.show() 

