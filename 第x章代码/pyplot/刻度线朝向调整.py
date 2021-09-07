import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname='G:\Fonts\simhei.ttf', size=20)
# 不同电脑字体安装位置不同
x = np.linspace(0, 10*np.pi, 1000)
# y = 2 * x * np.sin(np.power(x,1.8)) + 20
y = np.zeros(1000)
for i in range(1000):
    y[i] = 2 * x[i] * np.sin(np.power(x[i], 1.8)) + 20

# 坐标轴的刻度设置向内(in)或向外(out)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
# 画图
plt.plot(x, y)
# 设置背景网格线为虚线
plt.grid(linestyle="-")
# 设置坐标轴标签
plt.xlabel("时间/s", fontproperties=myfont)
plt.ylabel("峰高/(cm)", fontsize=18, fontproperties="SimSun")
# 显示图像
plt.show()
