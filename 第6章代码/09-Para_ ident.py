#09-Parameter identification 
#09-para_indent.py

from re import U
from scipy import optimize as op
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt
import scipy as scp
from scipy.integrate import odeint
#输入数据
#k1=0.1
#k2=0.1
#k3=0.1# 参数初值
C1=np.array([10,8.6231,	7.4627,	6.4811,	5.6475,	4.9366,	4.3282,	3.8057,	3.3552,	2.9652,	2.6261])
C2=np.array([0,	1.2759,	2.1736,	2.7808,	3.1666,	3.385,	3.478,	3.4783,	3.4118,	3.2984,	3.1537])
C3=np.array([0,	0.202,	0.7273,	1.4761,	2.3719,	3.3569,	4.3876,	5.432,	6.4661,	7.4728,	8.4403])
C=np.array([C1,C2,C3]).T
#定义微分方程组
def dy(y,t,k1,k2,k3):
    y1,y2,y3,=y[0],y[1],y[2]
    dy1=-k1*y1+k2*y2
    dy2= k1*y1-k2*y2-k3*y2
    dy3= 2*k3*y2
    return [dy1,dy2,dy3]
y0 = [10, 0,0]# 确定初始状态
tspan=np.linspace(0,5.0,11)#确定自变量范围
#sol =odeint(dy, y0, tspan,args=(k1,k2,k3))
#print("sol=",sol[:,0])
def J(k1,k2,k3):
   J1=odeint(dy, y0, tspan,args=(k1,k2,k3))[:,0]-C1
   J2=odeint(dy, y0, tspan,args=(k1,k2,k3))[:,1]-C2
   J3=odeint(dy, y0, tspan,args=(k1,k2,k3))[:,2]-C3
   JJ= sum(J1**2+J2**2+J3**2)
   return JJ
#k1=0.3,k2=0.05,k3=0.3
k0=np.array([0.1,0.1,0.1])#初始辨识参数
#单纯形法优化参数
h=0.1#高度
alfa=1
lamda=0.75
miue=1
flag=True
n=0
eer=0.000001
kk1=np.copy(k0)
kk1[0]=k0[0]+h

kk2=np.copy(k0)
kk2[1]=k0[1]+h

kk3=np.copy(k0)
kk3[2]=k0[2]+h

#得到初始单纯形4个点
#print(k0,kk1,kk2,kk3)
#print(J(*k0),J(*kk1),J(*kk2),J(*kk3))
flag=True
while flag:
    j0=J(*k0)
    j1=J(*kk1)
    j2=J(*kk2)
    j3=J(*kk3)
#目标函数排序
    n=n+1
    if n>=100:
       flag=False
    ob=[j0,j1,j2,j3]
    obj=[j0,j1,j2,j3]
    obj.sort()
    #print(obj)
    if abs((j0-j3)/(j3+0.5))<eer:
       flag=False
    if obj[0]==j0:
       fL=j0
       UL=k0
    elif obj[0]==j1:
       fL=j1
       UL=kk1 
    elif obj[0]==j2:
       fL=j2
       UL=kk2
    elif obj[0]==j3:
       fL=j3
       UL=kk3

    if obj[1]==j0:
       fT=j0
       UT=k0
    elif obj[1]==j1:
       fT=j1
       UT=kk1 
    elif obj[1]==j2:
       fT=j2
       UT=kk2
    elif obj[1]==j3:
       fT=j3
       UT=kk3

    if obj[2]==j0:
       fM=j0
       UM=k0
    elif obj[2]==j1:
       fM=j1
       UM=kk1 
    elif obj[2]==j2:
       fM=j2
       UM=kk2
    elif obj[2]==j3:
        fM=j3
        UM=kk3

    if obj[3]==j0:
       fH=j0
       UH=k0
    elif obj[3]==j1:
       fH=j1
       UH=kk1 
    elif obj[3]==j2:
       fH=j2
       UH=kk2
    elif obj[3]==j3:
       fH=j3
       UH=kk3

#找到最小、次大、最大三点
    #print(fL,UL,fM,UM,fH,UH)
#计算重心
    UC=(k0[:]+kk1[:]+kk2[:]+kk3[:]-UH[:])/3
    #print(UC)
#进行映射
    UR=UC+alfa*(UC-UH)
    fR=J(*UR)
    #print(fR)
    if fR<fM:
        UE=UR+miue*(UR-UH)
        fE=J(*UE)
        if fE<fR:
          UH=UE
          k0=UL
          kk1=UT
          kk2=UM
          kk3=UH
          continue
        else:
           UH=UR
           k0=UL
           kk1=UT
           kk2=UM
           kk3=UH
           continue
    else:
      US=UH+lamda*(UR-UH)
      fS=J(*US)
      if fS<fM:
         UH=US
         k0=UL
         kk1=UT
         kk2=UM
         kk3=UH
         continue
      else:
         k0=UL
         kk1=(UT+UL)/2
         kk2=(UM+UL)/2
         kk3=(UH+UL)/2
         continue
print("k0,j0,n=",k0,j0,n)
