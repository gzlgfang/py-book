#02-Second_fit.py
#二次拟合

import numpy as np
from numpy import linalg
import matplotlib  as mpl
import matplotlib.pyplot as plt


#设置刻度线朝内
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 16#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True

#给定实验数据
x=np.array([-4,-3,-2,-1,0,1,2,3,4])#自变量
y=np.array([6.2,2.6,0.48,0.56,2.4,6.7,12.3,20.7,30.2])#应变量
#计算法方程系数：
m=len(x)
a12=a21=sum(x)
a13=a22=a31=sum(x**2)
a23=a32=sum(x**3)
a33=sum(x**4)
A=np.mat([[m,a12,a13],[a21,a22,a23],[a31,a32,a33]])

b11=sum(y)
b21=sum(x*y)
b31=sum(x**2*y)
b=np.mat([[b11],[b21],[b31]])
 # 线性方程求解 Acoef=b 
coef=linalg.solve(A,b)
cc=np.array(coef).reshape(3,)
print("二次拟合求解")
for i in range(len(coef)):
    print(f"a{i}={cc[i]:.5f}")
def func(x, a0,  a1,a2):
        return  a0+a1*x+a2*x*x
plt.figure(num="拟合曲线绘制",figsize=(8,8))
plt.scatter(x,y,color="red",label='实验数据')#绘制数据点
plt.xlabel("x",fontname="serif")
plt.ylabel("y",labelpad=5,fontname="serif")
ydata=func(x,*cc)
eer=sum((y-func(x,*cc))**2)
print('eer=',eer)
plt.plot(x,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.text(-3.8,25,f'均方误差={eer:.5f}' )
plt.text(-3.8,23,f'拟合方程：y={cc[0]:.5f}+{cc[1]:.5f}x+{cc[2]:.5f}x$^2$' )
plt.xlim(-4,4)#设置x轴范围
plt.ylim(-5,35)
plt.legend()
plt.show()




