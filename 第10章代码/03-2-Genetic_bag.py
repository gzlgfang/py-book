#!/usr/bin/env python3
# 03-2-Genetic algorithm  for bag_problem
from matplotlib import colors
from matplotlib.figure import Figure
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
# 产生随机物体重量和及价值数据mass_value
def mass_value(num):
    """
    num：物体数目
    """
    m_v = np.zeros((2, num))
    for i in range(num):
        m_v[0, i] = int(np.random.random() * 100) + 1  # 产生0-100的随机整数
        m_v[1, i] = int(np.random.random() * 100) + 1
    return m_v


m_v = mass_value(30)  # 确定物体数目、重量和及价值
n=30
m=np.array(m_v[0,:])
v=np.array(m_v[1,:])
# 输入确定的物体重量及价值
# v = np.array(
#     [
#         202,
#         208,
#         198,
#         192,
#         180,
#         180,
#         165,
#         162,
#         160,
#         158,
#         155,
#         130,
#         125,
#         122,
#         120,
#         118,
#         115,
#         110,
#         105,
#         101,
#         110,
#         100,
#         98,
#         96,
#         95,
#         90,
#         88,
#         82,
#         80,
#         77,
#         75,
#         73,
#         72,
#         70,
#         69,
#         66,
#         65,
#         63,
#         60,
#         58,
#         56,
#         50,
#         30,
#         20,
#         15,
#         10,
#         8,
#         5,
#         3,
#         1,
#     ]
# )
# m = np.array(
#     [
#         80,
#         82,
#         85,
#         70,
#         72,
#         70,
#         66,
#         50,
#         55,
#         25,
#         50,
#         55,
#         40,
#         48,
#         50,
#         32,
#         22,
#         60,
#         30,
#         32,
#         40,
#         38,
#         35,
#         32,
#         25,
#         28,
#         30,
#         22,
#         50,
#         30,
#         45,
#         30,
#         60,
#         50,
#         20,
#         65,
#         20,
#         25,
#         30,
#         10,
#         20,
#         25,
#         15,
#         10,
#         10,
#         10,
#         4,
#         4,
#         2,
#         1,
#     ]
# )
# n = len(m)
M = 1000  # 背包中可以放入的总重量
# 定义背包是否放入物品0-1数组，0代表不放入，1代表放入
def put_array(n):
    x = np.zeros(n)
    for i in range(n):
        if np.random.random() >= 0.5:
            x[i] = 1
    return x
x = put_array(n)
# 计算背包中放入的总重量
def total_mass(x, m):
    T_mass = sum(x * m)
    return T_mass
# 计算背包中放入的总价值
def total_value(x, m):
    T_value = sum(x * v)
    return T_value

# 设置基本遗传数据
ZQS = 300  # 种群大小
Maxgen = 500  # 最大遗传代数
Pc = 0.8  # 交叉概率
Pm = 0.3  # 变异概率
Sel_ra = 0.8  # 选择率
# 产生随机放入背包物体序列，共ZQS个
# 输入种群数ZQS及物品总数目n
def array(ZQS, n):
    T_x = np.zeros((ZQS, n))
    for i in range(ZQS):
        T_x[i, :] = put_array(n)
    return T_x
T_x = array(ZQS, n)
# 计算种群全部个体的放入背包的总重量GM
def gene_mass(T_x, m):
    ZQS = T_x.shape[0]
    GM = np.zeros(ZQS)
    for i in range(ZQS):
        GM[i] = total_mass(T_x[i, :], m)
    return GM
# 计算种群全部个体的放入背包的总价值GV
def gene_value(T_x, v):
    ZQS = T_x.shape[0]
    GV = np.zeros(ZQS)
    for i in range(ZQS):
        GV[i] = total_mass(T_x[i, :], v)
    return GV
# 计算适应度值fitness 归一化处理
def fit(GM, GV, M):
    ZQS = len(GM)
    fitnv = np.ones(ZQS)
    for i in range(ZQS):
        if GM[i] > M:
            GV[i] = -i
    fitnv[:] = GV[:]
    max = np.max(fitnv)
    min = np.min(fitnv)
    fitnv[:] = (fitnv[:] - min) / (max - min)
    return fitnv
def draw_T_x(T_x, GM, GV, index, num):
    plt.figure(num=num)
    n = T_x.shape[1]
    x = np.arange(1, n + 1)
    y = T_x[index]
    plt.scatter(
        x, y, s=100, c="red", cmap=mpl.cm.RdYlBu, clip_on=False
    )  # clip_on=False表示坐标轴上的Mark也要整体显示
    plt.plot(x, y, lw=2)
    plt.xticks(np.arange(0, n + 1, 1))
    plt.yticks([0, 1])
    # plt.xticks(np.arange(0,n+1,1),position='top')
    plt.tick_params(top="on", right="on", which="both", direction="in")
    plt.xlabel("物件序号，n")
    plt.ylabel("放入包内逻辑数，x")
    plt.text(n / 2, 0.6, f"放入物品总重量GM(index)={GM[index]:.1f}", c="b")
    plt.text(n / 2, 0.5, f"放入物品总价值GV(index)={GV[index]:.1f}", c="b")
    plt.title("物体是否放入包内逻辑数据图")
    plt.xlim(0, n)
    plt.grid(c="green", ls="-.")
