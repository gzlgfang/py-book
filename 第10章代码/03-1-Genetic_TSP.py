#!/usr/bin/env python3
# 03-1-Genetic algorithm

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


# 产生随机城市坐标city_zb
def city_zb(width, hight, city_num):
    """
    width:城市配置平面图宽度
    hight:城市配置平面图高度
    city_num：配置城市数目
    """
    city_zb = np.zeros((city_num, 2))
    for i in range(city_num):
        city_zb[i, 0] = int(np.random.random() * width * 100) / 100
        city_zb[i, 1] = int(np.random.random() * hight * 100) / 100
    return city_zb


# city_zb=city_zb(50,50,15)#确定城市数目及坐标

# # 读入城市坐标
# DF = pd.read_excel("city.xlsx", "Sheet1", na_filter=False, index_col=0)  # 共有31个城市坐标
# city_x = np.array(DF["x"])  # 数据分配
# city_y = np.array(DF["y"])
# n = len(city_x)  # 计算城市的数目
# city_zb = np.zeros((n, 2))  # 设置坐标数组
# city_zb[:, 0] = city_x / 100
# city_zb[:, 1] = city_y / 100


city_zb=city_zb(100,100,100)#确定城市数目及坐标
n=len(city_zb)
print("n=",n)

# 计算城市i和城市j之间的距离
# 输入 city_zb 各城市的坐标,用city_zb[i,0:1])
# 输出 D 城市i和城市j之间的距离,用D[i,j]表示
def Distance(city_zb):
    n = len(city_zb)
    D = np.zeros((n, n))  #  产生两城市之间距离数据的空矩阵即零阵
    for i in range(n):
        for j in range(i + 1, n):
            # D[i,j]=city_zb[i,0]
            D[i, j] = (
                (city_zb[i, 0] - city_zb[j, 0]) ** 2
                + (city_zb[i, 1] - city_zb[j, 1]) ** 2
            ) ** 0.5
            D[j, i] = D[i, j]
    # D[0, 14] = D[14, 0] = 10000000  # 0-14之间有障碍物
    # D[29, 30] = D[30, 29] = 1000000
    return D


D = Distance(city_zb)  # 计算一次即可
# print(D)
# 设置基本遗传数据
ZQS = 100  # 种群大小
Maxgen= 1000  # 最大遗传代数
Pc = 0.6  # 交叉概率
Pm = 0.2  # 变异概率
Sel_ra = 0.7  # 选择率

# 产生随机路径path，一般调用一次即可
# 输入种群数ZQS及城市数目N
def path(ZQS, N):
    li = np.arange(0, N)
    LJ = np.zeros((ZQS, N))
    for i in range(ZQS):
        rnd.shuffle(li)
        # li=np.random.randint(N,size=N)
        LJ[i, :] = li
    return LJ.astype(int)  # 需要强制转变成整数


LJ = path(ZQS, n)
# print(LJ)
# print(type(LJ))
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
    # 无需回起点时，下面3行代码不要程序
    xy = (city_zb[LJ[n - 1], 0], city_zb[LJ[n - 1], 1])
    xytext = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
    plt.annotate(
        "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="g", lw=2)
    )

    # plt.ylim(0, 40)
    # plt.xlim(10, 45)

    plt.ylim(-5,105)
    plt.xlim(-5,105)

    plt.grid()
    plt.xlabel("横坐标")
    plt.ylabel("纵坐标")
    plt.title("轨迹图")


# 计算路径总距离
def pathlength(D, LJ):
    N = D.shape[1]
    ZQS = LJ.shape[0]
    p_len = np.zeros(ZQS)
    for i in range(ZQS):
        for j in range(N - 1):
            p_len[i] = p_len[i] + D[LJ[i, j], LJ[i, j + 1]]
        # 无需回起点时，下面1行代码不要
        p_len[i] = p_len[i] + D[LJ[i, N - 1], LJ[i, 0]]
    return p_len


