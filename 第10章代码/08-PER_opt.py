#!/usr/bin/env python3

"""
说明:PSO的函数写法
思路:智能算法与过程优化合成
作者:scarlet
备注:naive PSO
"""
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_bvp
import scipy.interpolate as spi 
from scipy import optimize as op
#设置刻度线朝内
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["FangSong"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 16#设置字体大小
#mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
font1 = {'family': 'Times New Roman'} 

def PSO(fitness, N, c1, c2, w, M, D):
    """
    c1 学习因子1
    c2 学习因子2
    w 惯性权重
    M 最大迭代次数
    D 搜索空间维数
    N 初始化群体个体数目
    """
    # 初始化种群的个体 
    x = np.random.rand(N, D) #初始位置
    x.sort#本题求温度分布，需要从高温到低温
    v = np.random.rand(N, D) #初始速度
    #x[0]=[1 ,1 ,0.71, 0.5935, 0.52, 0.475, 0.439, 0.411, 0.382, 0.369, 0.352]
    # pi 代表个体极值
    pbest = np.copy(x) #个体初始最优位置
    p = np.zeros(N)# 个体初始最优值
    for i, val in enumerate(x):
        p[i] = fitness(val) # 计算适应度，即目标函数，计算N个粒子的函数值

    # gbest 全局最优位置
    gbest = x[N-1]
    for i in range(N-1):#寻找n个粒子函数值最小的粒子位置gbest
        if fitness(x[i]) < fitness(gbest):
            gbest = x[i]
    # 主要循环
    pbest_fit = np.zeros(M)#每一次迭代的最优函数值
    for t in range(M):#进行M轮迭代
        for i in range(N):
            # momentum + cognition + social
            v[i] = w * v[i] + c1 * np.random.random() * (pbest[i] - x[i])  + c2 * np.random.random() * (gbest - x[i])
            x[i] = x[i] + v[i]
            for j in range(D):
               if  x[i,j]<0:#保证变量为非负，需要根据具体求解问题设置
                   x[i,j]=0
               if  x[i,j]>1:#保证变量为非负，需要根据具体求解问题设置
                   x[i,j]=1
            if fitness(x[i]) < p[i]: # 更新个体极值
                p[i] = fitness(x[i]) 
                pbest[i] = x[i]      #pbest[i]为个体最优解
            if p[i] < fitness(gbest): # 更新全局极值
                gbest = pbest[i]
        pbest_fit[t] = fitness(gbest)
        x.sort
    #结束迭代，得到最优解gbest,
    print(f'目标函数取最小值时的自变量 {gbest}')
    print(f'目标函数的最小值为 {fitness(gbest)}')
    plt.figure(num="目标函数与迭代次数关系图")
    for i in range(M-1):
        plt.plot([i,i+1],[pbest_fit[i],pbest_fit[i+1]],lw=2,c="b")
        plt.grid()
    #绘制浓度曲线:
    plt.xlabel("迭代次数")
    plt.ylabel("目标函数值")


    #根据求得的最优参数，求解微分方程，得到浓度分布
    tspan=np.linspace(0,1,11)#确定自变量范围
    C_tspan = np.zeros((2, tspan.size))#确定2个应变量初值    
    def dx(t,xx):# t表示长度方向，xx表示对应物质摩尔分率   
      ipo=spi.splrep(tspan,gbest,k=3)
      ky=spi.splev(t,ipo)
      x1,x2=xx[0],xx[1]
      #x1,x2,x3,x4=xx[0],xx[1],xx[2],xx[3]
    # 浓度方程
      dx1=ky**2*x2-ky*x1#%微分方程1
      dx2=ky*x1-3*ky**2*x2#%微分方程2
    # 伴随方程
      #dx3=ky*(x3-x4)#微分方程3
      #dx4=ky**2*(3*x4-x3*x1)#%微分方程4
      return np.vstack((dx1, dx2))
      #return np.vstack((dx1, dx2,dx3,dx4))
#定义边界条件
    def BC(xa, xb):
        return np.array([xa[0]-1,xa[1]-0])#
        #return np.array([xa[0]-1,xa[1]-0,xb[2]-0,xb[3]-1])#
    sol= solve_bvp(dx, BC,tspan, C_tspan)
    C=sol.sol(tspan) 
    plt.figure(figsize=(8,6), dpi=80)# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    plt.plot(tspan, C[0,:], label=r"$C_A$",color="red", linewidth=2, linestyle="-")
    plt.plot(tspan, C[1,:], label=r'$C_B$',color="green", linewidth=2.0, linestyle="--")
    #plt.plot(tspan, C[2,:], label=r"$λ_1$",color="b", linewidth=2, linestyle="-")
    #plt.plot(tspan, C[3,:], label=r"$λ_2$",color="k", linewidth=2, linestyle="-")
    plt.plot(tspan, 1-C[0,:]-C[1,:], label=r"$C_B$",color="b", linewidth=2, linestyle="-.")
    plt.xticks(np.linspace(0,1,11,endpoint=True))# 设置横轴刻度
    plt.xlim(0,1)# 设置x轴的上下限
#plt.ylim(-120,180)
    plt.xlabel(r'$\mathrm{x}$',color='blue',size=28)# 设置x轴描述信息
    plt.ylabel(r'$\mathrm{C_{A},C_{B},C_{C}}$',color='red')# 
    #plt.ylabel(r'$\mathrm{C_{A},C_{B},C_{C},λ_{1},λ_{2}}$',color='red')# 设置y轴描述信息,利用r'$x_1$设置下标1
    plt.yticks(np.linspace(0,1,11,endpoint=True))# 设置纵轴刻度
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.ylim(0,1)
    plt.legend()
    plt.grid(True)

    #绘制温度随管长关系图
    plt.figure(num="温度随管长关系图")
    
    T=np.zeros(tspan.size)
    T[0],T[1]=3000,2000
    for i in range(2,11):
        T[i]=-1000/1.9858115/np.log(gbest[i])
    ipo_T=spi.splrep(tspan,T,k=3)
    x=np.linspace(0,1,101)
    T_y=spi.splev(x,ipo_T)
    plt.plot(x,T_y,color="b", linewidth=3)
    plt.grid()
    plt.xticks(np.linspace(0,1,11,endpoint=True))# 设置横轴刻度
    plt.xlim(0,1)
    plt.xlabel("管长，L")
    plt.ylabel("加热温度，T(K)")
    plt.show()

#定义自适应度函数
def fitness(kx):
    tspan=np.linspace(0,1,11)#确定自变量范围
    C_tspan = np.zeros((2, tspan.size))#确定4个应变量初值
#定义微分方程,注意和程序08-bc_ode中的不同，自变量t放在前面
    def dx(t,xx):#    
      ipo=spi.splrep(tspan,kx,k=3)
      ky=spi.splev(t,ipo)
      x1,x2=xx[0],xx[1]
    # 浓度方程
      dx1=ky**2*x2-ky*x1#%微分方程1
      dx2=ky*x1-3*ky**2*x2#%微分方程2
    # 伴随方程
      #dx3=ky*(x3-x4)#微分方程3
      #dx4=ky**2*(3*x4-x3*x1)#%微分方程4
      return np.vstack((dx1, dx2))
#定义边界条件
    def BC(xa, xb):
        return np.array([xa[0]-1,xa[1]-0])#]
    sol= solve_bvp(dx, BC,tspan, C_tspan)
    C_B=sol.sol(tspan)[1]#共有2个应变量，序号从0-1,1表示第2个即C_B
    return -C_B[-1]#-1表示最后一个元素

PSO(fitness, 50, 1.5, 2.5, 0.5, 50, 11)#调用总程序

