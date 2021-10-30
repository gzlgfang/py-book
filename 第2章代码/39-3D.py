import matplotlib.pyplot as plt
#from matplotlib import *
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()

# 指定图形类型是 3d 类型
ax = fig.add_subplot(projection='3d')

# 构造数据
X = np.arange(-1.5, 1.5, 0.01)
Y = np.arange(-1.5, 1.5, 0.01)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)/R+np.exp((np.cos(2*np.pi*X)+np.cos(2*np.pi*Y))/2)-np.exp(1)
#Z=30+X**2 + Y**2-10*(np.cos(2*np.pi*X)+np.cos(2*np.pi*Y))
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# Customize the z axis.
#ax.set_zlim(0, 100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
