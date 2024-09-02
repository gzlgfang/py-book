#!/usr/bin/env python3
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


def Exhau(funJ, N, Pc, start, alfai):
    """
    funJ  优化函数
    N     区间等分数
    PC    收缩率，Percentage of contraction
    """
    # alfai = 0.1
    # start = 1
    global a, b, c, d, e
    a, b, c, d, e = 1, 3, 5, 7, 2
    flag = True
    temp, k = 1, 0
    while flag:
        temp = temp * 1 / N
        k = k + 1
        if temp <= Pc:
            flag = False
    Opt_inter = fast_scan(start, alfai)
    x_start = Opt_inter[0]
    x_end = Opt_inter[1]
    t1, t2 = x_start, x_end
    f = np.ones(N + 1)
    for m in range(k):  # 进行k轮穷举
        t = np.linspace(t1, t2, N + 1)
        for i in range(N + 1):  # 每轮穷举N等分
            f[i] = funJ(t[i], a, b, c, d, e)
        fmin = min(f[:])  # 确定最小值
        index = list(f[:]).index(min(f[:]))  # 确定最小值所在的位置
        t1 = t[index - 1]  # 重新设置t1
        t2 = t[index + 1]
    optim = t[index]
    minf = funJ(t[index], a, b, c, d, e)

    print(f"t={optim:.8f},minf={minf:.8f}")
    x = np.linspace(x_start, x_end, 100)
    y = funJ(x, a, b, c, d, e)

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
    str2 = "最优值=" + str(minf)
    plt.text(optim - 0.5, minf + 0.25, str1)
    plt.text(optim - 0.5, minf + 0.15, str2)
    plt.show()


# 快速扫描法程序
def fast_scan(start, alfai):
    n = 1
    t1 = start
    f1 = funJ(t1, a, b, c, d, e)
    t2 = t1 + alfai * 2 ** (n - 1)
    f2 = funJ(t2, a, b, c, d, e)
    if f1 < f2:
        alfai = -alfai
        t2 = t1 + alfai * 2 ** (n - 1)
    while n < 1000:
        n = n + 1
        t3 = t2 + alfai * 2 ** (n - 1)
        f3 = funJ(t3, a, b, c, d, e)
        if f2 < f3:
            break
        else:
            t1 = t2
            f1 = f2
            t2 = t3
            f2 = f3
    return [t1, t3]


def funJ(x, a, b, c, d, e):  ##fitness
    f = (
        (x**2 + a**2) ** 0.5
        + ((x + b) ** 2 + c**2) ** 0.5
        + ((x + d) ** 2 + e**2) ** 0.5
    )
    return f  # 求最大变成求最小，前面加负号，默认求最小


# if __name__ == '__main__':
Exhau(funJ, 100, 10e-6, 1, 0.1)
