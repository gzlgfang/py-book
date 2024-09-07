# 03-golden method
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
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细


# 自定义优化函数
def funJ(t):
    return 225 * np.log(14 - 0.1 * t) / (130 - t) + 480 / (t - 30)


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


def Golden(funJ, eer1, eer2, start, alfai):
    """
    funJ      优化函数
    eer1      变量精度
    eer2      函数精度
    alfai     扫描步长
    start     扫描起点
    """
    start_time = time.time()
    Opt_inter = fast_scan(start, alfai)
    beita = 0.5 * (5**0.5 - 1)  # 黄金分割率
    a = Opt_inter[0]
    b = Opt_inter[1]
    x1 = a + (1 - beita) * (b - a)
    x2 = b - (1 - beita) * (b - a)
    f1 = funJ(x1)
    f2 = funJ(x2)
    flag = True
    n = 0
    a0, b0 = a, b
    while flag:
        n = n + 1
        if f1 >= f2:
            e1 = abs((b - x1) / (a0 - b0))
            optim = x2
            minf = f2
            e2 = abs(f2 - f1) / (1 + abs(f1))
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - (1 - beita) * (b - a)
            f2 = funJ(x2)
        else:
            optim = x1
            minf = f1
            e1 = abs((x2 - a) / (a0 - b0))
            e2 = abs(f2 - f1) / (1 + abs(f1))
            b = x2
            x2 = x1
            x1 = a + (1 - beita) * (b - a)
            f2 = f1
            f1 = funJ(x1)
        if e1 <= eer1 and e2 <= eer2:
            flag = False
    print(f"t={optim:.8f},minf={minf:.8f},n={n}")
    end_time = time.time()
    print("程序运行计时", end_time - start_time)
    x_start, x_end = a0, b0
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
        xytext=(optim + 5, minf + 3.5),
        arrowprops=dict(arrowstyle="->", color="r", linewidth=2),
    )
    str1 = "x=" + str(optim)
    str2 = "最优值=" + str(minf)
    plt.text(optim - 0.5, minf + 2.5, str1)
    plt.text(optim - 0.5, minf + 1.5, str2)
    plt.show()


# if __name__ == '__main__':
Golden(funJ, 10e-5, 10e-5, 32, 0.1)
