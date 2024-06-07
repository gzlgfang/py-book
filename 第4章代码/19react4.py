# 19-react4_ode.py
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
#
No = 0
# 定义方程
# y1,y2=c_A,c_B
def dy(y, t):
    y1, y2 = y[0], y[1]
    dy1 = -0.1 * y1 + 0.02 * y2
    dy2 = 0.15 * y1 - 0.06 * y2 - 0.01 * y2**2
    return [dy1, dy2]


y0 = [20 + 0.1 * No, 0]  # 确定初始状态
tspan = np.linspace(0, 100, 101)  # 确定自变量范围
sol = odeint(dy, y0, tspan)
for i in range(10):
    i = i
    print(
        "C_A(",
        i + 1,
        ")",
        "C_B(",
        i + 1,
        ")=",
        f"{sol[(i + 1) * 10, 0]:.3f}",
        "," f"{sol[(i + 1) * 10, 1]:.3f}",
    )
fig = plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(tspan, sol[:, 0], label=r"$c_{A}$", color="red", linewidth=3, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(
    tspan, sol[:, 1], label="$c_{B}$", color="green", linewidth=3.0, linestyle="-."
)

plt.xlim(0, 100)
plt.ylim(0, 20 + 0.1 * No)
plt.xticks()  # 设置横轴刻度
plt.xlabel("时间t,min", color="blue")  # 设置x轴描述信息
plt.ylabel("浓度" + r"$c,kmol/m^{3}$", color="red")  # 设置y轴描述信息
plt.yticks()  # 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.show()  # 在屏幕上显示
