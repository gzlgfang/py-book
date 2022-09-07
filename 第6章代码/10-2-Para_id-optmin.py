#10-2=Parameter identification  
#10-2-para_indent.py 
#用optimize.minimize求解
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
k0=np.array([0.1,0.1,0.1])#参数初值
def fun(x):
    k1,k2,k3=x[0],x[1],x[2]
    #sum=J(k1,k2,k3)
    sum1=sum(sum((odeint(dy, y0, tspan,args=(k1,k2,k3))-C)**2))#先求解微分方程组，再将求解结果和实际数据相减，
                                                              #将所有差的平方和进行和列的相加，得到一个数值
    return sum1
res=op.minimize(fun,k0,method='L-BFGS-B',bounds=[(0.01,10),(0.01,10),(0.01,10)])
k=res.x#获取参数
j=res.fun#获取目标函数值即sum1
print("j=",j)#
print(f'辨识参数:k_1={k[0]:.5f}, k_2={k[1]:.5f}, k_3={k[2]:.5f}')
#图形绘制，#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['font.size']=16
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否

t=np.linspace(0,5,41)
y_data=odeint(dy, y0, t,args=(k[0],k[1],k[2]))#根据辨识参数，重新求解微分方程
fig = plt.figure()
plt.scatter(tspan, C1,s=58,color="red",label="实验数据C$_A$" ,clip_on=False)
plt.scatter(tspan, C2,s=58,color="b",label="实验数据C$_B$",clip_on=False )
plt.scatter(tspan, C3,s=58,color="purple",label="实验数据C$_B$",clip_on=False )

plt.plot(t, y_data[:,0],color="red",lw=2,label="拟合数据C$_A$" )
plt.plot(t, y_data[:,1],color="b",lw=2,label="拟合数据C$_B$" )
plt.plot(t, y_data[:,2],color="purple",lw=2,label="拟合数据C$_C$" )


plt.text(2,10,f'abseer={j*100:.5f}%')
plt.text(2,8,f'k$_1$={k[0]:.5f}, k$_2$={k[1]:.5f}, k$_3$={k[2]:.5f}')
plt.xlabel("$t$，时间 (min)", fontsize=16)
plt.ylabel("$C$,浓度 (kmol/m$^3$)", fontsize=16,labelpad=8) 
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)

plt.xlim(0,5)#设置x轴范围
plt.ylim(0,12)
plt.legend()
plt.show()