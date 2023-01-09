# 18-react3_ode.py
from tkinter import N
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
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
mpl.rcParams["font.size"] = 28  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
font1 = {"family": "Times New Roman"}
# 反应速率常数, L/min
global k
k = np.array([0.3, 0.05])


def dy(y, t):
    y1, y2 = y[0], y[1]
    dy1 = 0.5 * k[1] * y2**2 - k[0] * y1
    dy2 = 2 * k[0] * y1 - k[1] * y2**2
    return [dy1, dy2]


No = 0
y0 = [10 + No, 0]  # 确定初始状态
tspan = np.linspace(0, 5, 11)  # 确定自变量范围
##确定条件下求解微分方程组：
fig = plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
sol = odeint(dy, y0, tspan)
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(tspan, sol[:, 0], label=r"$c_{A}$", color="red", linewidth=3, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(
    tspan, sol[:, 1], label="$c_{B}$", color="green", linewidth=3.0, linestyle="-."
)
TC = sol[:, 0] + sol[:, 1]
plt.plot(tspan, TC, label="$T_{c}$", color="k", linewidth=3.0, linestyle=":")
MAX_C_B = max(sol[:, 1])  # 确定最大值
time1 = 0.5 * list(sol[:, 1]).index(MAX_C_B)  # 确定最大值所在的位置,即反应时间点
str_cb = "最佳反应时间" + str(time1) + "min"
plt.text(2.5, 6, str_cb)
plt.annotate(
    f"最高点{MAX_C_B:.5f}",
    xy=(time1, MAX_C_B),
    xytext=(time1 - 1.5, MAX_C_B + 0.8),
    arrowprops=dict(arrowstyle="->", color="r", lw=2.5),
)
plt.xlim(0, 5)
plt.ylim(0, 16)
plt.xticks()  # 设置横轴刻度
plt.xlabel("反应时间t,min", color="blue")  # 设置x轴描述信息
plt.ylabel("浓度" + r"$c,kmol/m^{3}$", color="red")  # 设置y轴描述信息
plt.yticks()  # 设置纵轴刻度
print(sol[:, 0])
print(sol[:, 1])
##关键物质浓度
plt.grid(True)
plt.legend()
# plt.savefig("g:\\recat_ode_18.png", dpi=72)  # 以分辨率 72 来保存图片
plt.show()  # 在屏幕上显示
