#32.py
#二维函数值色图绘制
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as mticker
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['font.size']=16
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
#from mpl_toolkits.mplot3d.axes3d import Axes3D
#数据处理
x = np.arange(-3, 3.01, 0.01)
y = np.arange(-3, 3.01, 0.01)
X, Y = np.meshgrid(x, y)
R = np.sqrt((X**2 + Y**2)/2)
Z =-20*np.exp(-0.2*R)+20+np.exp(0.5)-np.exp(0.5*(np.cos(2*np.pi*X)+np.cos(2*np.pi*Y)))
norm = mpl.colors.Normalize(-abs(Z).max(), abs(Z).max())
#布局设置
fig, ax = plt.subplots(1, 4, figsize=(16, 4) )
#pcolor绘制
p = ax[0].pcolor(X, Y, Z, cmap=mpl.cm.RdBu,norm=norm,shading='auto')
plt.colorbar(p, ax=ax[0])
ax[0].set_title("pcolor绘制")
#contour绘制
p=ax[1].contour(X, Y, Z, 15, cmap=mpl.cm.RdBu,norm=norm)
plt.colorbar(p, ax=ax[1])
ax[1].set_title("contour绘制")           
#imshow绘制
#ax.axis('tight')
p = ax[2].imshow(Z, norm=norm, cmap='Purples',
               extent=[x.min(), x.max(), y.min(), y.max()])
plt.colorbar(p, ax=ax[2],orientation = 'horizontal')
ax[2].set_title("imshow绘制")

#im.set_interpolation('bilinear')
#contourf绘制
p=ax[3].contourf(X, Y, Z, 15, cmap=mpl.cm.RdBu,norm=norm)#cmpa共有170种
plt.colorbar(p, ax=ax[3])
ax[3].set_title("contourf绘制") 

font1 = {'family': 'Times New Roman'}  
ax[0].set_xlabel('x',font1)
ax[0].set_ylabel('y',font1)
ax[1].set_xlabel('x',font1)
ax[1].set_ylabel('y',font1)
ax[2].set_xlabel('x',font1)
ax[2].set_ylabel('y',font1)
ax[3].set_xlabel('x',font1)
ax[3].set_ylabel('y',font1)
plt.show()