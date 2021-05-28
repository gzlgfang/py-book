#12-NLP_draw.py
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
def func(x):
    return x[0]**2-2*x[0]-4*x[1]
def cons(x):
    constr1=4-4*x[0]**2-x[1]**2+x[0]*x[1]

x = np.arange(0, 2.5, 0.01)
y = np.arange(0, 2.5, 0.01)
X, Y = np.meshgrid(x, y)
Z= X**2 -2*X-4* Y
norm = mpl.colors.Normalize((Z).min(), (Z).max())
#布局设置
fig, ax = plt.subplots(1, 1, figsize=(8, 8) )
p=ax.contour(X, Y, Z, 50, cmap=mpl.cm.RdBu,norm=norm)#cmpa共有170种
plt.colorbar(p, ax=ax)

ax.text(0.4,2,'*',va='bottom',ha='center')

ax.set_title("等高线+约束条件绘制") 
font1 = {'family': 'Times New Roman'}  
ax.set_xlabel('x',font1)
ax.set_ylabel('y',font1)
x1=np.linspace(0,1,101)
y1=(x1+np.sqrt(16-15*x1**2))/2
xx=np.zeros(103)
yy=np.zeros(103)
for i in range(101):
    xx[i+1] = x1[i]
    yy[i+1] = y1[i]
xx[102]=1
yy[102]=0
ax.fill(xx,yy,c="lightblue",lw=2)
plt.show()