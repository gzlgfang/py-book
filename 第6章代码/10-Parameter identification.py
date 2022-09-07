#10-Parameter identification 
#10-para_indent.py 
#用函数调用重编-09
from scipy import optimize as op
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt
import scipy as scp
from scipy.integrate import odeint
#输入数据
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
   JJ=sum(sum((odeint(dy, y0, tspan,args=(k1,k2,k3))-C)**2))
   return JJ
k0=np.array([0.1,0.1,0.1])#初始辨识参数
#单纯形法优化
def paixu(x,y): #数据线排序
  for i in range(len(y)-1):
      for j in range(i+1,len(y)):
          if y[i]>y[j]:
              tempy=y[i]
              y[i]=y[j]
              y[j]=tempy
              tempx=x[i]
              x[i]=x[j]
              x[j]=tempx
  xx=x
  yy=y
  return xx,yy
#单纯形结构参数
h=0.1#高度
alfa=1
lamda=0.75
miue=1
flag=True
n=0
eer=0.0000001#设定误差
kk1=np.copy(k0)
kk1[0]=k0[0]+h

kk2=np.copy(k0)
kk2[1]=k0[1]+h

kk3=np.copy(k0)
kk3[2]=k0[2]+h
#得到初始单纯形4个点
kkx=[k0,kk1,kk2,kk3]
print(kkx)
print(J(*k0),J(*kk1),J(*kk2),J(*kk3))
flag=True
while flag:
    j0=J(*kkx[0])
    j1=J(*kkx[1])
    j2=J(*kkx[2])
    j3=J(*kkx[3])
    
#目标函数排序
    n=n+1
    if n>=300:
       flag=False
    if abs((j0-j3)/(j3+0.5))<eer:
       flag=False
    oby=[j0,j1,j2,j3]
    kk,jj=paixu(kkx,oby)
    fL=jj[0]
    UL=kk[0]
    fT=jj[1]
    UT=kk[1]  
    fM=jj[2]
    UM=kk[2]
    fH=jj[3]
    UH=kk[3]
    
    kkx[0]=kk[0]
    kkx[1]=kk[1]
    kkx[2]=kk[2]
#找到最小、次大、最大三点
    #print(fL,UL,fM,UM,fH,UH)
#计算重心
    UC=(kk[0]+kk[1]+kk[2])/3
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
          kkx[3]=UH
          continue
        else:
           UH=UR
           kkx[3]=UH
           continue
    else:
      US=UH+lamda*(UR-UH)
      fS=J(*US)
      if fS<fM:
         UH=US
         kkx[3]=UH
         continue
      else:
         kkx[0]=UL
         kkx[1]=(UT+UL)/2
         kkx[2]=(UM+UL)/2
         kkx[3]=(UH+UL)/2
         continue
print(kk[0])
print("优化目标=",jj[0])
print("优化次数=",n)
print(f'辨识参数:k_1={kk[0][0]:.5f}, k_2={kk[0][1]:.5f}, k_3={kk[0][2]:.5f}')
#图形绘制,#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['font.size']=16
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
t=np.linspace(0,5,41)
y_data=odeint(dy, y0, t,args=(kk[0][0],kk[0][1],kk[0][2]))
fig = plt.figure()
plt.scatter(tspan, C1,s=58,color="red",label="实验数据C$_A$",clip_on=False)
plt.scatter(tspan, C2,s=58,color="b",label="实验数据C$_B$",clip_on=False )
plt.scatter(tspan, C3,s=58,color="purple",label="实验数据C$_B$",clip_on=False )
plt.plot(t, y_data[:,0],color="red",lw=2,label="拟合数据C$_A$" )
plt.plot(t, y_data[:,1],color="b",lw=2,label="拟合数据C$_B$" )
plt.plot(t, y_data[:,2],color="purple",lw=2,label="拟合数据C$_C$" )
plt.text(2,10,f'abseer={jj[0]*100:.5f}%')
plt.text(2,8,f'k$_1$={kk[0][0]:.5f}, k$_2$={kk[0][1]:.5f}, k$_3$={kk[0][2]:.5f}')
plt.xlabel("$t$，时间 (min)", fontsize=16)
plt.ylabel("$C$,浓度 (kmol/m$^3$)", fontsize=16,labelpad=8) 
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.xlim(0,5)#设置x轴范围
plt.ylim(0,12)
plt.legend()
plt.show()