p_len = pathlength(D, LJ)
# print(p_len)
# p_sort=np.sort(p_len)
# print(p_sort)
# 计算适应度值fitness 归一化处理
def fit(p_len):
    ZQS = len(p_len)
    fitnv = np.ones(ZQS)
    fitnv[:] = 1 / p_len[:]
    max = np.max(fitnv)
    min = np.min(fitnv)
    fitnv[:] = (fitnv[:] - min) / (max - min)
    return fitnv


# print(fit(p_len))

# 绘制初始路径1
num = "绘制初始路径1"
draw_path = drawpath(LJ[0, :], city_zb, num)
# plt.legend(str(p_len[0]))
# print(p_len[0])
plt.text(35, 35, "总长度=")
plt.text(37, 35, str(int(1000 * p_len[0]) / 1000))


# 绘制初始优化图
index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号
# print(index)
num = "绘制初始优化图"
draw_path = drawpath(LJ[index, :], city_zb, num)
# plt.legend(str(p_len[0]))
# print(p_len[index])
plt.text(35, 35, "总长度=")
plt.text(37, 35, str(int(1000 * p_len[index]) / 1000))

pre_obj = p_len[index]
print("初始最优解=", pre_obj)
# 初始种群优化图
fitnv = fit(p_len)
# 选择操作
def select(LJ, Sel_ra, fitnv):
    ZQS = len(LJ)
    sel_num = int(ZQS * Sel_ra)
    n = 0
    index = []
    flags = True
    while flags:
        for i in range(ZQS):
            pick = rnd.random()
            if pick < 0.8 * fitnv[i]:
                index.append(i)
                n = n + 1
                if n == sel_num:
                    break
        if n == sel_num:
            flags = False
    Sel_LJ = LJ[index]
    return Sel_LJ


Sel_LJ = select(LJ, Sel_ra, fitnv)

# print(Sel_LJ.shape)
# print(index)
# print(fitnv[index])
# print(Sel_LJ)

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
    # 保证找到两个不同是整数，可以进行交叉操作
    a1 = np.zeros(n)
    b1 = np.zeros(n)
    a1[:] = a[:]  # 先保护原数据到a1,b1
    b1[:] = b[:]
    r=[r1,r2]
    s=min(r)
    e=max(r)
    #print("s,e=",s,e)
    ar1=np.arange(0,n)
    ar2=np.arange(s,e+1)
    tan=np.delete(ar1,ar2)
    tan=tan.astype(int) #tan为扣除交换段序号的其他序号，需强制转换为整数
    #print("tan=:",tan)
    id1=[]
    id2=[]
    for i in range(s, e + 1):
        a[i] = b1[i]#第i个元素进行互换
        b[i] = a1[i]
        # a1,b1=a,b#先保护原数据到a1,b1
        x = [id for k,id in enumerate(tan)  if abs(a[id] -a[i])<0.01]  # 找到交换后a中重复元素的序号
        y = [id for k,id in enumerate(tan)  if abs(b[id] - b[i])<0.01]
        if x != []:
           id1.append(x[0])
        if y !=[]:
           id2.append(y[0])
    #print("i=",i)
    #print("id1=",id1)
    #print("id2=",id2)
    #print(len(id1),len(id2))
    #if id1 != []:
    for i in range(len(id1)): #其实就是交换后重复元素的序号，除i以外
        a[id1[i]] =b1[id2[i]]#a重复的元素用原来没交换前b重复的对应元素替换
        b[id2[i]] =a1[id1[i]]#b重复的元素用原来没交换前a重复的对应元素替换
    return [a, b]
