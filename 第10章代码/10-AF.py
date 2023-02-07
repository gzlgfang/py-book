#!/usr/bin/env python3
##人工鱼群算法

import numpy as np
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
## 调试用 X=np.array([[1,2,3],[2,3,4],[4,6,7],[9,3,2],[6,12,4]])
## 每条鱼的食物浓度Food concentration（Food_con)计算，其实就是目标函数值以求极大为例，求极小，将目标函数反转即可
def Food_con(X):  ##X 是矩阵向量，行数是鱼群数量，列数是每条鱼位置的维度数
    n = np.shape(X)[0]
    Y = np.zeros(n)
    x1 = X[:, 0]
    x2 = X[:, 1]
    x3 = X[:, 2]
    # Y[:] = (
    # 3 * (x1 - 5) ** 2 + 6 * (x2 - 6) ** 2 + (x3 - 4) ** 2
    # )  ##根据具体目标函数定义，Y是一维向量，数目为鱼群数量
    Y[:] = (
        (x1**1.2 + x1**0.5 * x2**0.9 + x2 * x3**0.9 - 0.8) ** 2
        + (x1**0.8 + x2**1.2 * x3 + x1 * x3**1.1 - 0.8) ** 2
        + (x1 * x2 * 1.1 + x2 * x3 + x3**1.5 - 0.8) ** 2
    )
    # R = x1**2 + x2**2
    # Y[:] = 20 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2)) - R - 20
    return -Y  ## 求极小值，目标反转


def Food_con_1(X):  ##X是每条鱼位置,求单条鱼的目标函数即浓度
    n = len(X)
    Y = np.zeros(1)
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    """ Y[:] = (
        3 * (x1 - 5) ** 2 + 6 * (x2 - 6) ** 2 + (x3 - 4) ** 2
    )  ##根据 """  ##具体目标函数定义，Y是一维向量，数目为鱼群数量

    Y[:] = (
        (x1**1.2 + x1**0.5 * x2**0.9 + x2 * x3**0.9 - 0.8) ** 2
        + (x1**0.8 + x2**1.2 * x3 + x1 * x3**1.1 - 0.8) ** 2
        + (x1 * x2 * 1.1 + x2 * x3 + x3**1.5 - 0.8) ** 2
    )
    """ R = x1**2 + x2**2
    Y[:] = 20 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2)) - R - 20 """
    return -Y


# X = np.array([[1, 2, 3], [2, 3, 4], [4, 6, 7], [9, 3, 2], [6, 12, 4]])
# Y = Food_con(X)
# print(Y)
# X1 = np.array([5, 6, 4])
# Y1= Food_con_1(X1)
# print("Y1=",Y1)
## 调试用 X=np.array([[1,2,3],[2,3,4],[4,6,7],[9,3,2],[6,12,4]])
def Distance(Xi, X):  ##计算第Xi条鱼和其他所有鱼之间的距离
    n = len(X)
    D = np.zeros(n)
    for j in range(n):
        D[j] = np.sqrt(np.sum((Xi - X[j]) ** 2))
    return D


##  Di_j=Distance(X[2],X)
##  print(Di_j) 调试用


def Inital_AF(NumF, lb_ub):  ##产生鱼群初始位置
    ## 输入变量
    ##NumF： 鱼群大小
    ##lb_ub： 鱼的活动范围
    ##输出变量
    ##X：产生初始人工鱼群的位置向量
    row = np.shape(lb_ub)[0]
    col = np.shape(lb_ub)[1]
    X = np.zeros([NumF, col])

    for i in range(NumF):
        for j in range(col):
            lb = lb_ub[0, j]
            ub = lb_ub[1, j]
            X[i, j] = lb + (ub - lb) * rnd.random()
    return X


