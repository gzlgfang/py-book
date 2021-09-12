#03-Genetic algorithm 
from typing import Type
from matplotlib import colors, markers
import numpy as np
import pandas as pd
import random as rnd
import time

#绘图设置
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



DF=pd.read_excel('city.xlsx','Sheet1', na_filter=False,index_col=0)#共有79组物性数据
city_x =np.array( DF['x'])#数据分配
city_y=np.array( DF['y'])
n=len(city_x)#计算城市的数目
city_zb=np.zeros((n,2))
city_zb[:,0]=city_x/100
city_zb[:,1]=city_y/100
# 计算城市i和城市j之间的距离
# 输入 city_zb 各城市的坐标,用city_zb[i,0:1])
# 输出 D 城市i和城市j之间的距离,用D[i,j]表示
def  Distance(city_zb):
     D=np.zeros((n,n))#  产生两城市之间距离数据的空矩阵即零阵
     for i in range(n):
            for  j in range(i+1,n):
               #D[i,j]=city_zb[i,0]
               D[i,j]=((city_zb[i,0]-city_zb[j,0])**2+(city_zb[i,1]-city_zb[j,1])**2)**0.5
               D[j,i]=D[i,j]
     return D 
D=Distance(city_zb)
#print(D)
#产生随机路径path
ZQS=100       #种群大小
MAXGEN=200     #最大遗传代数
Pc=0.9        #交叉概率
Pm=0.08        #变异概率
Sel_ra=0.9       #选择率
def path(ZQS,N):
    li=np.arange(0,N)
    LJ=np.zeros((ZQS,N))
    for i in range(ZQS):
         rnd.shuffle(li)
         LJ[i,:]=li
    return LJ.astype(int)
LJ=path(ZQS,n)
#print(LJ)
#绘制初始路径图
#画路径函数
#输入
# LJ 待画路径   
#city_zb 各城市坐标位置

def drawpath(LJ,city_zb):
    plt.figure()
    n=len(LJ)
    plt.scatter(city_zb[:,0],city_zb[:,1],marker='o',color="b",s=100)#所有城市位置上画上o
    plt.text(city_zb[LJ[0],0]+0.5,city_zb[LJ[0],1]+0.5,'起点')
    plt.text(city_zb[LJ[n-1],0]+0.5,city_zb[LJ[n-1],1]+0.5,'终点')
    
    #绘线
    xy=(city_zb[LJ[0],0],city_zb[LJ[0],1])
    xytext=(city_zb[LJ[1],0],city_zb[LJ[1],1])   
    plt.annotate('',xy=xy,xytext=xytext , arrowprops=dict(arrowstyle='<-',color="g",lw=1))
    for i in range(1,n-1):
        x=[city_zb[LJ[i],0],city_zb[LJ[i+1],0]]
        y=[city_zb[LJ[i],1],city_zb[LJ[i+1],1]]
        plt.plot(x,y,lw=2,c="r")
    xy=(city_zb[LJ[n-1],0],city_zb[LJ[n-1],1])
    xytext=(city_zb[LJ[0],0],city_zb[LJ[0],1])   
    plt.annotate('',xy=xy,xytext=xytext , arrowprops=dict(arrowstyle='<-',color="g",lw=1))



    plt.ylim(0,40)
    plt.xlim(10,45)
    plt.grid()
    plt.xlabel('横坐标')
    plt.ylabel('纵坐标')
    plt.title(' 轨迹图')


#计算路径总距离
def pathlength(D,LJ):
  N=D.shape[1]
  ZQS=LJ.shape[0]
  p_len=np.zeros(ZQS)
  for i in range(ZQS):
      for j in range(N-1):
         p_len[i]=p_len[i]+D[LJ[i,j],LJ[i,j+1]]
      p_len[i]=p_len[i]+D[LJ[i,N-1],LJ[i,0]]
  return p_len
p_len=pathlength(D,LJ)
#print(p_len)
#p_sort=np.sort(p_len)
#print(p_sort)
#计算适应度值fitness 归一化处理
def fit(p_len):
    ZQS=len(p_len)
    fitnv=np.ones(ZQS)
    fitnv[:]=1/p_len[:]
    max=np.max(fitnv)
    min=np.min(fitnv)
    fitnv[:]=(fitnv[:]-min)/(max-min)
    return fitnv
#print(fit(p_len))

