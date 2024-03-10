# 01-lin_fit.py
# 线性拟合

import numpy as np
from numpy import linalg
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import reshape

# 设置刻度线朝内
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 16  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True

# 给定实验数据
# y=a+bx
x0 = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # 自变量
x = x0
# y = np.array([3.12, 4.92, 7.15, 8.92, 11.24, 12.76, 15.08, 17.28])  # 应变量

# y=a+bx**1.7
x = x0**1.7
y = np.array([5, 11.75, 21.42, 33.67, 48.28, 65.09, 84, 104.9])

# 计算法方程系数：
m = len(x)
a12 = a21 = sum(x)
a22 = sum(x**2)
A = np.mat([[m, a12], [a21, a22]])
b11 = sum(y)
b21 = sum(x * y)
b = np.mat([[b11], [b21]])
# 线性方程求解 Acoef=b
coef = linalg.solve(A, b)
print("一次拟合求解")
for i in range(len(coef)):
    print(f"a{i}={coef[i,0]:.5f}")
# 定义模型方程
def func(x, a0, a1):
    return a0 + a1 * x


# 绘制曲线
plt.figure(num="拟合曲线绘制", figsize=(8, 8))
plt.scatter(x0, y, color="red", label="实验数据")  # 绘制数据点
plt.xlabel("x", fontname="serif")
plt.ylabel("y", labelpad=5, fontname="serif")
ydata = np.zeros(m)
eer = 0
for i in range(m):  # 计算均方差
    ydata[i] = func(x[i], *coef)
    eer = eer + (ydata[i] - y[i]) ** 2
print(eer)
plt.plot(x0, ydata, label="拟合曲线", color="green", linewidth=2.0, linestyle="--")
plt.grid(which="both", axis="both", color="r", linestyle=":", linewidth=1)
# y=a+bx
# plt.text(0.2, 12, f"均方误差={eer:.5f}")
# plt.text(0.2, 13, f"拟合方程：y={coef[0,0]:.5f}+{coef[1,0]:.5f}x")
# y=a+bx**1.7
plt.text(0.2, 80, f"均方误差={eer:.5f}")
plt.text(0.2, 70, f"拟合方程：y={coef[0,0]:.5f}+{coef[1,0]:.5f}x^1.7")


plt.xlim(0, 9)  # 设置x轴范围
plt.legend()
plt.show()