##调试时用
##NumF=8;
## lb_ub=np.array([[-5,8,2],[4.3,8,1]]);
##这里的lb_ub是2行3列的矩阵，第1行是鱼群位置范围的上限，第2行是鱼群位置范围的下限。每一行数据的数目表示维度
NumF = 20
# lb_ub = np.array([[-1, -1, -1], [10, 10, 10]])  ##第一行数据为下限，第二行数据为上限，列数为位置维度
lb_ub = np.array([[0, 0, 0], [1, 1, 1]])
# lb_ub = np.array([[-5, -5], [5, 5]])
XX = Inital_AF(NumF, lb_ub)
lu_dis = np.sqrt(np.sum((lb_ub[0, :] - lb_ub[1, :]) ** 2)) / 10
step = 0.2 * lu_dis
visual = 0.5
try_N = 30
last_Y = Food_con(XX)
print(last_Y)
##觅食行为，Find food（Find_food),为每条鱼计算下一个位置及浓度 Xnext[Ynext]
def Find_food(Xi, Fi, visual, step, try_N, last_Y, lb_ub):
    # 输入参数：
    # Xi           当前人工鱼的位置
    # Fi            当前人工鱼的序号
    # visual       感知范围
    # step         最大移动步长
    # try_N        最大尝试次数
    # lastY        上次的各人工鱼位置的食物浓度即求极大值的函数值
    # lb_ub        鱼坐标位置的上下限
    # 输出参数：
    #%Xnext       Xi人工鱼的下一个位置
    # Ynext        Xi人工鱼的下一个位置的食物浓度
    flag = True
    Xnext = np.zeros(1)
    Yi = last_Y[Fi - 1]  ##从0开始排序号
    n = len(Xi)  ##鱼的位置维度数
    for i in range(try_N):
        Xj = Xi + (2 * np.random.random(n) - 1) * visual
        for k in range(n):
            if Xj[k] < lb_ub[0, k]:
                Xj[k] = lb_ub[0, k]
            if Xj[k] > lb_ub[1, k]:
                Xj[k] = lb_ub[1, k]

        Yj = Food_con_1(Xj)
        if Yi < Yj:
            Xnext = Xi + np.random.random() * step * (Xj - Xi) / np.sqrt(
                np.sum((Xj - Xi) ** 2)
            )
            for k in range(n):
                if Xnext[k] < lb_ub[0, k]:
                    Xnext[k] = lb_ub[0, k]
                if Xnext[k] > lb_ub[1, k]:
                    Xnext[k] = lb_ub[1, k]

            Xi = Xnext  ##此句似乎可以不要
            flag = False  ##只要有一次尝试成功即可
            break
    ##随机行为,全部尝试都不成功才发生随机行为
    if flag == True:
        Xj = Xi + (2 * np.random.random(n) - 1) * visual
        Xnext = Xj
    for k in range(n):
        if Xnext[k] < lb_ub[0, k]:
            Xnext[k] = lb_ub[0, k]
        if Xnext[k] > lb_ub[1, k]:
            Xnext[k] = lb_ub[1, k]

    Ynext = Food_con_1(Xnext)  ##可以考虑放在主程序上，只要返回Xnext，Ynext在主程序中调用Food_con_1(Xnext)
    return [Xnext, Ynext]


