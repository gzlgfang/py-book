import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='G:\Fonts\simhei.ttf', size=20)
# 不同电脑字体安装位置不同
x = np.linspace(0, 10, 1000)

y = 2 * x * np.sin(x) + 20

xx = [x[0], x[0], x[-1], x[-1]]
yy = [0, y[0], y[-1], 0]


# 填充范围
x3 = np.zeros(1004)
y3 = np.zeros(1004)

x3[0] = x[0]
x3[1] = x[0]
y3[0] = 0
y3[1] = y[0]

for i in range(1000):
    x3[i+2] = x[i]
    y3[i+2] = y[i]

x3[1002] = x[-1]
x3[1003] = x[-1]
y3[1002] = y[-1]
y3[1003] = 0


N = 10000
dx = 10/N
area = 0

for i in range(10000):
    x0, x1 = i*dx, (i+1)*dx
    area = area+(2*x0*np.sin(x0)+20+2*x1*np.sin(x1)+20)/2*dx


# 绘图

plt.title('填充图绘制', FontProperties=font)
plt.xlabel('时间，time（s)', FontProperties=font)
plt.ylabel('色谱柱高度，h(mm)', FontProperties=font)

plt.plot(x, y, 'r', alpha=0.6)  # 设置线条的样式和颜色

# plt.fill(x,y,c='r',alpha=0.9) # 简答填充
# plt.fill(xx,yy,c='b',alpha=0.9) #填充的效果不一样

plt.fill(x3, y3, c='b', alpha=0.9)  # x轴和函数y之间的填充，数据比较复杂一点

plt.plot(x3, y3, 'r', linewidth=3, alpha=0.6)
ax = plt.gca()  # 为调用网格属性准备
ax.grid(True)

plt.xlim(0, 10)
plt.ylim(0, 40)

s = str(area)

plt.text(4, 35, s, size=16)
plt.text(2, 35, '面积=', FontProperties=font)


plt.show()
