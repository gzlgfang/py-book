# 08-heat_trans.py
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.shape_base import _hvdsplit_dispatcher
from scipy.integrate import odeint
import math

# 设置刻度线朝内
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 24  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
font1 = {"family": "Times New Roman"}
t = np.zeros((2001, 202))  # 设置初始解为零
t[:, 0] = 30  # 设置边界条件
t[0, :] = 30  # 设置初始值
TW = 150  # 设置蒸汽温度
# print(t[0,:])
x = np.arange(202) * 0.01  # 长度位置，归一处理，从0开始，共102个点，终端外引入1点
t_time = np.arange(2001) * 0.001  # 计算时间，步长0.001
X, Y = np.meshgrid(x, t_time)
for n in range(0, 2000):
    for j in range(1, 201):
        t[n + 1, j] = 0.002 * TW + 0.698 * t[n, j] + 0.3 * t[n, j - 1]  # 迭代计算
    t[n + 1, 201] = t[n + 1, 200]  # 边界处一阶偏导为零处理
norm = mpl.colors.Normalize(abs(t).min(), abs(t).max())
fig, ax = plt.subplots(1, 1, figsize=(16, 8))  # 布局设置
p = ax.pcolor(X, Y, t, cmap=mpl.cm.RdBu, norm=norm, shading="auto")  # pcolor绘制
cb = plt.colorbar(p, ax=ax)
cb.set_label("温度")
ax.set_title("不同时间不同位置温度变化色图")
font1 = {"family": "Times New Roman"}
plt.yticks(np.linspace(0.1, 2, 20))  # 设置纵轴刻度
ax.set_xlabel("x", font1)
ax.set_ylabel("time", font1)
fig, ax = plt.subplots(1, 1, figsize=(16, 8))
ax.plot(x, t[200, :], label="time=0.2", color="green", linewidth=2.0, linestyle="--")
ax.plot(x, t[500, :], label="time=0.5", color="red", linewidth=2.0, linestyle="-")
ax.plot(x, t[800, :], label="time=0.8", color="blue", linewidth=2.0, linestyle="-.")
plt.xlabel("长度," + r"$x$", color="blue")  # 设置x轴描述信息
plt.ylabel("温度，t(°C)", color="red")  # 设置y轴描述信息
plt.yticks(np.linspace(40, 150, 12))  # 设置纵轴刻度
plt.xlim(0, 2)
plt.ylim(30, 150)
plt.legend()
plt.grid(True)
plt.show()