Fi = 15
Xi = XX[Fi - 1, :]
Xnext, Ynext = Find_food(Xi, Fi, visual, step, try_N, last_Y, lb_ub)
print("觅食=", Xnext, Ynext)
deta = 0.618
##群聚行为
def cluster_AF(X, Fi, visual, step, deta, try_N, last_Y, lb_ub):

    # 输入参数：
    # X            所有人工鱼的位置
    # Fi           当前人工鱼的序号
    # visual       感知范围
    # step         最大移动步长
    # try_N        最大尝试次数
    # detal         鱼群拥挤度
    # lastY        上次的各人工鱼位置的食物浓度即求极大值的函数值
    # try_number   最大尝试次数
    # lb_ub        鱼坐标位置的上下限
    # 输出参数：
    #%Xnext       Xi人工鱼的下一个位置
    # Ynext        Xi人工鱼的下一个位置的食物浓度

    Xi = X[Fi - 1, :]
    D = Distance(Xi, X)
    # print("D=",D)
    F_num = len(D)  ##鱼群数量
    n = len(Xi)  ##鱼位置维度数
    index = []
    Xc = np.zeros(n)
    for i in range(F_num):
        if D[i] > 0 and D[i] < visual:
            # k=list(x[:]).index(x[:]=x[i]
            index.append(i)
    # print(index)
    nf = len(index)
    if nf > 0:  ##附近有符合条件的鱼，求这些鱼的中心位置
        for j in range(n):
            Xc[j] = xc = np.mean(X[index, j])
        Yc = Food_con_1(Xc)
        Yi = last_Y[Fi - 1]
        if Yc / nf > deta * Yi:
            Xnext = Xi + np.random.random() * step * (Xc - Xi) / np.sqrt(
                np.sum((Xc - Xi) ** 2)
            )
            ##norm(Xc-Xi);
            for k in range(n):
                if Xnext[k] < lb_ub[0, k]:
                    Xnext[k] = lb_ub[0, k]
                if Xnext[k] > lb_ub[1, k]:
                    Xnext[k] = lb_ub[1, k]
            Ynext = Food_con_1(Xnext)
        else:
            [Xnext, Ynext] = Find_food(Xi, Fi, visual, step, try_N, last_Y, lb_ub)

    else:
        [Xnext, Ynext] = Find_food(Xi, Fi, visual, step, try_N, last_Y, lb_ub)
    return [Xnext, Ynext]


Xnext, Ynext = cluster_AF(
    XX, Fi, visual, step, deta, try_N, last_Y, lb_ub
)  ##XX其实就是程序中的X
print("群聚=", Xnext, Ynext)  # 调试时用


def follow_AF(X, Fi, visual, deta, step, try_N, last_Y, lb_ub):

    ## 追尾行为
    # 输入参数：
    # X            所有人工鱼的位置
    # Fi           当前人工鱼的序号
    # visual       感知范围
    # step         最大移动步长
    # try_N        最大尝试次数
    # lastY        上次的各人工鱼位置的食物浓度即求极大值的函数值
    # try_number   最大尝试次数
    # lb_ub        鱼坐标位置的上下限
    # 输出参数：
    #%Xnext       Xi人工鱼的下一个位置
    # Ynext        Xi人工鱼的下一个位置的食物浓度
    Xi = X[Fi - 1, :]
    D = Distance(Xi, X)
    # print("D=",D)
    F_num = len(D)  ##鱼群数量
    n = len(Xi)  ##鱼位置维度数
    index = []
    Xc = np.zeros(n)
    for i in range(F_num):
        if D[i] > 0 and D[i] < visual:
            index.append(i)
    # print(index)
    nf = len(index)
    if nf > 0:
        X_index = X[index, :]
        Y_index = last_Y[index]
        Max_Y_id = list(Y_index[:]).index(max(Y_index[:]))
        Ymax = max(Y_index[:])  ##视野范围内的最大浓度
        Xmax = X_index[Max_Y_id, :]  ##浓度最大处的位置数据
        Yi = last_Y[Fi - 1]

        if Ymax / nf > deta * Yi:  ##向高浓度方向移动
            Xnext = Xi + np.random.random() * step * (Xmax - Xi) / np.sqrt(
                np.sum((Xmax - Xi) ** 2)
            )
            ##norm(Xc-Xi);
            for k in range(n):
                if Xnext[k] < lb_ub[0, k]:
                    Xnext[k] = lb_ub[0, k]
                if Xnext[k] > lb_ub[1, k]:
                    Xnext[k] = lb_ub[1, k]
            Ynext = Food_con_1(Xnext)
        else:
            [Xnext, Ynext] = Find_food(Xi, Fi, visual, step, try_N, last_Y, lb_ub)

    else:
        [Xnext, Ynext] = Find_food(Xi, Fi, visual, step, try_N, last_Y, lb_ub)
    return [Xnext, Ynext]


