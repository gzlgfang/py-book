# 05-uvode.py
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
mpl.rcParams["font.size"] = 24  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细


def dy(y, t):
    y1, y2 = y[0], y[1]
    dy1 = 0.1 * y1 * (1 - y1 / 20) - 0.35 * y1 * y2
    dy2 = 0.05 * y2 * (1 - y2 / 15) - 0.15 * y1 * y2
    return [dy1, dy2]


y0 = [1.6, 1.2]  # 确定初始状态
tspan = np.linspace(0, 300, 301)  # 确定自变量范围
sol = odeint(dy, y0, tspan)

plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(tspan, sol[:, 0], label="u", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(tspan, sol[:, 1], label="v", color="green", linewidth=2.0, linestyle="--")
plt.xticks(np.linspace(0, 300, 31, endpoint=True))  # 设置横轴刻度
plt.xlim(0, 300)  # 设置x轴的上下限
# plt.ylim(0,1.6)
plt.xlabel("时间", color="blue")  # 设置x轴描述信息
plt.ylabel("物种数量，(u，v)", color="red")  # 设置y轴描述信息
plt.yticks()  # 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.savefig("g:\\uvode_05.png", dpi=72)  # 以分辨率 72 来保存图片
plt.show()  # 在屏幕上显示
