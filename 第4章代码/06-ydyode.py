# 06-ydyode.py
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# 设置刻度线朝内
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 48  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
font1 = {"family": "Times New Roman"}


def dy(y, t):
    y1, y2 = y[0], y[1]
    dy1 = y2
    dy2= t**2*np.cos(t)+y1*np.sin(t)
    #dy2 = 5 * np.sin(t) - 2 * np.cos(t) * t * np.exp(0.001 * y1)

    return [dy1, dy2]


y0 = [0, 1]  # 确定初始状态
tspan = np.linspace(0, 30, 301)  # 确定自变量范围
sol = odeint(dy, y0, tspan)
t=tspan
y1=sol[:, 0]
y2=sol[:, 1]
#ddy=5 * np.sin(t) - 2 * np.cos(t) * t * np.exp(0.001 * y1)
ddy=t**2*np.cos(t)+y1*np.sin(t)
#print(ddy)
plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(tspan, y1, label="y", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(tspan, y2, label="dy", color="green", linewidth=2.0, linestyle="--")
plt.plot(tspan, ddy, label="ddy", color="blue", linewidth=2.0, linestyle="-.")
plt.xticks(np.linspace(0, 30, 16, endpoint=True))  # 设置横轴刻度
plt.xlim(0, 30)  # 设置x轴的上下限
# plt.ylim(0,200)
plt.xlabel("x", font1, color="blue")  # 设置x轴描述信息
plt.ylabel("y,dy,ddy", color="red")  # 设置y轴描述信息
plt.yticks()  # 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.savefig("g:\\ydyode_06.png", dpi=72)  # 以分辨率 72 来保存图片
plt.show()  # 在屏幕上显示
