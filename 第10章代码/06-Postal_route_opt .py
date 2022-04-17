# Postal route optimization
# 06-Postal_route_opt 
#已知邮局位置坐标P_x,P_y,邮局负责N个投递点，每个投递点的邮件重量为w[i]，位置坐标city_x,city_y
#邮件数据放在city_x,city_y数据的第一行位置，后面N行为投递点位置坐标数据，方便后续程序处理

#!/usr/bin/env python3
# 用 05-Simulated annealing TSP 框架改进
#
from typing import Type
from matplotlib import colors, markers
import numpy as np
from numpy.core.numeric import tensordot
import copy
import pandas as pd
import random as rnd
import time

# 绘图设置
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
mpl.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
# 模拟退火基础参数：
from scipy import optimize
global T0, q, Tend, T
T0 = 3800  # 初始温度
Tend = 0.0005  # 最终温度
L = 480  # 链长，每次稳定温度下优化次数
q = 0.93  # 温度下降速率
def fun(x):
    return T0 * q ** x[0] - Tend
T_num = int(optimize.fsolve(fun, [30]) + 2)  # 计算退火次数
# 读入城市坐标
DF = pd.read_excel("g:/Postal.xlsx", "Sheet1", na_filter=False, index_col=0)  # 共有31个城市坐标
city_x = np.array(DF["x"])  # 数据分配
city_y = np.array(DF["y"])
w1=np.array(DF["w"])
n = len(city_x)-1  # 计算投递点的数目
w=w1[1:]#读入每个投递点的投递重量
TG=sum(w)
print("总邮件重量=",TG)

city_zb = np.zeros((n+1, 2))  # 设置坐标空数组
city_zb[:, 0] = city_x #city_zb[0, :]为邮局位置坐标
city_zb[:, 1] = city_y 

test_num=3
opt_JJ=np.zeros(test_num)
opt_way=np.zeros((test_num,n))
#计算两地距离
def Distance(city_zb):
    n=len(city_x)#其实是n+1
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

#定义绘制函数
def drawpath(LJ, city_zb, num):
    plt.figure(num=num)
    n = len(LJ)
    print("n=",n)
    plt.scatter(
        city_zb[:, 0], city_zb[:, 1], marker="o", color="b", s=100
    )  # 所有城市位置上画上o
    plt.text(city_zb[0, 0] + 0.5, city_zb[0, 1] + 0.5, "邮局")
    plt.text(city_zb[LJ[0], 0] + 0.5, city_zb[LJ[0], 1] + 0.5, "起点")
    plt.text(city_zb[LJ[n - 1], 0] + 0.5, city_zb[LJ[n - 1], 1] + 0.5, "终点")
    
    plt.text(city_zb[0, 0] - 0.3, city_zb[0, 1] + 0.5, str(0), color="r")#邮局放置0号
    for i in range(n):#0-n-1
        # plt.text(city_zb[LJ[i],0]-0.3,city_zb[LJ[i],1]+0.5,str(i+1),color="r")
        plt.text(city_zb[i+1, 0] - 0.3, city_zb[i+1, 1] + 0.5, str(i+1), color="r")
    # 绘线
    xy = (city_zb[0, 0], city_zb[0, 1])
    xytext = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
    plt.annotate(
        "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="r", lw=3)
    )#邮局到起点
    
    for i in range(n-1):
        # x=[city_zb[LJ[i],0],city_zb[LJ[i+1],0]]
        # y=[city_zb[LJ[i],1],city_zb[LJ[i+1],1]]
        # plt.plot(x,y,lw=2,c="r")
        xy = [city_zb[LJ[i], 0], city_zb[LJ[i], 1]]
        xytext = [city_zb[LJ[i + 1], 0], city_zb[LJ[i + 1], 1]]
        plt.annotate(
            "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="g", lw=2)
        )

    xy = (city_zb[LJ[n - 1], 0], city_zb[LJ[n - 1], 1])
    xytext = (city_zb[0, 0], city_zb[0, 1])
    plt.annotate(
    "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="r", lw=3)
    )
    plt.grid()
    plt.xlabel("横坐标")
    plt.ylabel("纵坐标")
    plt.title(" 轨迹图")
#定义计算目标函数
def pathlength(D, LJ):
    n = D.shape[1]-1#多了一个邮局
    ZQS = 1
    p_len = np.zeros(ZQS)
    for i in range(ZQS):
        p_len[i]=D[0,LJ[0]]*TG#邮局到第一个投递点的距离与总总量之和
        TW=TG
        for j in range(n - 1):
            TW=TW-w[j]
            #TW=1
            p_len[i] = p_len[i] + D[LJ[j], LJ[j + 1]]*TW
        p_len[i] = p_len[i] + D[LJ[n - 1], 0]#最后一个投递点返回邮局,无重量
    return p_len
#p_len = pathlength(D, LJ0)