# def cross(a, b):
#     # a和b为两个待交叉的个体
#     # 输出：
#     # a和b为交叉后得到的两个个体
#     n = len(a)  # 城市数目
#     flags = True
#     while flags:
#         r1 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
#         r2 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
#         if r1 != r2:
#             flags = False
#     # 保证找到两个不同是整数，可以进行交叉操作
#     a0 = np.zeros(n)
#     b0 = np.zeros(n)
#     a1 = np.zeros(n)
#     b1 = np.zeros(n)
#     # a0[:] = a[:]
#     # b0[:] = b[:]
#     a1[:] = a[:]  # 先保护原数据到a1,b1
#     b1[:] = b[:]
#     # r=np.random.randint(n,size=2) #可能重复
#     # r.sort()
#     # r1,r2=r[0],r[1]
#     # a0,b0=a,b#作为中间变量
#     if r1 > r2:
#         s, e = r2, r1
#     else:
#         s, e = r1, r2
#     # s,e=r1,r2
#     # a[s:e+1]=b0[s:e+1]
#     # b[s:e+1]=a0[s:e+1]
#     # print(s,e)
#     for i in range(s, e + 1):
#         a[i] = b1[i]
#         b[i] = a1[i]
#         # a1,b1=a,b#先保护原数据到a1,b1
#         x = [id for id in range(n) if a[id] == a[i]]  # 找到交换后a中重复元素的序号
#         y = [id for id in range(n) if b[id] == b[i]]
#         # print("i=",x,y)
#         id1 = [s1 for k, s1 in enumerate(x) if x[k] != i]  # 找到序号不为i的其他序号
#         id2 = [s2 for k, s2 in enumerate(y) if y[k] != i]
#         # print("i=",i)
#         # print(id1)
#         # print(id2)
#         if id1 != []:
#             i1 = id1[0]
#             a[i1] = a1[i]
#             a1[i1] = a[i1]
#         if id2 != []:
#             i2 = id2[0]
#             b[i2] = b1[i]
#             b1[i2] = b[i2]
#     return [a, b]


# 交叉重组
def Re_com(Sel_LJ, Pc):
    n = len(Sel_LJ)
    for i in range(0, n - 1, 2):
        # print(i)
        if Pc >= rnd.random():  #%交叉概率Pc
            [Sel_LJ[i, :], Sel_LJ[i + 1, :]] = cross(Sel_LJ[i, :], Sel_LJ[i + 1, :])
    return Sel_LJ


Sel_LJ = Re_com(Sel_LJ, Pc)
# print("NEW=",Sel_LJ)

# 交叉重组后的最优解
p_len = pathlength(D, Sel_LJ)
# fitnv=fit(p_len)
index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号
# print(index)
print(Sel_LJ[index])
num = "初始交叉重组后的最优解"
draw_path = drawpath(Sel_LJ[index], city_zb, num)
plt.text(40, 37, "总长度=")
plt.text(42, 37, str(int(1000 * p_len[index]) / 1000))
# print(np.sort(Sel_LJ[index]))
# print(Sel_LJ[index])

# 变异操作
# Pm为变异概率
# Sel_LJ为变异操作前后路径
def Mutate(Sel_LJ, Pm):
    ZQS, n = Sel_LJ.shape
    Sel_LJ1 = np.copy(Sel_LJ)
    for i in range(ZQS):
        if Pm >= rnd.random():
            r = np.random.randint(n, size=2)
            r.sort()  # 产生2个不相等的0到n-1的整数
            r_min = r[0]
            r_max = r[1]
            Sel_LJ[i, r_min] = Sel_LJ1[i, r_max]
            Sel_LJ[i, r_max] = Sel_LJ1[i, r_min]
    return Sel_LJ


# print(np.sort(Sel_LJ))
Sel_LJ = Mutate(Sel_LJ, Pm)  # 变异后的路径
# 变异后的最优解
p_len = pathlength(D, Sel_LJ)
# fitnv=fit(p_len)
index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号
# print(index)
print(Sel_LJ[index])
num = "初始变异后的最优解"
draw_path = drawpath(Sel_LJ[index], city_zb, num)
plt.text(40, 37, "总长度=")
plt.text(42, 37, str(int(1000 * p_len[index]) / 1000))
# print(np.sort(Sel_LJ[index]))
# print(Sel_LJ[index])

# print("Sel_LJ=",Sel_LJ.shape)
# print(type(Sel_LJ))

# 逆转操作：
# 全部被选中种子均参加逆转操作
# 逆转后适应度大的将替换原选择种子
# 输入种子Sel_LJ及D
# 输出新的选择集Sel_LJ
def Reverse(Sel_LJ, D):
    ZQS, n = Sel_LJ.shape
    Sel_LJ = np.array(Sel_LJ)
    p_len = pathlength(D, Sel_LJ)
    Sel_LJ1 = np.copy(Sel_LJ)
    for i in range(ZQS):
        # r=np.random.randint(n,size=2) #有重复的可能性
        # r.sort()                #产生2个不相等的0到n-1的整数
        # r_min=r[0]
        # if r_min==0:
        # r_min=1
        # r_max=r[1]

        # 换成下面代码，保证不重复
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
    p_len1 = pathlength(D, Sel_LJ1)
    # %计算路径长度
    index = p_len1 < p_len
    Sel_LJ[index, :] = Sel_LJ1[index, :]
    return Sel_LJ