# 打印初始优化结果图
GM = gene_mass(T_x, m)
GV = gene_value(T_x, v)
fitnv = fit(GM, GV, M)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
pre_obj = GV[index]
num = "初始优化结果图"
draw_T_x(T_x, GM, GV, index, num)
# 开始遗传算法核心代码
# 选择操作
LJ = T_x
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
Sel_LJ = select(LJ, Sel_ra, fitnv)
# 选择操作后的最优解
GM = gene_mass(Sel_LJ, m)
GV = gene_value(Sel_LJ, v)
fitnv = fit(GM, GV, M)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
print(index, GM[index], GV[index])
print(Sel_LJ[index, :])
num = "选择操作的最优解图"
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
Sel_LJ = Re_com(Sel_LJ, Pc)
# 交叉重组后的最优解
GM = gene_mass(Sel_LJ, m)
GV = gene_value(Sel_LJ, v)
fitnv = fit(GM, GV, M)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
print(index, GM[index], GV[index])
print(Sel_LJ[index, :])
num = "交叉重组后的最优解图"
# Pm为变异概率
# Sel_LJ为变异操作前后路径,原来0的变成1，原来1的变成0
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

Sel_LJ = Mutate(Sel_LJ, Pm)  # 变异后的路径
# 变异后的最优解
GM = gene_mass(Sel_LJ, m)
GV = gene_value(Sel_LJ, v)
fitnv = fit(GM, GV, M)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
print(index, GM[index], GV[index])
print(Sel_LJ[index, :])
num = "变异后的最优解"
draw_T_x(Sel_LJ, GM, GV, index, num)
# 逆转操作
def Reverse(Sel_LJ, m, v, M):
    ZQS, n = Sel_LJ.shape
    Sel_LJ = np.array(Sel_LJ)
    GM = gene_mass(Sel_LJ, m)
    GV = gene_value(Sel_LJ, v)
    fitnv = fit(GM, GV, M)
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
    GM = gene_mass(Sel_LJ1, m)
    GV = gene_value(Sel_LJ1, v)
    fitnv1 = fit(GM, GV, M)
    # p_len1=pathlength(D,Sel_LJ1); # %计算路径长度
    index = fitnv1 > fitnv
    Sel_LJ[index, :] = Sel_LJ1[index, :]
    return Sel_LJ
Sel_LJ = Reverse(Sel_LJ, m, v, M)
print(Sel_LJ)

# 逆转后的最优解
GM = gene_mass(Sel_LJ, m)
GV = gene_value(Sel_LJ, v)
fitnv = fit(GM, GV, M)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
print(index, GM[index], GV[index])
print(Sel_LJ[index, :])
num = "逆转后的最优解"
# draw_T_x(Sel_LJ,GM,GV,index,num)
# 重新产生新种群
# 输入原种群LJ
# 输入经过遗传操作后的优势种群Sel_LJ
# 输出新的种群LJ1
def newLJ(LJ, Sel_LJ, m, v, M):
    ZQS, n = LJ.shape
    sel_num = len(Sel_LJ)
    GM = gene_mass(LJ, m)
    GV = gene_value(LJ, v)
    fitnv = fit(GM, GV, M)
    tem_p = []
    for i, e in enumerate(fitnv):
        tem_p.append((i, e))
    z = sorted(tem_p, key=lambda x: x[1], reverse=True)  # 按fitnv从大到小排序
    index = [id[0] for id in z]  # 获得从大到小排序的原fitnv数组的序号
    LJ1 = np.copy(LJ)
    LJ1[0 : ZQS - sel_num - 1, :] = LJ[index[0 : ZQS - sel_num - 1], :]
    LJ1[ZQS - sel_num : ZQS, :] = Sel_LJ
    return LJ1
LJ = newLJ(LJ, Sel_LJ, m, v, M)
gen = 0  # 遗传代数
# pre_obj=p_len(index) 为上一轮最优
print(gen, pre_obj)
plt.figure(num="优化总价值和遗传代数关系")
while gen <= Maxgen:
    GM = gene_mass(LJ, m)
    GV = gene_value(LJ, v)
    fitnv = fit(GM, GV, M)
    index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
    obj = GV[index]  # 初次遗传操作后的最优解
    plt.plot([gen, gen + 1], [pre_obj, obj], lw=2)
    pre_obj = obj
    # 选择操作
    fitnv = fit(GM, GV, M)
    Sel_LJ = select(LJ, Sel_ra, fitnv)  # LJ由上一代带入
    # 交叉重组操作
    # Sel_LJ=Re_com(Sel_LJ,Pc)
    # 变异操作
    Sel_LJ = Mutate(Sel_LJ, Pm)
    # 逆转操作
    Sel_LJ = Reverse(Sel_LJ, m, v, M)
    # 新种子重组，保证上一轮最优解遗传给下一代
    LJ = newLJ(LJ, Sel_LJ, m, v, M)
    gen = gen + 1
plt.xlabel("遗传代数")
plt.ylabel("放入物品总价值")
plt.title("优化总价值和遗传代数关系")
plt.grid()
# 绘制最后最优解
num = "绘制最终优化图"
GM = gene_mass(LJ, m)
GV = gene_value(LJ, v)
fitnv = fit(GM, GV, M)
index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
print(index, GM[index], GV[index])
print(LJ[index, :])
draw_T_x(LJ, GM, GV, index, num)
plt.show()
