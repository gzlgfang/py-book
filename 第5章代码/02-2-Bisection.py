#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time

mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
start_time = time.time()


def Bisexhau(funJ, beita, eer1, eer2, start, alfai):
    """
    funJ      优化函数
    beita     中心偏离因子
    eer1      变量精度
    eer2      函数精度
    alfai     扫描步长
    start     扫描起点
    """

    Opt_inter = fast_scan(start, alfai)
    x_start = Opt_inter[0]
    x_end = Opt_inter[1]
    t1, t2 = x_start, x_end
    a0, b0 = x_start, x_end
    flag = True
    print("t1,t2=", t1, t2)
    n = 0
    while flag:
        n = n + 1
        a = t1
        b = t2
        x1 = (a + b) / 2 - beita * (b - a)
        x2 = (a + b) / 2 + beita * (b - a)
        f1 = funJ(x1)
        f2 = funJ(x2)
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
    y = funJ(x)
    plt.figure(num="目标函数与优化区间变量关系图")
    plt.plot(x, y, lw=2, c="b")
    plt.grid()
    plt.xlabel("变量值")
    plt.ylabel("优化函数值")
    plt.annotate(
        "最优点",
        xy=(optim, minf),
        xytext=(optim + 0.1, minf + 0.15),
        arrowprops=dict(arrowstyle="->", color="r", linewidth=2),
    )
    str1 = "x=" + str(optim)
    str2 = "最优值=" + str(minf)
    plt.text(optim - 0.05, minf + 0.10, str1)
    plt.text(optim - 0.05, minf + 0.05, str2)
    plt.show()


# 快速扫描法程序
def fast_scan(start, alfai):
    n = 1
    t1 = start
    f1 = funJ(t1)
    t2 = t1 + alfai * 2 ** (n - 1)
    f2 = funJ(t2)
    if f1 < f2:
        alfai = -alfai
        t2 = t1 + alfai * 2 ** (n - 1)
    while n < 1000:
        n = n + 1
        t3 = t2 + alfai * 2 ** (n - 1)
        f3 = funJ(t3)
        if f2 < f3:
            break
        else:
            t1 = t2
            f1 = f2
            t2 = t3
            f2 = f3
    return [t1, t3]


def funJ(x):  ##fitness
    a1, b1, c1, d1 = 2, 6, 5, 7
    f = ((x + a1) ** 2 + b1**2) ** 0.5 + ((-x + c1) ** 2 + d1**2) ** 0.5
    return f  # 求最大变成求最小，前面加负号，默认求最小


""" def funJ(x):  ##fitness
    a, b, c, d, e = 1, 3, 5, 7, 2
    f = (
        (x**2 + a**2) ** 0.5
        + ((x + b) ** 2 + c**2) ** 0.5
        + ((x + d) ** 2 + e**2) ** 0.5
    )
    return f  # 求最大变成求最小，前 """


# if __name__ == '__main__':
Bisexhau(funJ, 0.001, 10e-5, 10e-5, -1, 0.1)
