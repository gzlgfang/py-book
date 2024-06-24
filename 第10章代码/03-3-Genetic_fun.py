#!/usr/bin/env python3
# 03-3-Genetic algorithm  for fun_problem
import numpy as np
from numpy.core.numeric import tensordot
import pandas as pd
import random as rnd
import time

# 绘图设置
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
##输入参数
D = 3  # 变量维数
lb, ub = 0, 1.0  # 变量上下限
N = 120  # 二进制数据长度
ZQS = 100
Maxgen = 300
Pc = 0.5  # 交叉概率
Pm = 0.2  # 变异概率
Sel_ra = 0.7  # 选择率


def Bin_pop(ZQS, N):  # 产生初始变量二进制数种群
    li = np.zeros(N)
    LJ = np.zeros((ZQS, N))
    for i in range(ZQS):
        for j in range(N):
            li[j] = np.fix(0.5 + np.random.random())
        LJ[i, :] = li
    return LJ.astype(int)  # 需要强制转变成整数


LJ = Bin_pop(ZQS, N)
# print("LJ=",LJ)
def Change2_10(LJ, lb, ub, D):  # 二进制转化为10进制，能区分变量数目及上下限
    ZQS, N = LJ.shape  # 二进制数组大小
    var2_num = int(N / D)  # 每个变量的二进制数编码长度
    X = np.zeros((ZQS, D))
    for i in range(ZQS):
        for j in range(D):
            temp0 = 0  #
            temp1 = 0
            for k in range(var2_num):
                temp0 = temp0 + 2 ** (var2_num - k - 1) * LJ[i, j * var2_num + k]
                temp1 = temp1 + 2**k
            temp0 = lb + temp0 / temp1 * (ub - lb)
            X[i, j] = temp0
    return X


# X=Change2_10(LJ, lb, ub, D)
# print("X=",X)
## 计算函数值
def funv(X):  ##X
    x1 = X[:, 0]
    x2 = X[:, 1]
    x3 = X[:, 2]
    """ Y = (
        (x1**1.2 + x1**0.5 * x2**0.9 + x2 * x3**0.9 - 0.8) ** 2
        + (x1**0.8 + x2**1.2 * x3 + x1 * x3**1.1 - 0.8) ** 2
        + (x1 * x2 * 1.1 + x2 * x3 + x3**1.5 - 0.8) ** 2
    ) """
    Y = (
        (x1**0.8 + x1 * x2**0.7 + x3**0.8 - 1) ** 2
        + (x1**1.2 * x2 + x2**0.9 * x3 + x1**0.5 - 1) ** 2
        + (x1 + x2**0.4 * x3**0.5 + x3**1.2 - 1) ** 2
    )

    return Y + 1  ##加1后，达到最优时，目标函数值为1


# print("FV=",FV)
# 计算适应度值fitness 归一化处理
def fit(FV):
    ZQS = len(FV)
    fitnv = np.ones(ZQS)
    fitnv[:] = 1 / FV[:]
    max = np.max(fitnv)
    min = np.min(fitnv)
    fitnv[:] = (fitnv[:] - min) / (max - min)
    return fitnv


# print("fitnv=",fitnv)

# 打印初始种群最优解
X = Change2_10(LJ, lb, ub, D)
FV = funv(X)
fitnv = fit(FV)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到适用度值最大即三个方程的平方和最小解
pre_obj = FV[index] - 1
pre_X = X[index]
print("pre_obj=", pre_obj)
print("pre_X=", pre_X)
##选择操作
def select(LJ, Sel_ra, fitnv):
    ZQS = len(LJ)
    sel_num = int(ZQS * Sel_ra)
    n = 0
    index = []
    flags = True
    while flags:
        for i in range(ZQS):
            pick = rnd.random()
            if pick < fitnv[i]:
                index.append(i)
                n = n + 1
                if n == sel_num:
                    break
        if n == sel_num:
            flags = False
    Sel_LJ = LJ[index]
    return Sel_LJ


##Sel_LJ = select(LJ, Sel_ra, fitnv)
# print("Sel_LJ=",Sel_LJ)
# print("目标函数取最小值时的自变量优位置= [0.34194738 0.4310146  0.54625798])")
# 交叉
def cross(a, b):
    # a和b为两个待交叉的个体
    # 输出：
    # a和b为交叉后得到的两个个体
    n = len(a)  # 城市数目
    flags = True
    while flags:
        r1 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
        r2 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
        if r1 != r2:
            flags = False
    # 保证找到两个不同整数，可以进行交叉操作
    a0 = np.zeros(n)
    b0 = np.zeros(n)
    a0[:] = a[:]
    b0[:] = b[:]
    if r1 > r2:
        s, e = r2, r1
    else:
        s, e = r1, r2
    for i in range(s, e + 1):
        a[i] = b0[i]
        b[i] = a0[i]
    return [a, b]


# 交叉重组
def Re_com(Sel_LJ, Pc):
    n = len(Sel_LJ)
    for i in range(0, n - 1, 2):
        # print(i)
        if Pc >= rnd.random():  #%交叉概率Pc
            [Sel_LJ[i, :], Sel_LJ[i + 1, :]] = cross(Sel_LJ[i, :], Sel_LJ[i + 1, :])
    return Sel_LJ


""" Sel_LJ = Re_com(Sel_LJ, Pc)
# 交叉重组后的最优解
X=Change2_10(Sel_LJ, lb, ub, D)
FV=funv(X)
fitnv=fit(FV)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到适用度值最大即三个方程的平方和最小解
cro_obj = FV[index]-1
cro_X=X[index]
print("cro_obj=",cro_obj)
print("cro_X=",cro_X) """


