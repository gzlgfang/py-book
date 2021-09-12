#02-wuxing Physical properties 
from typing import Type
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
mpl.rcParams["font.size"] =28#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细



DF=pd.read_excel('xuexi.xlsx','Sheet1', na_filter=False,index_col=0)#共有79组物性数据
a1 =np.array( DF['TB'])#数据分配
a2 =np.array( DF['TC'])
a3 =np.array( DF['PC'])
yy =np.array( DF['HV'])
a1_max=a1.max()*1.25
a2_max=a2.max()*1.25
a3_max=a3.max()*1.25
yy_max=yy.max()*1.25

a1=a1/a1_max#数据简单归一化，保证不大于1
a2=a2/a2_max
a3=a3/a3_max
yy=yy/yy_max
print(a1,"\n",type(a1),"\n",len(a2))#抽查数据

n =3 # eval(input("输入输入层神经元数目="))#相当于输入变量有n个分量
p =3# eval(input("输入中间层神经元数目="))
q =1# eval(input("输入输出层神经元数目="))#相当于输出变量有q个分量

m =15# eval(input("训练模式数量="))
a=np.zeros((31,n))
y=np.zeros((31,q))
a[:,0]=a1#设置全部网络数据
a[:,1]=a2
a[:,2]=a3
y[:,0]=yy
print(a,"\n",y)
#'生成初始连接权数及阀值
w=2*np.random.random((n,p))-1
thta=2*np.random.random(p)-1
print(w,"\n",thta) 
v=2*np.random.random((p,q))-1
r=2*np.random.random(q)-1
print(v,"\n",r)
#'神经元函数
def fnf(x):
  fnf = 1 / (1 + np.exp(-x))
  return fnf

start_time = time.perf_counter()
print("start_time:", start_time)
ee = 1
train_num=0
tol=[]
b=np.zeros(p)
c=np.zeros((30,q))
d=np.zeros(q)
while ee>0.0045:
   eer=np.zeros(m)
   #c=np.zeros((m,q))
   e =np.zeros((m,p))
   for k in range(m):
      #eer(k) = 0
       #'模式顺传播
       s=np.zeros(p)
       #b=np.zeros(p)
       for j in range(p):
            #s(j) = 0
            for i in range(n):
               s[j] = s[j] + w[i, j] * a[k, i]
            s[j] = s[j] - thta[j]
            b[j] = fnf(s[j]) 
       L=np.zeros(q)
       #d=np.zeros(q)
       for t in range(q):
            #L(t) = 0
            for j in range(p):
               L[t] =L[t] + v[j, t] * b[j]
            L[t] = L[t] - r[t]
            #'Print l(t)
            c[k, t] = fnf(L[t])
            #'误差逆传播
            d[t] = (y[k, t] - c[k, t]) * c[k, t] * (1 - c[k, t])
     
              
       for j in range(p):
            #e(k, j) = 0
            for t in range(q):
                e[k, j] = e[k, j] + d[t] * v[j, t]
            e[k, j] = e[k, j] * b[j] * (1 - b[j])
        
        #'调整连接权及罚值，网络的学习系数均取0.5
       for t in range(q):
            for j in range(p):
                 v[j, t] = v[j, t] +0.5* d[t] * b[j]
            r[t] = r[t] - 0.5 * d[t]#0.5学习效率，下同
       for j in range(p):
            for i in range(n):
                 w[i, j] = w[i, j] + 0.5 * e[k, j] * a[k, i]
            thta[j] = thta[j] - 0.5 * e[k, j]
   train_num =train_num + 1

    #'计算全局误差
   ee = 0
   for k in range(m):
        #eer(k) = 0
        for t in range(q):
            eer[k] = eer[k] + (y[k, t] - c[k, t])** 2
        ee = ee + eer[k]
   ee=np.sqrt(ee)
   #'全局误差判断
   
   
   if train_num/100000==int(train_num/100000):
       print("ee=",ee)
       tol.append(ee)
   if train_num<2000000:
         continue#'网络尚未收敛，继续计算
   else:
        exit
   #'网络收敛，打印权值及阀值并进入回响
   #GoTo 200
