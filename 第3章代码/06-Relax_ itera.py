#06-Relaxation iteration 

import numpy as np
#a=10*np.random.rand(10,11)#产生系数
a=np.array([[5.0,1,1,12],[15,9.0,3,42],[2,2,7.0,13]])
for i in range(3):#形成迭代矩阵
    a[i,:]=-a[i,:]/a[i,i]
    a[i,i]=0
#print(a)
x0=np.ones(3)*0.5
x=np.zeros(3)
omiga=0.1#初始化
flag=True
eps=0.0000001
k=1
while flag==True:
    k=k+1
    for i in range(3):#方程行号
        temp=-a[i,3]
        for j in range(3):#列号
            temp=temp+a[i,j]*x0[j]
        x[i]=(1-omiga)*x0[i]+omiga*temp
    if max(abs(x-x0))<=eps:
       flag=False
    x0[:]=x[:]#注意不能用x0=x互换
    #print("x0=",x0)
    if k==2000:
        flag=False
print("k=",k,"x=",x)