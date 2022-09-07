#07-Nu_Re_Pr-fit.py
from scipy import optimize as op
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt

def func(x,c1,c2,c3):
    return c1*x[0]**c2*x[1]**c3

x0=np.ones(99)
for i in range(9):
      for j in range(11):
          x0[i*11+j]=i*500+1000
x=np.array([x0,[1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 1. , 1.2,
       1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 1. , 1.2, 1.4, 1.6,
       1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 1. , 1.2, 1.4, 1.6, 1.8, 2. ,
       2.2, 2.4, 2.6, 2.8, 3. , 1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4,
       2.6, 2.8, 3. , 1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8,
       3. , 1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 1. ,
       1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 1. , 1.2, 1.4,
       1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. ]])
cc=[0.023,0.8,0.3]
y_real=func(x,*cc)+np.random.random(99)*0.1
#print(y_real)
fit_cc,fit_cv=op.curve_fit(func,x,y_real)#拟合曲线curvefit方法p0=(0.2,0.2,0.2)
print(f'c_1={fit_cc[0]:.5f},c_2={fit_cc[1]:.5f}, c_3={fit_cc[2]:.5f}')
y_data=z=func(x,*fit_cc)
#计算绝对百分误差平均值
abseer=np.mean(abs(y_real-y_data)/y_data)*100
print("abseer=",f'{abseer:.5f}',"%")

#图形绘制
from mpl_toolkits.mplot3d import Axes3D
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['font.size']=16
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
fig = plt.figure()
# 指定图形类型是 3d 类型
ax = fig.add_subplot(projection='3d')
# 构造数据
xx=x[0]
yy=x[1]
# Plot the line and scatter
ax.scatter(xx, yy, y_real,s=58,color="red",label="实验数据" )
ax.plot(xx, yy, z,color="b",lw=2,label="拟合数据" )
ax.text(2100,2,25,f'abseer={abseer:.5f}%',zdir='x')
ax.text(2100,2,30,f'c$_1$={fit_cc[0]:.5f}, c$_2$={fit_cc[1]:.5f}, c$_3$={fit_cc[2]:.5f}',zdir='x')
ax.set_xlabel("$Re$", fontsize=16)
ax.set_ylabel("$Pr$", fontsize=16,labelpad=8) 
ax.set_zlabel("$Nu$", fontsize=16)
plt.legend()
plt.show()
