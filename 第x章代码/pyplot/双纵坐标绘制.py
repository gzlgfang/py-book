import matplotlib.ticker as mticker
import matplotlib
import numpy as np
# import time
import matplotlib.pyplot as plt
from pylab import *  # 调用mpl
mpl.rcParams['font.sans-serif'] = ['Times New Roman']
matplotlib.rcParams['font.family'] = 'sans-serif'
# 中文设置成宋体，除此之外的字体设置成New Roman
matplotlib.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'

# 均值、标准差、shape,100可以修改为288
flow = np.random.normal(200, 50, 288)
speed = np.random.normal(30, 12, 288)
# 为了显示24个刻度
x = np.arange(0, 24, 24/288)
# 自定义字体
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 19,
         }
fig, ax1 = plt.subplots(figsize=(14, 6))
# 设置第一纵坐标轴的单位
ax1.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d km/h'))
# 自定义横轴
ax1.set_xticklabels([str(i)+':00' for i in range(0, 25, 2)],
                    rotation=0, fontsize='x-large')  # fontproperties=myfont
# 设置横轴 特定x值时显示刻度
ax1.set_xticks([i for i in range(0, 25, 2)])

ax1.tick_params(labelsize=17)
plt.plot(x, speed, 'r', label="traffic speed")
# 显示网格
plt.grid(True)
plt.xlabel("time", font1)
plt.ylabel('traffic speed', font1)
#plt.title("This is double axis label")
# 设置线标的位置
plt.legend(loc='upper left')

# 第二纵轴的设置和绘图
ax2 = ax1.twinx()
plt.plot(x, flow, 'g', label="traffic flow")
plt.legend(loc='upper right')
ax2.tick_params(labelsize=17)
ax2.set_ylabel("traffic flow", font1)
# 限制横轴显示刻度的范围
plt.xlim(0, 24)
plt.show()
