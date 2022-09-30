# 16-Parameter_BVP_ode.py
from tkinter import Y
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
mpl.rcParams["font.size"] = 48  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
font1 = {"family": "Times New Roman"}
tspan = np.linspace(1, 11, 101)  # 确定自变量范围
y_tspan = np.zeros((2, tspan.size))  # 确定应变量初值
# 定义微分方程,注意和程序08-bc_ode中的不同，自变量t放在前面
# a=1
def dy(t, y):  # 已知微分方程y1的两个端点值为40和80，但不知y2的开始端点值，注意和ode定义方程dy(y,t)的不同
    y1, y2 = y[0], y[1]
    dy1 = y2
    dy2 = 0.5 * t**0.8 * np.sin(t) * y1 + a * np.log(t)
    return np.vstack((dy1, dy2))


# 定义边界条件#
def BC(ya, yb):
    f1, f2 = 1, 8
    return np.array([ya[0] - f1, yb[0] - f2])
    # return np.array([20*ya[1]-f1*ya[0], 40*yb[0]-f2*yb[1]])
    # 可以其他边界条件，ya表示左边界，yb表示右边界，以bc=0的形式表示边界条件


tol = 10e-6  ##收敛精度
eer = 1  ##偏差初值
a1 = 1  ##a参数第一个假设值
a2 = 2  ##a参数第二个假设值

t = tspan
y_right = 5
# 计算一种假设情况下的右端点值
a = a1
sol = solve_bvp(dy, BC, tspan, y_tspan)
y = sol.sol(tspan)[0]
dyy = sol.sol(tspan)[1]
y1 = y
y2 = dyy
dy_2 = 0.5 * t**0.8 * np.sin(t) * y1 + a * np.log(t)
result1 = dy_2[-1]  ## 二阶导数右端点

# result1 = y2[-1]#### 一阶导数右端点
y_right1 = result1
# 计算另一种假设情况下的右端点值
a = a2
sol = solve_bvp(dy, BC, tspan, y_tspan)
y = sol.sol(tspan)[0]
dyy = sol.sol(tspan)[1]
y1 = y
y2 = dyy
dy_2 = 0.5 * t**0.8 * np.sin(t) * y1 + a * np.log(t)
result2 = dy_2[-1]  ## 二阶导数右端点
# result2 = y2[-1]  #### 一阶导数右端点
y_right2 = result2
# 产生新的插值点作为迭代计算起点
k = (a2 - a1) / (y_right2 - y_right1)
a_0 = a1 + k * (y_right - y_right1)
# print(c_0)
while eer >= tol:
    a = a_0
    sol = solve_bvp(dy, BC, tspan, y_tspan)
    y = sol.sol(tspan)[0]
    dyy = sol.sol(tspan)[1]
    y1 = y
    y2 = dyy
    dy_2 = 0.5 * t**0.8 * np.sin(t) * y1 + a * np.log(t)
    result = dy_2[-1]  ## 二阶导数右端点
    # result = y2[-1]  ## 一阶导数右端点
    eer = abs((y_right - result) / y_right)
    a_1 = a_0 + k * (y_right - result)
    a_0 = a_1
a = a_0
sol = solve_bvp(dy, BC, tspan, y_tspan)
y = sol.sol(tspan)[0]
dyy = sol.sol(tspan)[1]
y1 = y
y2 = dyy
dy_2 = 0.5 * t**0.8 * np.sin(t) * y1 + a * np.log(t)
# print("a=",a[0])
print("ddy_right=", dy_2[-1])
# print("y", y)
print("y_left=", y[0])
print("y_right=", y[-1])
print("a=", a)
print("dy_right=", y2[-1])
plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(tspan, y1, label="$y$", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(tspan, y2, label="$dy$", color="green", linewidth=2.0, linestyle="--")
plt.plot(tspan, dy_2, label="$d^2y$", color="blue", linewidth=2.0, linestyle="-.")
plt.xticks(np.linspace(0, 11, 12, endpoint=True))  # 设置横轴刻度
plt.xlim(0, 11)  # 设置x轴的上下限
x_text = 5.5
y_text = 100
str_a = "$a=$" + str(int(10000 * a) / 10000)
plt.text(x_text, y_text, str_a)
# plt.ylim(-120, 180)
plt.xlabel("$x$", font1, color="blue")  # 设置x轴描述信息
plt.ylabel("$y,dy,d^2y$", font1, color="red")  # 设置y轴描述信息
# plt.yticks(np.linspace(-120, 180, 16))  # 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.savefig("g:\\bvp_ode.png", dpi=72)  # 以分辨率 72 来保存图片
plt.show()  # 在屏幕上显示
