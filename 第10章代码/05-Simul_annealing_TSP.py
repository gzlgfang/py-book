#!/usr/bin/env python3
# 05-Simulated annealing TSP
# 最优计算结果153.77
from typing import Type
from matplotlib import colors, markers
import numpy as np
from numpy.core.numeric import tensordot
from numpy.lib import copy
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

# 模拟退火基础参数：
from scipy import optimize

global T0, q, Tend, T
T0 = 2800  # 初始温度
Tend = 0.0006  # 最终温度
L = 380  # 链长，每次稳定温度下优化次数
q = 0.93  # 温度下降速率


def fun(x):
    return T0 * q ** x[0] - Tend


T_num = int(optimize.fsolve(fun, [30]) + 2)  # 计算退火次数
# 读入城市坐标
DF = pd.read_excel("city.xlsx", "Sheet1", na_filter=False, index_col=0)  # 共有31个城市坐标
city_x = np.array(DF["x"])  # 数据分配
city_y = np.array(DF["y"])
n = len(city_x)  # 计算城市的数目
city_zb = np.zeros((n, 2))  # 设置坐标数组
city_zb[:, 0] = city_x / 100
city_zb[:, 1] = city_y / 100
# 计算城市i和城市j之间的距离
# 输入 city_zb 各城市的坐标,用city_zb[i,0:1])
# 输出 D 城市i和城市j之间的距离,用D[i,j]表示
def Distance(city_zb):
    D = np.zeros((n, n))  #  产生两城市之间距离数据的空矩阵即零阵
    for i in range(n):
        for j in range(i + 1, n):
            D[i, j] = (
                (city_zb[i, 0] - city_zb[j, 0]) ** 2
                + (city_zb[i, 1] - city_zb[j, 1]) ** 2
            ) ** 0.5
            D[j, i] = D[i, j]
    return D


D = Distance(city_zb)  # 计算一次即可
# 产生初始轨迹LJ0
def path(N):
    li = np.arange(0, N)
    # LJ = np.zeros(N)
    # rnd.shuffle(li)
    LJ = rnd.sample(list(li), N)
    # LJ[:] = li
    return LJ  # .astype(int)  # 需要强制转变成整数


LJ0 = path(n)


# 绘制初始路径图
# 画路径函数
# 输入
# LJ 待画路径
# city_zb 各城市坐标位置
# num为图片左上角的图名
def drawpath(LJ, city_zb, num):
    plt.figure(num=num)
    n = len(LJ)
    plt.scatter(
        city_zb[:, 0], city_zb[:, 1], marker="o", color="b", s=100
    )  # 所有城市位置上画上o
    plt.text(city_zb[LJ[0], 0] + 0.5, city_zb[LJ[0], 1] + 0.5, "起点")
    plt.text(city_zb[LJ[n - 1], 0] + 0.5, city_zb[LJ[n - 1], 1] + 0.5, "终点")
    for i in range(n):
        # plt.text(city_zb[LJ[i],0]-0.3,city_zb[LJ[i],1]+0.5,str(i+1),color="r")
        plt.text(city_zb[i, 0] - 0.3, city_zb[i, 1] + 0.5, str(i + 1), color="r")
    # 绘线
    xy = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
    xytext = (city_zb[LJ[1], 0], city_zb[LJ[1], 1])
    plt.annotate(
        "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="g", lw=2)
    )
    for i in range(1, n - 1):
        # x=[city_zb[LJ[i],0],city_zb[LJ[i+1],0]]
        # y=[city_zb[LJ[i],1],city_zb[LJ[i+1],1]]
        # plt.plot(x,y,lw=2,c="r")
        xy = [city_zb[LJ[i], 0], city_zb[LJ[i], 1]]
        xytext = [city_zb[LJ[i + 1], 0], city_zb[LJ[i + 1], 1]]
        plt.annotate(
            "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="g", lw=2)
        )

    xy = (city_zb[LJ[n - 1], 0], city_zb[LJ[n - 1], 1])
    xytext = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
    plt.annotate(
        "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="g", lw=1)
    )
    plt.ylim(0, 40)
    plt.xlim(10, 45)
    plt.grid()
    plt.xlabel("横坐标")
    plt.ylabel("纵坐标")
    plt.title(" 轨迹图")


print(T_num)


def pathlength(D, LJ):
    N = D.shape[1]
    ZQS = 1
    p_len = np.zeros(ZQS)
    for i in range(ZQS):
        for j in range(N - 1):
            p_len[i] = p_len[i] + D[LJ[j], LJ[j + 1]]
        p_len[i] = p_len[i] + D[LJ[N - 1], LJ[0]]
    return p_len


p_len = pathlength(D, LJ0)


