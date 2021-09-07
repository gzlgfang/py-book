import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

plt.rcParams['xtick.direction'] = 'in'  # 坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
# mpl.use('qt4agg')
t = np.linspace(0, 10, 2000)
y = 4*t**1.3*abs(np.sin(t**1.23))/(1+t)
plt.plot(t, y, 'r', lw=3, alpha=0.6)
plt.ylim(0, y[-1])
fx_ticks = np.arange(0, 11, 0.5)
plt.xticks(fx_ticks)
plt.xlim(0, t[-1])
ax = plt.gca()
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
plt.grid(True)
plt.show()
