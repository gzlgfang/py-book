#11-Wave_equa.py   波动方程
import xdrlib
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
mpl.rcParams["font.size"] = 16  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
font1 = {"family": "Times New Roman"}
t0 = 100.0 * np.ones((101, 101))  # 设置初始解为零
t0[100, :] = 300.0  # 设置右边界条件
t0[:, 100] = 300.0  # 设置上边界条件
t1 = 300.0 * np.ones((101, 101))  # 设置初始解为300
for i in range(101):
    t0[i, 0] = 30.0 + 270 * (i / 100.0) ** 4  # 设置下边界条件
    t0[0, i] = 30.0 + 270 * (i / 100.0) ** 4  # 设置左边界条件
    t1[i, 0] = 30.0 + 270 * (i / 100.0) ** 4  # 边界值迭代过程不变
    t1[0, i] = 30.0 + 270 * (i / 100.0) ** 4
x = np.arange(101) * 0.01  # 长度位置，归一处理，从0开始，共101个点
y = np.arange(101) * 0.01
X, Y = np.meshgrid(x, y)
k = 0
flag = True
while flag == True:
    k = k + 1
    for i in range(1, 100):  # 内部点迭代
        for j in range(1, 100):
            t1[i, j] = 0.25 * (
                t0[i - 1, j] + t0[i, j - 1] + t0[i + 1, j] + t0[i, j + 1]
            )  # 迭代计算
    if np.max(abs((t1 - t0) / t0)) <= 0.0001:
        flag = False
    t0[:, :] = t1[:, :]
    if k == 10000:  # 设置迭代次数上限
        flag = False

# print(t1)
print("k=", k)
print(t1[50, 50], t1[20, :])
print(type(t1))
print(type(t0))


norm = mpl.colors.Normalize(abs(t1).min(), abs(t1).max())
fig, ax = plt.subplots(1, 1, figsize=(8, 8))  # 布局设置
p = ax.pcolor(X, Y, t1, cmap=mpl.cm.jet, norm=norm, shading="auto")  # pcolor绘制
cb = plt.colorbar(p, ax=ax)
cb.set_label("温度")
ax.set_title("不同位置温度变化色图")
font1 = {"family": "Times New Roman"}
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0])  # 设置纵轴刻度
plt.xticks()
ax.set_xlabel("x", font1)
ax.set_ylabel("y", font1)
plt.show()
