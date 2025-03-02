# 04-optim_single库优化方法求解  Multiple
# （1）golden
# （2）fmin
# （3）minimize
# 0.21*x**4-2*x**3+5.5*x**2-6*x+5

from scipy import optimize
import scipy as scp
import numpy as np
import time

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  #


# 自定义优化函数
def func(x):
    return 0.21 * x**4 - 2 * x**3 + 5.5 * x**2 - 6 * x + 5


def funJ(x):  ##fitness
    a, b, c, d, e = 1, -3, 5, -7, 2
    f = (
        (x**2 + a**2) ** 0.5
        + ((x + b) ** 2 + c**2) ** 0.5
        + ((x + d) ** 2 + e**2) ** 0.5
    )
    return f


def funD(x):
    x1, x2, x3 = x[0], x[1], x[2]
    f = (
        (x1 - 2 * x2 * x3 - 8) ** 2
        + (x2 * x2 - x1 - x3**2 - 9) ** 2
        + (x3 + x1**2 - 8 * x1 - 12) ** 2
    )
    return f


# 黄金分割法
minf = optimize.golden(func, brack=(1, 3), full_output=True)  # full_output=True
print("golden_output=", minf[:])
x = np.linspace(1, 6, 51)
y = func(x)

plt.figure(num="黄金分割法")
plt.plot(x, y, lw=2, c="b")
plt.grid()
plt.xlabel("变量值")
plt.ylabel("优化函数值")
plt.annotate(
    "最优点",
    xy=(minf[0], minf[1]),
    xytext=(minf[0] + 0.5, minf[1] + 3.5),
    arrowprops=dict(arrowstyle="->", color="r", linewidth=2),
)
str1 = "x=" + str(minf[0])
str2 = "最优值=" + str(minf[1])
plt.text(minf[0] - 0.5, minf[1] + 2.5, str1)
plt.text(minf[0] - 0.5, minf[1] + 1.5, str2)


# fmin设置
minf = optimize.fmin(funJ, x0=5)
print("fmin_output_funJ:")
optim = minf[0]
minf = funJ(optim)
print(f"x={optim:.5f},minf={minf:.5f}")

x = np.linspace(1, 4, 31)
y = funJ(x)
plt.figure(num="fmin优化法")
plt.plot(x, y, lw=2, c="b")
plt.grid()
plt.xlabel("变量值")
plt.ylabel("优化函数值")
plt.annotate(
    "最优点",
    xy=(optim, minf),
    xytext=(optim + 0.5, minf + 0.4),
    arrowprops=dict(arrowstyle="->", color="r", linewidth=2),
)
str1 = "x=" + str(optim)
str2 = "最优值=" + str(minf)
plt.text(optim - 0.5, minf + 0.3, str1)
plt.text(optim - 0.5, minf + 0.2, str2)


# fmin全输出设置
minf = optimize.fmin(func, x0=5, full_output=True, retall=True)
print("fmin_output:\n", minf)

# 默认设置minimize_scalar
minf = optimize.minimize_scalar(func)
print("mini_scalar_output:")
optim = minf.x
minf = func(optim)
print(f"x={optim:.5f},minf={minf:.5f}")
# minimize函数优化单变量
res = optimize.minimize(func, [4], method="CG")
optim = res.x
minf = func(optim)
print(f"minimize_output:\nx={optim[0]:.5f},minf={minf[0]:.5f}")
print(f"res=\n{res}")
print("res.fun=", res.fun)
# minimize函数优化多变量
res = optimize.minimize(funD, [1, 1, 1], method="CG")
optim = res.x
minf = funD(optim)
print(f"minimize_output:\nx={optim},minf={minf}")
print(f"res=\n{res}")
print("res.fun=", res.fun)


plt.show()
