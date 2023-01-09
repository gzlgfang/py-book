# 16-BVP_ode.py
from re import T
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_bvp

# 设置刻度线朝内
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 24  # 4设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
font1 = {"family": "Times New Roman"}
tspan = np.linspace(0, 10, 21)  # 确定自变量范围
y_tspan = np.zeros((2, tspan.size))  # 确定应变量初值
# 定义微分方程,注意和程序08-bc_ode中的不同，自变量t放在前面
global no
no = 50


def dy(t, y):  # 已知微分方程y1的两个端点值为40和80，但不知y2的开始端点值，注意和ode定义方程dy(y,t)的不同
    y1, y2 = y[0], y[1]
    dy1 = y2
    # dy2 = -0.002 * y1 * np.sin(5 * t) + 0.02 * (y1 - 340) * y2 + 0.01 * no

    dy2 = -0.003 * y1 * np.sin(10 * t) + 0.02 * (y1 - 340) * y2 + 0.02 * no
    # dy2 = 2 * (y1 - 200)
    return np.vstack((dy1, dy2))


# 定义边界条件#
def BC(ya, yb):
    f1, f2 = 350, 450 + no
    return np.array([ya[0] - f1, yb[0] - f2])
    # return np.array([20*ya[1]-f1*ya[0], 40*yb[0]-f2*yb[1]])
    # 可以其他边界条件，ya表示左边界，yb表示右边界，以bc=0的形式表示边界条件


sol = solve_bvp(dy, BC, tspan, y_tspan)
y = sol.sol(tspan)[0]
dy_1 = sol.sol(tspan)[1]
# dy_2 = y * np.sin(y) + (y - 300) * dy_1 + 0.1 * no * y**0.12
# dy_2 = 0.01 * y * np.sin(y) + 0.2 * (y - 340) * dy_1 + 0.1 * no
plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(tspan, y, label="y", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(tspan, dy_1, label="dT/dt", color="green", linewidth=2.0, linestyle="--")
# plt.plot(tspan, dy_2, label="$d^2T/dt^2$", color="blue", linewidth=2.0, linestyle="-.")

plt.xticks(np.linspace(0, 10, 21, endpoint=True))  # 设置横轴刻度
plt.xlim(0, 10)  # 设置x轴的上下限
# plt.ylim(320, 500)
plt.xlabel("t", font1, color="blue")  # 设置x轴描述信息
plt.ylabel("T,dT/dt", font1, color="red")  # 设置y轴描述信息
plt.yticks()  # 设置纵轴刻度np.linspace(-120, 180, 16)
plt.legend()
plt.grid(True)
# plt.savefig("g:\\16_bvp_ode.png", dpi=72)  # 以分辨率 72 来保存图片
print("T=", y)
plt.show()  # 在屏幕上显示
