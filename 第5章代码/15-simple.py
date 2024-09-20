# 单纯形法优化
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time
import copy

mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
start_time = time.time()


def Simple(funJ, h, alfa, miue, lamda, eer, n):
    """
    funJ      优化函数
    n         函数维度
    h         高度
    alfa      映射系数
    miue      扩张系数
    lamda     压缩系数
    eer       设定误差
    """
    n = int(n)
    # print(type(n))
    # 得到初始单纯形n+1个点
    U = rect_simple(n, h)  ##n=3,h=0.5;kkx相当与U
    # print(U)
    y = []  # 计算n+1个顶点的值
    for i in range(n + 1):
        y.append(funJ(U[i]))

    flag = True
    num = 0
    while flag:
        # 目标函数排序
        y = []  # 计算n+1个顶点的值
        for i in range(n + 1):
            y.append(funJ(U[i]))
        # print("uu=", U)
        kk, jj = paixu(U, y)
        # print("KKK=", kk, jj)

        ##补充U=KK
        fL = jj[0]  # 最小
        UL = kk[0]
        U[1 : n - 1] = kk[1 : n - 1]
        y[1 : n - 1] = jj[1 : n - 1]
        fM = jj[n - 1]  # 次大
        UM = kk[n - 1]
        fH = jj[n]
        UH = kk[n]  # 最大
        # 找到最小、次大、最大三点
        # print(fL,UL,fM,UM,fH,UH)
        # 计算重心
        num = num + 1
        if num >= 300:
            flag = False
        if abs((fL - fH) / (fH + 0.5)) < eer and (abs(UL[0] - UH[0])) < eer:
            flag = False

        UC = (sum(kk) - UH) / n
        # print(UC)
        # 进行映射
        UR = UC + alfa * (UC - UH)
        fR = funJ(UR)
        # print(fR)
        if fR < fM:
            UE = UR + miue * (UR - UH)
            fE = funJ(UE)
            if fE < fR:
                UH = UE
                U[n] = UH
                continue
            else:
                UH = UR
                U[n] = UH
                continue
        else:
            US = UH + lamda * (UR - UH)
            fS = funJ(US)
            if fS < fM:
                UH = US
                U[n] = UH
                continue
            else:
                U[0] = UL
                U[1 : n - 1] = (U[1 : n - 1] + UL) / 2
                U[n - 1] = (UM + UL) / 2
                U[n] = (UH + UL) / 2
                continue
    print(U[0])
    print("优化目标=", y[0])
    print("优化次数=", num)


# 图形绘制,#全局设置字体


def rect_simple(n, h):  ##生成初始单纯形
    x0 = np.ones((n + 1, n))
    for i in range(n + 1):
        if i > 0:
            x0[i][i - 1] = x0[i][i - 1] + h
    return x0


def paixu(x, y):  # 数据排序从小到大按y序列为准
    for i in range(len(y) - 1):
        for j in range(i + 1, len(y)):
            if y[i] > y[j]:
                tempy = y[i]
                y[i] = y[j]
                y[j] = tempy
                tempx = copy.deepcopy(x[i][:])  ##不能简单赋值，否则数据将穿透
                x[i][:] = x[j][:]
                x[j][:] = tempx
    xx = x
    yy = y
    return xx, yy


def funJ(x):  ##fitness
    x1, x2, x3 = x[0], x[1], x[2]
    f = ((x1 - 9) ** 2 + (x2 - 7) ** 2) ** 0.5 + ((x3 - 5) ** 2) ** 0.5
    return f  # 求


Simple(funJ, 0.8, 1, 0.65, 0.75, 10e-6, 3)