#绘制误差图
#print(tol)

#   
#'打印权值及阀值
for j in range(p):
        for i in range(n):
             print( "w(", i, j, ")=", w[i, j])
        print( "thta(", j, ")=", thta[j])
for t in range(q): 
        for j in range(p):
             print ("v(", j, t,")=", v[j, t])
        print ("r(", t, ")=", r[t])

print ("全局误差=", ee,"\n" "总训练次数=", train_num)

end_time = time.perf_counter()
print("perf_counter程序运行计时=", end_time - start_time,"秒")

 
# 训练集网络回响

train_eer = 0

   #c=np.zeros((m,q))
#e =np.zeros((m,p))
for k in range(m):
     s=np.zeros(p)
     for j in range(p):
          for i in range(n):
               s[j] = s[j] + w[i, j] * a[k, i]
          s[j] = s[j] - thta[j]
          b[j] = fnf(s[j])
     L=np.zeros(q)
     #d=np.zeros(q)
     for t in range(q):
          for j in range(p):
               L[t] =L[t] + v[j, t] * b[j]
          L[t] = L[t] - r[t]
            #'Print l(t)
          c[k, t] = fnf(L[t])
     #c[k,0]=c[k,0]*yy_max ,由于数据均以归一化处理，计算百分误差时无需翻转
     train_eer=train_eer+abs((c[k,0]-y[k,0])/y[k,0])
train_eer= train_eer/m
print( f"训练集相对百分误差={100*train_eer:.2f}% ")     


#测试集网络回响

test_eer = 0
eer=np.zeros(m)
   #c=np.zeros((m,q))
e =np.zeros((m,p))
for k in range(m,30):
     s=np.zeros(p)
     for j in range(p):
          for i in range(n):
               s[j] = s[j] + w[i, j] * a[k, i]
          s[j] = s[j] - thta[j]
          b[j] = fnf(s[j])
     L=np.zeros(q)
     #d=np.zeros(q)
     for t in range(q):
          for j in range(p):
               L[t] =L[t] + v[j, t] * b[j]
          L[t] = L[t] - r[t]
            #'Print l(t)
          c[k, t] = fnf(L[t])
     #c[k,0]=c[k,0]*yy_max ,由于数据均以归一化处理，计算百分误差时无需翻转
     test_eer=test_eer+abs((c[k,0]-y[k,0])/y[k,0])
test_eer=test_eer/(30-m)
print( f"测试集相对百分误差={100*test_eer:.2f}% ") 


train_num1=[]
print(len(tol))
for i in range(len(tol)):
    train_num1.append((i+1)*10000) 
plt.figure()
plt.plot(train_num1,tol,lw=2,marker="o",color='#1f77b4')#
plt.grid()
plt.xlabel("训练数目")
plt.ylabel("全局误差")
plt.title("训练数目和全局误差关系图")
plt.show()

# 单个网络回响
# '网络回响
flags=True
while flags:
    x=np.zeros(n) 
    for i in range(n):
        print("输入第",i+1,"输入变量")
        x[i] = eval(input("x[i]="))
        print(x[i])
    x[0]=x[0]/a1_max
    x[1]=x[1]/a2_max
    x[2]=x[2]/a3_max
    s=np.zeros(p) 
    for j in range(p):
        for i in range(n): 
            s[j] = s[j] + w[i, j] * x[i]
        s[j] = s[j] - thta[j]
        b[j] = fnf(s[j])
    L=np.zeros(q)
    for t in range(q): 
        for j in range(p):
            L[t] =L[t] + v[j, t] * b[j]
        L[t] = L[t] - r[t]
        print(L[t])
        yy = fnf(L[t])*yy_max
        print(yy)
    tt=input( "是否继续需要网络回响，是输入y，否输入n ")
    if tt== "y":
        flags=True
    else:
        flags=False





