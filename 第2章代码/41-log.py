import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
#设置刻度线朝内
#plt.rcParams['xtick.direction'] = 'in'
#plt.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["FangSong"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 18#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
#normal	默认值，正常体
#italic	斜体，这是一个属性
#oblique 将字体倾斜，将没有斜体变量（italic）的特殊字体，要应用oblique

fig, axes = plt.subplots(1, 3, figsize=(3, 12))
x = np.linspace(1, 1e2, 1000)
y1, y2 = x**2.5, x**4
axes[0].set_title('对数-对数')
axes[0].loglog(x, y1, 'm', x, y2, 'b')

axes[1].set_title('半对数')
axes[1].semilogy(x, y1, 'b', x, y2, 'r')

axes[2].set_title('坐标轴比例对数设置')
axes[2].plot(x, y1, 'm', x, y2, 'b')
axes[2].set_xscale('log')
axes[2].set_yscale('log')
plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.show()
