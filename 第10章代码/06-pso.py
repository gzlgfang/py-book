#!/usr/bin/env python3

"""
说明：PSO的函数写法
来源：MATLAB 智能算法
作者：scarlet
备注：naive PSO
"""
import numpy as np


import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] =18#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细

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
    v = np.random.rand(N, D) #初始速度
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
            if fitness(x[i]) < p[i]: # 更新个体极值
                p[i] = fitness(x[i]) 
                pbest[i] = x[i]      #pbest[i]为个体最优解
            if p[i] < fitness(gbest): # 更新全局极值
                gbest = pbest[i]
        pbest_fit[t] = fitness(gbest)
    print(f'目标函数取最小值时的自变量 {gbest}')
    print(f'目标函数的最小值为 {fitness(gbest)}')


    plt.figure(num="目标函数与迭代次数关系图")
    for i in range(M-1):
        plt.plot([i,i+1],[pbest_fit[i],pbest_fit[i+1]],lw=2,c="b")
        plt.grid()


def func(x):
    #x1=x[0]
    #x2=x[1]
    #x,y,z=x[0],x[1],x[2]
    x,y=x[0],x[1]
    f=lambda x: x**2-2*x+y+1000*(min(4-4*x**2-y**2,0))**2
    #f=lambda x:(x**0.8+x*y**0.7+z**0.8-1)**2+(x**1.2*y+y**0.9+x**0.5*z-1)**2+(x+y**0.4*z**0.5+z**1.2-1)**2
    #f=lambda x:(x[0]-10)**2+(x[1]-16)**2
    #f = lambda x: x1**2 +2*x1 - 6+x2**2 +2*x2
    #f=lambda x:30+x1**2 + x2**2-10*(np.cos(2*np.pi*x1)+np.cos(2*np.pi*x2))
    #f=lambda x:np.sin(np.sqrt(x1**2 + x2**2))/np.sqrt(x1**2 + x2**2)+np.exp((np.cos(2*np.pi*x1)+np.cos(2*np.pi*x2))/2)-np.exp(1)
    return np.sum(f(x))#求最大变成求最小，前面加负号

#if __name__ == '__main__':
PSO(func, 50, 1.5, 2.5, 0.5, 100, 2)
plt.xlabel("迭代次数")
plt.ylabel("目标函数值")

plt.show()