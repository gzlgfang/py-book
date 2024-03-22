#!/usr/bin/env python3
# 04-Simulated annealing opt_fun
# 模拟退火求函数优化
from typing import Type
import numpy as np
import random as rnd
import time

# 绘图设置
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.lib import copy

mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
# 模拟退火基础参数：
from scipy import optimize

# global T0, q, Tend, T
T0 = 2000  # 初始温度
Tend = 0.0005  # 最终温度
L = 180  # 链长，每次稳定温度下优化次数
q = 0.93  # 温度下降速率


def funT(x):  # 降温函数
    return T0 * q ** x[0] - Tend


T_num = int(optimize.fsolve(funT, [30]) + 2)  # 计算退火次数，+2保证数据下标
D = 2  # 变量维数
lb, ub = -0.5, 0.5  # 变量上下限
# lb,ub=-5,10
N = 80  # 二进制数据长度


def Bin_pop(N):  # 产生初始变量二进制数
    LJ = np.zeros(N)
    for i in range(N):
        LJ[i] = np.fix(0.5 + np.random.random())
    return LJ.astype(int)  # 需要强制转变成整数


def Change2_10(LJ, lb, ub, D):  # 二进制转化为10进制，能区分变量数目及上下限
    N = len(LJ)  # 二进制数组大小
    var2_num = int(N / D)  # 每个变量的二进制数编码长度
    x = np.zeros(D)
    for i in range(D):
        temp0 = 0  #
        temp1 = 0
        for k in range(var2_num):
            temp0 = temp0 + 2 ** (var2_num - k - 1) * LJ[i * var2_num + k]
            temp1 = temp1 + 2**k
        temp0 = lb + temp0 / temp1 * (ub - lb)
        x[i] = temp0
    return x.T


def fun(x):  # 定义函数
    x1 = x[0]
    x2 = x[1]
    # return  225*np.log(14-0.1*t)/(130-t)+480/(t-30)
    # return -20*np.exp(-0.2*np.sqrt(x1**2+x2**2))+20+np.exp(1)-np.exp(0.5*(np.cos(2*np.pi*x1)+np.cos(2*np.pi*x2)))
    # return   5+(6-x1)**2+(8-x2)**2
    return (
        30 + x1**2 + x2**2 - 10 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))
    )


def Newpath(LJ):
    # 有原来的二进制LJ1数组计算产生新的二进制LJ2数组(部分逆转）
    # 输入 LJ1 原来的二进制数组
    # 输出 LJ2 新的二进制数组
    n = int(len(LJ))  # 计算单个二进制数组长度
    LJ2 = copy(LJ)  # 先将原数组全部复制到新数组
    flags = True
    while flags:
        r1 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
        r2 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
        r3 = rnd.randint(0, n - 1)  # 辅助扰动
        if r1 != r2:
            flags = False
        if r1 > r2:
            r_min, r_max = r2, r1
        else:
            r_min, r_max = r1, r2
        if r_min == 0:
            r_min = 1
        # LJ2[r_min:r_max+1]=LJ[r_max:r_min-1:-1]
        LJ2[r_min] = LJ[r_max]
        LJ2[r_max] = LJ[r_min]
        # LJ2[r_min+n]=LJ[r_max+n]
        # LJ2[r_max+n]=LJ[r_min+n]#针对两个变量
        # LJ2[5]=LJ[r3]
    return LJ2


LJ1 = Bin_pop(N)
LJ2 = Newpath(LJ1)
x = Change2_10(LJ2, lb, ub, D)  # 2进制转化为10进制，能区分变量数目及上下限
preObj = fun(x)
print("初始解及目标函数=", x, preObj)
# 新解确定与否判定
def Metropolis(LJ1, LJ2, T, D, lb, ub):
    x1 = Change2_10(LJ1, lb, ub, D)
    f1 = fun(x1)  # 计算变量为x1的函数值
    x2 = Change2_10(LJ2, lb, ub, D)
    f2 = fun(x2)  # 计算变量为x2的函数值
    dc = f2 - f1
    if dc < 0:
        LJ = LJ2
        f = f2
    else:
        if np.exp(-dc / T) >= rnd.random():
            LJ = LJ2
            f = f2
        else:
            LJ = LJ1
            f = f1
    return [LJ, f]


[LJ, f] = Metropolis(LJ1, LJ2, T0, D, lb, ub)
count = 0
LJ0 = LJ.astype(int)
# print(LJ0, f)

count = 0
obj = np.zeros(T_num)  # 初始化路径总距离
obj1 = np.zeros(T_num)
track = np.zeros((T_num, N))  # 初始化轨迹
# 迭代
while T0 > Tend:
    count = count + 1
    tem_LJ = np.zeros((L, N))
    tem_len = np.zeros(L)
    # 进行一次退火需要进行L次新函数计算
    for i in range(L):
        LJ1 = LJ0
        LJ2 = Newpath(LJ0)
        # Metropolis 法则判断新解
        [LJ0, f] = Metropolis(LJ1, LJ2, T0, D, lb, ub)
        tem_LJ[i, :] = LJ0[:].astype(int)  # 临时记录下一路径及路程，在每次退火过程中数据会更新
        tem_len[i] = f
    # looking for the most short way
    index = list(tem_len[:]).index(min(tem_len[:]))  # 找到最短距离路径序号
    opt_var = tem_len[index]
    opt_LJ = tem_LJ[index, :]
    obj1[count] = opt_var
    obj[count] = opt_var  # 将计算本次退火操作中最小的函数值给 obj(count)
    track[count, :] = opt_LJ[:]  # 记录当前温度的最优变量
    LJ0 = opt_LJ.astype(int)
    T0 = q * T0
    if count > 1 and opt_var > obj[count - 1]:
        LJ0 = track[count - 1, :].astype(
            int
        )  # 如果本次退火操作最小函数值大于上次退火的最小函数, 用上次退火最优变量代替本次退火最优变量进行新的退火操作
        obj[count] = obj[count - 1]
        track[count, :] = track[count - 1, :]

# 进行新的退火操作时只需保留到目前为止最优的轨迹


x = Change2_10(LJ0, lb, ub, D)
print("最优解=", x)
print("最优目标函数=", fun(x))
plt.figure(num="目标函数和和退火次数关系图1")
for i in range(1, T_num - 1):
    plt.plot([i, i + 1], [obj[i], obj[i + 1]])
plt.xlabel("退火次数")
plt.ylabel("目标函数")

plt.grid()
plt.figure(num="目标函数和和退火次数关系图2")
for i in range(1, T_num - 1):
    plt.plot([i, i + 1], [obj1[i], obj1[i + 1]])


plt.grid()
plt.show()
