# 蚁群算法 Ant Colony Algorithm #


import numpy as np
from numpy.core.fromnumeric import cumsum
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

# 参数初始化
"""
n:城市数目
m: 蚂蚁个数
alpha :表征信息素重要程度的参数
beta :表征启发式因子重要程度的参数
rho :信息素蒸发系数
itera_max： 最大迭代次数
city_zb:城市坐标
Q： 信息素增加强度系数
LJ_best[itera_max,n]: 各代最佳路线
pen_best[itera_max]: 各代最佳路线的长度
eta:启发因子，取距离的倒数
LJ[m,n]:路径记录
tau[n,n]:信息素矩阵
ran_ant:不受信息素影响的随机蚂蚁数

"""
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

# 固定城市坐标
# 读入城市坐标
DF = pd.read_excel("city.xlsx", "Sheet1", na_filter=False, index_col=0)  # 共有31个城市坐标
city_x = np.array(DF["x"])  # 数据分配
city_y = np.array(DF["y"])
n = len(city_x)  # 计算城市的数目
city_zb = np.zeros((n, 2))  # 设置坐标数组
city_zb[:, 0] = city_x / 100
city_zb[:, 1] = city_y / 100

# city_zb=city_zb(50,50,50)#确定城市数目及坐标

# 计算城市i和城市j之间的距离
# 输入 city_zb 各城市的坐标,用city_zb[i,0:1])
# 输出 D 城市i和城市j之间的距离,用D[i,j]表示
n = len(city_zb)


def Distance(city_zb):
    D = np.zeros((n, n))  #  产生两城市之间距离数据的空矩阵即零阵
    for i in range(n):
        D[i, i] = 10e-4  # 计算信息素时要用到
        for j in range(i + 1, n):
            D[i, j] = (
                (city_zb[i, 0] - city_zb[j, 0]) ** 2
                + (city_zb[i, 1] - city_zb[j, 1]) ** 2
            ) ** 0.5
            D[j, i] = D[i, j]
    return D


D = Distance(city_zb)  # 计算一次即可
m = int(1.3 * n)  # 确定蚂蚁数
alpha = 1.5
beta = 4
rho = 0.08
itera_max = 500
Q = 1
ran_ant = 0
LJ_best = np.zeros((itera_max, n))  # 各代最佳路线
pen_best = np.zeros(itera_max)  # 各代最佳路线的长度
eta = 3.0 / D  # 启发因子，取距离的倒数
LJ = np.zeros((m, n))  # 路径记录
tau = np.ones((n, n))  # 信息素矩阵
# print(n)
# print(city_zb)
# print(eta)
# 计算城市之间的距离


# 产生初始蚂蚁轨迹LJ0用以验证绘制程序的正确性
def path(n):
    li = np.arange(0, n)
    LJ = np.zeros(n)
    rnd.shuffle(li)
    LJ[:] = li
    return LJ.astype(int)  # 需要强制转变成整数


LJ0 = path(n)


# 绘制初始路径图
# 画路径函数
def drawpath(LJ, city_zb, num):
    """
    #画路径函数
    #输入
    LJ: 待画路径
    city_zb: 各城市坐标位置
    num: 图片左上角的图名
    """
    plt.figure(num=num)
    n = len(LJ)
    plt.scatter(
        city_zb[:, 0], city_zb[:, 1], marker="o", color="b", s=100
    )  # 所有城市位置上画上o
    plt.text(city_zb[LJ[0], 0] + 0.5, city_zb[LJ[0], 1] + 0.5, "起点")
    plt.text(city_zb[LJ[n - 1], 0] + 0.5, city_zb[LJ[n - 1], 1] + 0.5, "终点")
    for i in range(n):
        plt.text(city_zb[i, 0] - 0.3, city_zb[i, 1] + 0.5, str(i + 1), color="r")
    # 绘线
    xy = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
    xytext = (city_zb[LJ[1], 0], city_zb[LJ[1], 1])
    plt.annotate(
        "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="g", lw=2)
    )
    for i in range(1, n - 1):
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
    # plt.ylim(0,40)
    # plt.xlim(10,50)
    plt.ylim(-5, 55)
    plt.xlim(-5, 55)
    plt.grid()
    plt.xlabel("横坐标")
    plt.ylabel("纵坐标")
    plt.title(" 轨迹图")


# 路径长度计算
def pathlength(D, LJ):
    N = D.shape[1]
    p_len = 0
    for j in range(N - 1):
        p_len = p_len + D[LJ[j], LJ[j + 1]]
    p_len = p_len + D[LJ[N - 1], LJ[0]]
    return p_len


p_len = pathlength(D, LJ0)
print(p_len)


# 绘制初始路径1
num = "绘制初始路径"
draw_path = drawpath(LJ0, city_zb, num)
# plt.legend(str(p_len[0]))
plt.text(22, 33, "总长度=" + str(int(1000 * p_len) / 1000))

# 打印路径
def print_way(LJ):
    print_LJ = str()
    n = len(LJ)
    for i in range(n):
        print_LJ = print_LJ + str(LJ[i] + 1) + "-->"
    print_LJ = print_LJ + str(LJ[0] + 1)
    print(print_LJ)


print("初始路径")
print_way(LJ0)