# 定义打印路径
def print_way(LJ):
    print_LJ = str()
    n = len(LJ)
    print_LJ="邮局Post-->"
    for i in range(n):
        print_LJ = print_LJ + str(LJ[i] ) + "-->"
    print_LJ = print_LJ + "邮局Post"
    print(print_LJ)

#进入模拟退火算法
def Newpath(LJ):
    # 有原来的旅行轨迹LJ1计算产生新的旅行轨迹LJ2(部分逆转）
    # 输入 LJ1 原来的旅行轨迹，是0到N-1城市的数字排列
    # 输出 LJ2 新的旅行轨迹,逆转扰动
    N = len(LJ)  # 计算城市的数目
    LJ2 =copy.deepcopy(LJ)  # 先将原轨迹全部复制到新轨迹
    flags = True
    while flags:
        r1 = rnd.randint(0, n-1 )  # 随机产生一个0：n-1的整数
        r2 = rnd.randint(0, n-1 )  # 随机产生一个0：n-1的整数
        if r1 != r2:
            flags = False
        if r1 > r2:
            r_min, r_max = r2, r1
        else:
            r_min, r_max = r1, r2
        if r_min == 0:
            r_min = 1
        
        #轨迹逆转       
        LJ2[r_min : r_max + 1] = LJ[r_max : r_min - 1 : -1]
        #互换位置
        #LJ2[r_min] = LJ[r_max]
        #LJ2[r_max] = LJ[r_min]
    return LJ2
# 判断新路径是否被采用
def Metropolis(LJ0, LJ2, D, T):
    Len1 = pathlength(D, LJ0)  # 计算轨迹LJ0路径长度
    Len2 = pathlength(D, LJ2)  # 计算轨迹LJ2路径长度
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

for test in range(test_num): 
    T0 = 3800  # 初始温度
    def path(n):
        li = np.arange(1, n+1)#产生1-n的整数
        LJ = np.zeros(n)
        rnd.shuffle(li)
        LJ[:] = li
        return LJ.astype(int)  # 需要强制转变成整数
    LJ0 = path(n)
    #print(LJ0)
    #print(len(city_x))
    # 绘制初始路径图
    # 画路径函数
    # 输入
    # LJ 待画路径
    # city_zb 各城市坐标位置
    # num为图片左上角的图名
    
    
    p_len = pathlength(D, LJ0)
    
    LJ2 = Newpath(LJ0)
    p_len = pathlength(D, LJ2)
    
    
    [LJ0, Len] = Metropolis(LJ0, LJ2, D, T0)
    count = 0
    LJ0 = LJ0.astype(int)
    # 初始化设置及函数定义工作完成，进入主程序迭代
    # print(Len)
    #print_way(LJ0)
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
        #obj1[count] = opt_sd
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
    print("第" ,(test+1), "次实验最优路径")
    print_way(LJ0)
    p_len = pathlength(D, LJ0)
    print("最优目标函数=",p_len[0])
    # num = "绘制最优路径"
    # draw_path = drawpath(LJ0, city_zb, num)
    # # plt.legend(str(p_len[0]))
    # plt.text(25, 25, "总长度=")
    # plt.text(27, 25, str(int(1000 * p_len) / 1000))
    opt_JJ[test]=p_len[0]
    opt_way[test,:]=LJ0



    # plt.figure(num="优化路径距离和退火次数关系图")
    # for i in range(1, T_num - 1):
    #     plt.plot([i, i + 1], [obj1[i], obj1[i + 1]])

    #plt.show()


#print(opt_JJ)
opt_way=opt_way.astype(int)
#print(opt_way)
#寻找全部实验中是最优解：
#find opt_JJ elements minizmation 
#fmin=min(opt_JJ[:])#确定最小值
index=list(opt_JJ[:]).index(min(opt_JJ[:]))#确定最小值所在的位置
#print(index)
print("全部实验中是最优解")
print(opt_JJ[index])
opt_way=opt_way.astype(int)
#最优路径
print_way(opt_way[index])

plt.figure(num="实验序号和最优目标函数关系图")
x=np.arange(1,test_num+1)
y=opt_JJ
plt.plot(x, y,color="b",label="目标函数值" ,linewidth=2.0, linestyle="--" )
#plt.xticks(np.linspace(0,test_num,test_num+1,endpoint=True))# 设置横轴刻度
plt.xlim(0,test_num)# 设置x轴的上下限
plt.xlabel('实验序号',color='blue',size=28)# 设置x轴描述信息
plt.ylabel("目标函数",color='red')# 设置y轴描述信息,利用r'$x_1$设置下标1
#plt.yticks(np.linspace(0,1,11,endpoint=True))# 设置纵轴刻度
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.legend()
plt.grid(True)
LJ=opt_way[index]
num="列次实验中最优路径"
drawpath(LJ, city_zb, num)
plt.text(25, 25, "总长度=")
plt.text(28, 25, str(int(1000 * opt_JJ[index] )/ 1000))

print("列次计算目标函数平均值=",np.mean(opt_JJ))

plt.show()