# 绘制初始路径1
num = "绘制初始路径"
draw_path = drawpath(LJ0, city_zb, num)
# plt.legend(str(p_len[0]))
plt.text(35, 35, "总长度=")
plt.text(37, 35, str(int(1000 * p_len) / 1000))

# 打印优化路径
def print_way(LJ):
    print_LJ = str()
    n = len(LJ)
    for i in range(n):
        print_LJ = print_LJ + str(LJ[i] + 1) + "-->"
    print_LJ = print_LJ + str(LJ[0] + 1)
    print(print_LJ)


print("初始路径")
print_way(LJ0)


def Newpath(LJ):
    # 有原来的旅行轨迹LJ1计算产生新的旅行轨迹LJ2(部分逆转）
    # 输入 LJ1 原来的旅行轨迹，是0到N-1城市的数字排列
    # 输出 LJ2 新的旅行轨迹,逆转扰动
    N = len(LJ)  # 计算城市的数目
    LJ2 = copy(LJ)  # 先将原轨迹全部复制到新轨迹
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
            r_min = 1  # 轨迹逆转
        LJ2[r_min : r_max + 1] = LJ[r_max : r_min - 1 : -1]
    return LJ2


LJ2 = Newpath(LJ0)
p_len = pathlength(D, LJ2)
num = "绘制初始退火路径"
draw_path = drawpath(LJ2, city_zb, num)
# plt.legend(str(p_len[0]))
plt.text(35, 35, "总长度=")
plt.text(37, 35, str(int(1000 * p_len) / 1000))
# 判断新路径是否被采用


def Metropolis(LJ0, LJ2, D, T):
    Len1 = pathlength(D, LJ0)  # 计算轨迹LJ0路径长度
    Len2 = pathlength(D, LJ2)  # 计算轨迹GJ2路径长度
    dc = Len2 - Len1
    if dc < 0:
        LJ = LJ2
        Len = Len2
    else:
        if np.exp(-dc / T) >= rnd.random():
            LJ = LJ2
            Len = Len2
        else:
            LJ = LJ0
            Len = Len1
    return [LJ, Len]


[LJ0, Len] = Metropolis(LJ0, LJ2, D, T0)
count = 0
LJ0 = LJ0.astype(int)
# 初始化设置及函数定义工作完成，进入主程序迭代
# print(Len)
print_way(LJ0)


count = 0
obj = np.zeros(T_num)  # 初始化路径总距离
obj1 = np.zeros(T_num)
track = np.zeros((T_num, n))  # 初始化轨迹
# 迭代
while T0 > Tend:
    count = count + 1
    tem_LJ = np.zeros((L, n))
    tem_len = np.zeros(L)
    # 进行一次退火需要进行L次新轨迹计算
    for i in range(L):
        LJ2 = Newpath(LJ0)
        # Metropolis 法则判断新解
        [LJ0, Len] = Metropolis(LJ0, LJ2, D, T0)
        tem_LJ[i, :] = LJ0[:].astype(int)  # 临时记录下一路径及路程，在每次退火过程中数据会更新
        tem_len[i] = Len[0]
    # looking for the most short way
    index = list(tem_len[:]).index(min(tem_len[:]))  # 找到最短距离路径序号
    opt_sd = tem_len[index]
    opt_LJ = tem_LJ[index, :]
    obj[count] = opt_sd  # 将计算本次退火操作中最小的路程SD赋值给 obj(count)
    obj1[count] = opt_sd
    track[count, :] = opt_LJ[:]  # 记录当前温度的最优路径
    LJ0 = opt_LJ.astype(int)
    T0 = q * T0
    if count > 1 and opt_sd > obj[count - 1]:
        LJ0 = track[count - 1, :].astype(
            int
        )  # 如果本次退火操作最小路程大于上次退火的最小路程, 用上次退火最优轨迹代替本次退火最优轨迹进行新的退火操作
        obj[count] = obj[count - 1]
        track[count, :] = track[count - 1, :]
# 进行新的退火操作时只需保留到目前为止最优的轨迹


# 绘制最优路径1
print_way(LJ0)
p_len = pathlength(D, LJ0)
print(p_len)
num = "绘制最优路径"
draw_path = drawpath(LJ0, city_zb, num)
# plt.legend(str(p_len[0]))
plt.text(35, 35, "总长度=")
plt.text(37, 35, str(int(1000 * p_len) / 1000))

plt.figure(num="优化路径距离和退火次数关系图")
for i in range(1, T_num - 1):
    plt.plot([i, i + 1], [obj[i], obj[i + 1]])
plt.xlabel("退火次数")
plt.ylabel("优化路径长度")
plt.title("优化路径距离和退火次数关系图")

plt.grid()
plt.show()