# 开始迭代计算
itera_num = 0
while itera_num < itera_max:
    # 随机产生每只蚂蚁的起点城市序号0~n-1
    start = np.zeros(m)
    # itera_num=itera_num+1
    for i in range(m):
        start[i] = rnd.randint(0, n - 1)
    start = start.astype(int)
    # print(start)
    LJ[:, 0] = start
    LJ = LJ.astype(int)
    # print(LJ[:,0])
    # print("len(LJ[:,0]=",len(LJ[:,0]))
    city_id = np.arange(n)
    # print(city_id)
    p_len = np.zeros(m)  # 每只蚂蚁的总路径长度初始化
    for i in range(m):  # m只蚂蚁逐个城市选择路径
        for j in range(1, n):
            prohi_tab = LJ[i, 0:j]  # 禁止表 prohibit_table
            allow = list(set(city_id).difference(set(prohi_tab)))
            P = np.zeros(len(allow))  # []#建立初始空数据
            # P=allow[:]
            # print("p=",P)
            # print(len(allow))
            # print(len(P))
            for k in range(len(allow)):
                # print(prohi_tab[j-1],allow[k])
                P[k] = (
                    tau[prohi_tab[j - 1], allow[k]] ** alpha
                    + eta[prohi_tab[j - 1], allow[k]] ** beta
                )
                # tem_P=tau[prohi_tab[j-1],allow[k]]**alpha+eta[prohi_tab[j-1],allow[k]]**beta
                # P.append(tem_P)
            # print("k=",k)
            # print("allow[k]=",allow[k])
            # print("J=",j)
            # print("k=",k)
            P = P / sum(P)
            # print(P)
            Pc = cumsum(P)
            # print(Pc)
            # Pc=P
            tar_id = [i for i, tp in enumerate(Pc) if tp > np.random.random()]
            tar = allow[tar_id[0]]
            LJ[i, j] = tar
        # print("LJ=",LJ[i,:])
        if i >= m - ran_ant:  # ran_ant=3
            LJ[i, :] = path(n)
            # print("LJ(m-1)",LJ[m-1,:])#每轮循环放三只随机蚂蚁，不受信息素影响，以便跳出局部最优解

        p_len[i] = pathlength(D, LJ[i, :])
    id_ant = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径的蚂蚁序号

    pen_best[itera_num] = p_len[id_ant]  # 各代最佳路线的长度
    LJ_best[itera_num, :] = LJ[id_ant, :]  # 各代最佳路线
    # print(LJ[i,:])
    # print(len(LJ[i,:]))
    detal_tau = np.zeros((n, n))
    for i in range(m):
        for j in range(n - 1):
            detal_tau[LJ[i, j], LJ[i, j + 1]] = (
                detal_tau[LJ[i, j], LJ[i, j + 1]] + Q / p_len[i]
            )
            # detal_tau[LJ[i,j+1],LJ[i,j]]=detal_tau[LJ[i,j+1],LJ[i,j]]+Q/ p_len[i]
        detal_tau[LJ[i, n - 1], LJ[i, 0]] = (
            detal_tau[LJ[i, n - 1], LJ[i, 0]] + Q / p_len[i]
        )  # 最后一个点和起始点闭合
        # detal_tau[LJ[i,0],LJ[i,n-1]]=detal_tau[LJ[i,0],LJ[i,n-1]]+Q/ p_len[i]

    # 最优蚂蚁路线加强：
    for j in range(n - 1):
        detal_tau[LJ[id_ant, j], LJ[id_ant, j + 1]] = (
            detal_tau[LJ[id_ant, j], LJ[id_ant, j + 1]] + 9
        )
        # detal_tau[LJ[i,j+1],LJ[i,j]]=detal_tau[LJ[i,j+1],LJ[i,j]]+Q/ p_len[i]
    detal_tau[LJ[id_ant, n - 1], LJ[id_ant, 0]] = (
        detal_tau[LJ[id_ant, n - 1], LJ[id_ant, 0]] + 9
    )

    # ran_ant只随机蚂蚁信息素也加强
    # for i in range(ran_ant):
    # for j in range(n-1):
    # detal_tau[LJ[m-i-1,j],LJ[m-i-1,j+1]]=detal_tau[LJ[m-i-1,j],LJ[m-i-1,j+1]]+0.1
    # detal_tau[LJ[i,j+1],LJ[i,j]]=detal_tau[LJ[i,j+1],LJ[i,j]]+Q/ p_len[i]
    # detal_tau[LJ[m-i-1,n-1],LJ[m-i-1,0]]=detal_tau[LJ[m-i-1,n-1],LJ[m-i-1,0]]+0.1
    # 实验表明随机的加强效果不好，最短距离只能到160左右
    tau = (1 - rho) * tau + detal_tau  # 更新信息素
    # print("tau=",tau)
    itera_num = itera_num + 1
    LJ = np.zeros((m, n))  # 路径记录清空
id_best = list(pen_best[:]).index(min(pen_best[:]))  # 找到最短距离路径的迭代序号
print(LJ_best[id_best, :].astype(int))
LJ_end = LJ_best[id_best, :].astype(int)
print("最优路径")
print_way(LJ_end)

num = "绘制最后路径"
draw_path = drawpath(LJ_end, city_zb, num)
plt.text(22, 52, "总长度=" + str(int(1000 * pen_best[id_best]) / 1000))
plt.figure(num="优化路径距离迭代次数关系图")
for i in range(itera_max - 1):
    plt.plot([i, i + 1], [pen_best[i], pen_best[i + 1]])
plt.xlabel("迭代次数")
plt.ylabel("路径长度")
plt.title("优化路径距离和迭代次数关系")
plt.grid()


plt.show()