#绘制初始路径1
draw_path=drawpath(LJ[0,:],city_zb)
#plt.legend(str(p_len[0]))
print(p_len[0])
plt.text(35,35,'总长度=')
plt.text(37,35,str(int(1000*p_len[0])/1000))


#绘制初始优化图
index=list(p_len[:]).index(min(p_len[:]))#找到最短距离路径序号
#print(index)

draw_path=drawpath(LJ[index,:],city_zb)
#plt.legend(str(p_len[0]))
print(p_len[index])
plt.text(35,35,'总长度=')
plt.text(37,35,str(int(1000*p_len[index])/1000))


#初始种群优化图
fitnv=fit(p_len)
#选择操作
def select(LJ,Sel_ra,fitnv):
   ZQS=len(LJ) 
   sel_num=int(ZQS*Sel_ra)
   n=0
   index=[]
   flags=True
   while flags:
       for i in range(ZQS):
           pick= rnd.random()
           if pick<0.8*fitnv[i]:
               index.append(i)
               n=n+1
               if n==sel_num:
                   break
       if n==sel_num:
          flags=False
   Sel_LJ=LJ[index]
   return Sel_LJ
Sel_LJ=select(LJ,Sel_ra,fitnv)

#print(Sel_LJ.shape)
#print(index)
#print(fitnv[index])
#print(Sel_LJ)

#交叉
def cross(a,b):
#a和b为两个待交叉的个体
#输出：
#a和b为交叉后得到的两个个体
   n=len(a)#城市数目
   flags=True
   while flags:
       r1=rnd.randint(0,n-1)# 随机产生一个0：n-1的整数
       r2=rnd.randint(0,n-1)# 随机产生一个0：n-1的整数
       if r1!=r2:
          flags=False 
#保证找到两个不同是整数，可以进行交叉操作
   a0=np.zeros(n)
   b0=np.zeros(n)
   a1=np.zeros(n)
   b1=np.zeros(n)
   a0[:]=a[:]
   b0[:]=b[:]
   a1[:]=a[:]#先保护原数据到a1,b1
   b1[:]=b[:]  
   
   #a0,b0=a,b#作为中间变量
   if r1>r2: 
      s,e=r2,r1
   else:
       s,e=r1,r2
   #a[s:e+1]=b0[s:e+1]
   #b[s:e+1]=a0[s:e+1]
#print(s,e)
   for i in range(s,e+1):
        a[i]=b0[i]
        b[i]=a0[i]
        #a1,b1=a,b#先保护原数据到a1,b1
        x=[id for id in range(n) if a[id]==a[i]]#找到交换后a中重复元素的序号
        y=[id for id in range(n) if b[id]==b[i]]
        #print("i=",x,y)
        id1=[s1 for k, s1 in enumerate(x)  if x[k]!=i] #找到序号不为i的其他序号
        id2=[s2 for k, s2 in enumerate(y)  if y[k]!=i]
        #print("i=",i)
        #print(id1)
        #print(id2)
        if id1!=[]:
           i1=id1[0]
           a[i1]=a1[i]
           a1[i1]=a[i1]
        if id2!=[]:
           i2=id2[0] 
           b[i2]=b1[i]
           b1[i2]=b[i2]

        #if ~isempty(i2)
            #b(i2)=b1(i)
   #print(np.sort(a))
   #print(np.sort(b))   
   return [a,b]  
   



#交叉重组
def Re_com(Sel_LJ,Pc):
    n=len(Sel_LJ)
    for i  in range(0,n-1,2):
       #print(i) 
       if Pc>=rnd.random():#%交叉概率Pc
        [Sel_LJ[i,:],Sel_LJ[i+1,:]]=cross(Sel_LJ[i,:],Sel_LJ[i+1,:])  
    return Sel_LJ
Sel_LJ=Re_com(Sel_LJ,Pc)
#print("NEW=",Sel_LJ)


p_len=pathlength(D,Sel_LJ)
fitnv=fit(p_len)
index=list(p_len[:]).index(min(p_len[:]))#找到最短距离路径序号
#print(index)
print(Sel_LJ[index])
draw_path=drawpath(Sel_LJ[index],city_zb)
plt.text(35,35,'总长度=')
plt.text(37,35,str(int(1000*p_len[index])/1000))
print(np.sort(Sel_LJ[index]))
print(Sel_LJ[index])
plt.show()