def Mutate(Sel_LJ, Pm):
    ZQS, n = Sel_LJ.shape
    for i in range(ZQS):
        if Pm >= rnd.random():
            r = np.random.randint(n, size=4)
            r.sort()  # 产生4个不相等的0到n-1的整数
            r_min = r[0]
            r_mid = r[1]
            r_max = r[2]
            if abs(Sel_LJ[i, r_min] - 1) <= 0.1:
                Sel_LJ[i, r_min] = 0
            else:
                Sel_LJ[i, r_min] = 1
            if abs(Sel_LJ[i, r_mid] - 1) <= 0.1:
                Sel_LJ[i, r_mid] = 0
            else:
                Sel_LJ[i, r_mid] = 1
            if abs(Sel_LJ[i, r_max] - 1) <= 0.1:
                Sel_LJ[i, r_max] = 0
            else:
                Sel_LJ[i, r_max] = 1
            if abs(Sel_LJ[i, r[3]] - 1) <= 0.1:
                Sel_LJ[i, r[3]] = 0
            else:
                Sel_LJ[i, r[3]] = 1
    return Sel_LJ


""" Sel_LJ = Mutate(Sel_LJ, Pm)  # 变异后的路径
#变异后的最优解
X=Change2_10(Sel_LJ, lb, ub, D)
FV=funv(X)
fitnv=fit(FV)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到适用度值最大即三个方程的平方和最小解
Mut_obj = FV[index]-1
Mut_X=X[index]
print("Mut_obj=", Mut_obj)
print("Mut_X=", Mut_X) """

# 逆转操作
def Reverse(Sel_LJ, fitnv):
    ZQS, n = Sel_LJ.shape
    Sel_LJ = np.array(Sel_LJ)
    Sel_LJ1 = np.copy(Sel_LJ)
    for i in range(ZQS):
        flags = True
        while flags:
            r1 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
            r2 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
            if r1 != r2:
                flags = False
        if r1 > r2:
            r_min, r_max = r2, r1
        else:
            r_min, r_max = r1, r2
        if r_min == 0:
            r_min = 1
        # print(r_min,r_max)
        Sel_LJ1[i, r_min : r_max + 1] = Sel_LJ[i, r_max : r_min - 1 : -1]
    X1 = Change2_10(Sel_LJ1, lb, ub, D)
    FV1 = funv(X1)
    fitnv1 = fit(FV1)
    index = fitnv1 > fitnv
    Sel_LJ[index, :] = Sel_LJ1[index, :]
    return Sel_LJ


""" Sel_LJ = Reverse(Sel_LJ, fitnv)

# 逆转后的最优解
X=Change2_10(Sel_LJ, lb, ub, D)
FV=funv(X)
fitnv=fit(FV)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到适用度值最大即三个方程的平方和最小解
Rev_obj = FV[index]-1
Rev_X=X[index]
print("Rev_obj=", Rev_obj)
print("Rev_X=", Rev_X) """

# 重新产生新种群
# 输入原种群LJ
# 输入经过遗传操作后的优势种群Sel_LJ
# 输出新的种群LJ1
def newLJ(LJ, Sel_LJ):
    ZQS, n = LJ.shape
    sel_num = len(Sel_LJ)
    X = Change2_10(LJ, lb, ub, D)
    FV = funv(X)
    fitnv = fit(FV)
    tem_p = []
    for i, e in enumerate(fitnv):
        tem_p.append((i, e))
    z = sorted(tem_p, key=lambda x: x[1], reverse=True)  # 按fitnv从大到小排序
    index = [id[0] for id in z]  # 获得从大到小排序的原fitnv数组的序号
    LJ1 = np.copy(LJ)
    LJ1[0 : ZQS - sel_num - 1, :] = LJ[index[0 : ZQS - sel_num - 1], :]
    LJ1[ZQS - sel_num : ZQS, :] = Sel_LJ
    return LJ1


# LJ = newLJ(LJ, Sel_LJ)
# print("LJ_new=",LJ)

gen = 0
plt.figure(num="目标函数值和遗传代数关系")
while gen <= Maxgen:
    X = Change2_10(LJ, lb, ub, D)
    FV = funv(X)
    fitnv = fit(FV)
    index = list(fitnv[:]).index(max(fitnv[:]))
    obj = FV[index] - 1  # 初次遗传操作后的最优解
    plt.plot([gen, gen + 1], [pre_obj, obj], lw=2)
    pre_obj = obj
    # 选择操作
    Sel_LJ = select(LJ, Sel_ra, fitnv)  # LJ由上一代带入
    # 交叉重组操作
    Sel_LJ = Re_com(Sel_LJ, Pc)
    # 变异操作
    Sel_LJ = Mutate(Sel_LJ, Pm)
    X = Change2_10(Sel_LJ, lb, ub, D)
    FV = funv(X)
    fitnv = fit(FV)
    # 逆转操作
    Sel_LJ = Reverse(Sel_LJ, fitnv)
    # 新种子重组，保证上一轮最优解遗传给下一代
    LJ = newLJ(LJ, Sel_LJ)
    gen = gen + 1
plt.xlabel("遗传代数")
plt.ylabel("目标函数值")
plt.title("目标函数值和遗传代数关系")
plt.grid()

# 打印最后最优解
X = Change2_10(LJ, lb, ub, D)
FV = funv(X)
fitnv = fit(FV)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
opt_obj = FV[index] - 1
opt_X = X[index]
print("最优目标函数=", opt_obj)
print("最优解=", opt_X)
plt.show()