Xnext, Ynext = follow_AF(
    XX, Fi, visual, step, deta, try_N, last_Y, lb_ub
)  ##XX其实就是程序中的X
print("追尾=", Xnext, Ynext)

##主程序迭代
start_time = time.process_time()
gen = 0
##重新设置计算参数
NumF = 60  ##生成60只人工鱼
# lb_ub = np.array([[0.01, 0.01, 0.01], [1, 1, 1]])  ##三维位置上下限
# lb_ub = np.array([[-5, -5], [5, 5]])
Maxgen = 200  ##最多迭代次数
try_N = 200  ##最多试探次数
visual = 0.5  ##感知距离
deta = 0.618  ##拥挤度因子
step = 0.1  ##步长
##初始化鱼群
XX = Inital_AF(NumF, lb_ub)
BestY = np.ones(Maxgen)  ##每次迭代中最优的函数值
BestX = np.zeros([Maxgen, 3])  ##每步中最优的自变量
# BestX = np.zeros([Maxgen, 2])
besty = -800  ##最优函数值
Y = Food_con(XX)  ##初始化鱼群个鱼的函数值即浓度

while gen <= Maxgen - 1:
    for i in range(NumF):
        ## 聚群行为
        Fi = i + 1
        Xi1, Yi1 = cluster_AF(XX, Fi, visual, step, deta, try_N, Y, lb_ub)
        ## 追尾行为
        Xi2, Yi2 = follow_AF(XX, Fi, visual, step, deta, try_N, Y, lb_ub)
        if Yi1 > Yi2:
            XX[Fi - 1, :] = Xi1
            Y[Fi - 1] = Yi1
        else:
            XX[Fi - 1, :] = Xi2
            Y[Fi - 1] = Yi2
    Max_id = list(Y[:]).index(max(Y[:]))
    # print(Max_id)
    Ymax = max(Y[:])  ##本次迭代最大值
    Xmax = XX[Max_id, :]  ##浓度最大处的位置数据

    if Ymax > besty:
        besty = Ymax
        bestx = Xmax
        BestY[gen] = Ymax
        BestX[gen, :] = Xmax
    else:
        BestY[gen] = BestY[gen - 1]  ##用上一轮迭代的最优解
        BestX[gen, :] = BestX[gen - 1, :]
    gen = gen + 1

bestyy = max(BestY)
id = list(BestY[:]).index(max(BestY[:]))
bestxx = BestX[id, :]

plt.figure(num="优化目标和迭代次数关系图")
x = np.arange(0, Maxgen)
y = BestY
plt.plot(x, y, lw=2, clip_on=False)
plt.xlabel("迭代代数")
plt.ylabel("目标函数")
plt.title("鱼群算法迭代过程")
plt.grid()

print("最优目标函数值=", bestyy)
print("最优鱼个体位置=", bestxx)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")
x = BestX[:, 0]
y = BestX[:, 1]
z = BestX[:, 2]
c = BestY
p = ax.scatter(x, y, z, c=c, cmap=mpl.cm.RdYlBu, marker="o", s=500, zdir="z")
fig.colorbar(p, ax=ax, shrink=0.5)
ax.set_xlabel("$x$", labelpad=10, fontsize=16)
ax.set_ylabel("$y$", labelpad=10, fontsize=16)
ax.set_zlabel("$z$", labelpad=10, fontsize=16)
ax.set_title("鱼群算法迭代过程最优点位置移动")

ax.text(
    bestxx[0] - 0.04,
    bestxx[1] - 0.04,
    bestxx[2],
    f"最优点位置坐标x={bestxx[0]:.5f}, y={bestxx[1]:.5f}, z={bestxx[2]:.5f}",
    zdir="x",
)

ax.text(
    bestxx[0] - 0.05, bestxx[1] - 0.05, bestxx[2], f"最优点函数值J={bestyy:.5f}", zdir="x"
)
print(BestY)
end_time = time.process_time()
print("process_time程序运行计时=", end_time - start_time)
plt.show()
