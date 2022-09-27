# 03-odeint.py
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

# a=2
# b=2
def dy(y, x):  # 注意是参数y在前面
    # ddy =y**2*np.cos(x)
    # ddy = a*np.cos(x)
    ddy = a * np.sin(3 * x) + 0.05 * x
    # ddy=np.cos(6*x)+0.8*np.sin(6*x)
    return ddy


# x = np.arange(10,-0.1, -0.1)  # 确定自变量范围,右边界
# x = np.arange(0,10.1, 0.1)  # 确定自变量范围,左边界
# x = np.arange(0,10.1, 0.1)  # 确定自变量范围

x = np.linspace(0, 10, 101)
y0 = 0  # 确定初始状态
y_left = 2
y_right = 6
tol = 10e-6
eer = 1
a1 = 1
a2 = 2
# 计算一种假设情况下的右端点值
a = a1
result1 = odeint(dy, y_left, x)
y_right1 = result1[-1]
# 计算另一种假设情况下的右端点值
a = a2
result2 = odeint(dy, y_left, x)
y_right2 = result2[-1]
# 产生新的插值点作为迭代计算起点
k = (a2 - a1) / (y_right2 - y_right1)
a_0 = a1 + k * (y_right - y_right1)
# print(c_0)
while eer >= tol:
    a = a_0
    result = odeint(dy, y_left, x)
    eer = abs((y_right - result[-1]) / y_right)
    a_1 = a_0 + k * (y_right - result[-1])
    a_0 = a_1
a = a_0
result = odeint(dy, y_left, x)
ddy = dy(result[:], x[:])
print("a=", a[0])
print("y_b=", result[-1])
# print(ddy[3:13])
# for i in range(int(len(x)/2)):
# print(f"x={2*(i+1)*0.05:.2f},y={result[2*(i+1)-1,0]:.5f}")
# print(result.T)
plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(x, result[:], label="y", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(x, ddy[:], label="dy/dx", color="green", linewidth=2.0, linestyle="--")
plt.xticks(np.linspace(0, 10, 11))
ymin = [min(result[:]), min(ddy[:])]
ymax = [max(result[:]), max(ddy[:])]
plt.ylim(min(ymin) - 1, max(ymax) + 1)  # 设置纵轴的上下限

plt.xlim(0, 10)  # 设置纵轴的上下限
aa = int(a[0] * 10000 + 0.5) / 10000
stra = str(aa)
stra = "a=" + stra
plt.text(4, 7, stra)

# plt.text(4,6,"dy=a*cos(x)")
plt.text(4, 8, "a*sin3x+0.05x")

plt.xlabel("x", color="blue")  # 设置x轴描述信息
plt.ylabel("y,dy", color="red")  # 设置y轴描述信息
plt.yticks(np.linspace(-8, 10, 19))  # 设置纵轴刻度# 设置纵轴刻度
plt.legend()
plt.grid(True)


plt.annotate(
    "y_a=y_left",
    xy=(0, y_left),
    xytext=(2, y_left - 3),
    bbox=dict(facecolor="w", alpha=1, edgecolor="r", lw=2),
    arrowprops=dict(arrowstyle="->", color="r", lw=2),
)


plt.annotate(
    "y_b=y_right",
    xy=(10, y_right),
    xytext=(7, y_right - 3),
    bbox=dict(facecolor="w", alpha=1, edgecolor="b", lw=2),
    arrowprops=dict(arrowstyle="->", color="b", lw=2),
)

plt.title("两点边值问题")
plt.savefig("g:\\odeint_03.png", dpi=72)  # 以分辨率 72 来保存图片


plt.figure(figsize=(8, 6), dpi=80)
x = np.arange(10, -0.1, -0.1)  # 确定自变量范围,右边界
# x = np.arange(0,10.1, 0.1)  # 确定自变量范围,左边界
a = 2
y0 = 0
result = odeint(dy, y0, x)
ddy = dy(result[:], x[:])
plt.plot(x, result[:], label="y", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(x, ddy[:], label="dy/dx", color="green", linewidth=2.0, linestyle="--")
plt.xticks(np.linspace(0, 10, 11))
ymin = [min(result[:]), min(ddy[:])]
ymax = [max(result[:]), max(ddy[:])]
plt.ylim(min(ymin) - 1, max(ymax) + 1)  # 设置纵轴的上下限

plt.xlim(0, 10)  # 设置纵轴的上下限
stra = str(a)
# stra="a="+stra
# plt.text(4,3,stra)
# plt.text(4,2,"dy=a*cos(x)")
plt.text(4, 3, "2sin3x+0.05x")
plt.xlabel("x", color="blue")  # 设置x轴描述信息
plt.ylabel("y,dy", color="red")  # 设置y轴描述信息
plt.yticks(np.linspace(-4, 4, 9))  # 设置纵轴刻度# 设置纵轴刻度
plt.legend()
plt.grid(True)

plt.annotate(
    "y_b=y_0",
    xy=(10, y0),
    xytext=(8, y0 - 3),
    bbox=dict(facecolor="w", alpha=1, edgecolor="b", lw=2),
    arrowprops=dict(arrowstyle="->", color="b", lw=2),
)


plt.title("右端点确定问题")


plt.figure(figsize=(8, 6), dpi=80)

x = np.arange(0, 10.1, 0.1)  # 确定自变量范围,左边界，
a, y0 = 2, 0  # 赋值微分方程系数及初值
result = odeint(dy, y0, x)  # 用odeint求解方程得y
ddy = dy(result[:], x[:])


plt.plot(x, result[:], label="y", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(x, ddy[:], label="dy/dx", color="green", linewidth=2.0, linestyle="--")
plt.xticks(np.linspace(0, 10, 11))
ymin = [min(result[:]), min(ddy[:])]
ymax = [max(result[:]), max(ddy[:])]
plt.ylim(min(ymin) - 1, max(ymax) + 1)  # 设置纵轴的上下限

plt.xlim(0, 10)  # 设置纵轴的上下限
stra = str(a)
stra = "a=" + stra
# plt.text(4,3,stra)
# plt.text(4,2,"dy=a*cos(x)")
plt.text(4, 3, "2sin3x+0.05x")
plt.xlabel("x", color="blue")  # 设置x轴描述信息
plt.ylabel("y,dy", color="red")  # 设置y轴描述信息
plt.yticks(np.linspace(-4, 4, 9))  # 设置纵轴刻度# 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.annotate(
    "y_a=y_0",
    xy=(0, y0),
    xytext=(2, y0 - 3),
    bbox=dict(facecolor="w", alpha=1, edgecolor="b", lw=2),
    arrowprops=dict(arrowstyle="->", color="b", lw=2),
)
plt.title("左端点确定问题")


plt.show()  # 在屏幕上显示
