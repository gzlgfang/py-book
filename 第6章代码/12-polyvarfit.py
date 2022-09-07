#12-polyvarfit
from scipy import optimize as op
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt
#自定义拟合函数
def func(x, a0,  a1, a2):
        return a0+a1*x[0]+a2*x[1]
x=np.array([[1,2,3,4,5,7,8,9],[5,7,8,9,3,4,2,1]])
y_data=func(x, 2, 1,1)
y_real=y_data+0.99*np.random.random(8)
print(y_real)#

#最小二乘拟合
def J(alfai):
    return y_real-func(x,*alfai)
alf0=[1,1,1]
alf_opt,alf_cov=op.leastsq(J,alf0)
print('alf_opt=',alf_opt)
print("alf_cov=",alf_cov)

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
z=func(x, *alf_opt)#拟合数据
print(y_real,z)


MSE=sum((z-y_real)**2)
print("MSE=",MSE)


x_text=0.4*(max(xx)-min(xx))+min(xx)
y_text=0.4*(max(yy)-min(yy))+min(yy)
z1_text=0.8*(max(z)-min(z))+min(z)
z2_text=0.9*(max(z)-min(z))+min(z)
# Plot the line and scatter
ax.scatter(xx, yy,y_real,s=58,color="red",label="实验数据" )
ax.plot(xx, yy, z,color="b",lw=2,label="拟合数据" )
ax.text(x_text,y_text,z1_text,f'偏差平方和MSE={MSE:.5f}%',zdir='x')
ax.text(x_text,y_text,z2_text,f'a$_0$={alf_opt[0]:.5f}, a$_1$={alf_opt[1]:.5f}, a$_2$={alf_opt[2]:.5f}',zdir='x')
ax.set_xlabel("$x1$", fontsize=16)
ax.set_ylabel("$x2$", fontsize=16,labelpad=8) 
ax.set_zlabel("$y$", fontsize=16)
plt.legend()
plt.show()