Sel_LJ = Reverse(Sel_LJ, D)

print(Sel_LJ)


# 逆转后的最优解
p_len = pathlength(D, Sel_LJ)
# fitnv=fit(p_len)
index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号
# print(index)
# print(Sel_LJ[index])
num = "初始逆转后的最优解"
draw_path = drawpath(Sel_LJ[index], city_zb, num)
plt.text(40, 37, "总长度=")
plt.text(42, 37, str(int(1000 * p_len[index]) / 1000))
# print(np.sort(Sel_LJ[index]))
# print(Sel_LJ[index])


# 重新产生新种群
# 输入原种群LJ
# 输入经过遗传操作后的优势种群Sel_LJ
# 输出新的种群LJ1
def newLJ(LJ, Sel_LJ, D):
    ZQS, n = LJ.shape
    sel_num = len(Sel_LJ)
    p_len = pathlength(D, LJ)
    tem_p = []
    for i, e in enumerate(p_len):
        tem_p.append((i, e))
    z = sorted(tem_p, key=lambda x: x[1])  # 按p_len大小排序
    index = [id[0] for id in z]  # 获得从小到大排序的原p_len数组的序号
    LJ1 = np.copy(LJ)
    LJ1[0 : ZQS - sel_num - 1, :] = LJ[index[0 : ZQS - sel_num - 1], :]
    LJ1[ZQS - sel_num : ZQS, :] = Sel_LJ
    return LJ1


LJ = newLJ(LJ, Sel_LJ, D)
# print(LJ)
# print(np.sort(LJ))

# 完成第一代遗传优化操作，进入循环操作
start_time = time.process_time()
gen = 0  # 遗传代数
# pre_obj=p_len(index) 为上一轮最优
print(gen, pre_obj)
plt.figure(num="优化路径距离和遗传代数关系")

while gen <= Maxgen:
    p_len = pathlength(D, LJ)  # 计算路径长度
    index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号
    obj = p_len[index]
    plt.plot([gen, gen + 1], [pre_obj, obj], lw=2,clip_on=False)
    pre_obj = obj
    # 选择操作
    fitnv = fit(p_len)
    Sel_LJ = select(LJ, Sel_ra, fitnv)  # LJ由上一代带入
    # 交叉重组操作
    Sel_LJ = Re_com(Sel_LJ, Pc)
    # 变异操作
    Sel_LJ = Mutate(Sel_LJ, Pm)
    # 逆转操作
    Sel_LJ = Reverse(Sel_LJ, D)
    # 新种子重组，保证上一轮最优解遗传给下一代
    LJ = newLJ(LJ, Sel_LJ, D)
    gen = gen + 1
    if (gen/30-int(gen/30))<=0.01:
        print("gen=",gen)
plt.xlabel("遗传代数")
plt.ylabel("路径长度")
plt.title("优化路径距离和遗传代数关系")
plt.grid()
# 绘制最后最优解，并打印路线图
# 绘制初始优化图
num = "绘制最终优化图"
draw_path = drawpath(LJ[index, :], city_zb, num)
# plt.legend(str(p_len[0]))
plt.text(40, 102, "总长度=")
plt.text(50, 102, str(int(1000 * p_len[index]) / 1000))

# plt.text(35, 32, "总长度=")
# plt.text(39, 32, str(int(1000 * p_len[index]) / 1000))


# 打印最终优化路径
print_LJ = str()
for i in range(n):
    print_LJ = print_LJ + str(LJ[index, i] + 1) + "-->"
print_LJ = print_LJ + str(LJ[index, 0] + 1)
print(print_LJ)
end_time = time.process_time()
print("process_time程序运行计时=", end_time - start_time)
plt.show()