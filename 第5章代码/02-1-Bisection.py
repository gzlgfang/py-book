# 二分法bisection method
# 02-Bisection
import scipy as scp
import numpy as np
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细

# 自定义优化函数
# def func(t):
# return 225 * np.log(14 - 0.1 * t) / (130 - t) + 480 / (t - 30)


def func(x):  ##fitness
    a1, b1, c1, d1 = 2, 6, -5, 7
    f = ((x + a1) ** 2 + b1**2) ** 0.5 + ((x + c1) ** 2 + d1**2) ** 0.5
    return f


start_time = time.time()
# t1, t2, n = 32, 128, 0
# t1, t2, n = -5.5, -0.5, 0
t1, t2, n = 1.1, 1.7, 0

x_start, x_end = t1, t2
a0, b0 = t1, t2
beita = 0.005
eer1 = 0.000001
eer2 = 0.000001
flag = True
while flag:
    n = n + 1
    a = t1
    b = t2
    x1 = (a + b) / 2 - beita * (b - a)
    x2 = (a + b) / 2 + beita * (b - a)
    f1 = func(x1)
    f2 = func(x2)
    if f1 >= f2:
        t1 = x1
        e1 = abs((b - x1) / (a0 - b0))
        optim = x2
        minf = f2
    else:
        t2 = x2
        e1 = abs((b - x1) / (a0 - b0))
        optim = x1
        minf = f1
    e2 = abs(f2 - f1) / (1 + abs(f1))
    if e1 <= eer1 and e2 <= eer2:
        flag = False
print(f"t={optim:.8f},minf={minf:.8f},n={n}")
end_time = time.time()
print("程序运行计时", end_time - start_time)
x = np.linspace(x_start, x_end, 100)
y = func(x)
plt.figure(num="目标函数与优化区间变量关系图")
plt.plot(x, y, lw=2, c="b")
plt.grid()
plt.xlabel("变量值")
plt.ylabel("优化函数值")
plt.annotate(
    "最优点",
    xy=(optim, minf),
    xytext=(optim + 1, minf + 0.5),
    arrowprops=dict(arrowstyle="->", color="r", linewidth=2),
)
str1 = "x=" + str(optim)
str2 = "最优值=" + str(minf)jkjn,
plt.text(optim - 0.5, minf + 0.25, str1)
plt.text(optim - 0.5, minf + 0.15, str2)
plt.show()
