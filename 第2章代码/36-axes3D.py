#36-axex3D.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
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

#数据处理




def title_and_lablim(ax, title):#常规坐标轴特性设置，可通用
    ax.set_title(title)
    ax.set_xlabel("$x$", fontsize=16)
    ax.set_ylabel("$y$", fontsize=16)
    ax.set_zlabel("$z$", fontsize=16)
    ax.set_xlim(-5,5.1)
    ax.set_ylim(-5,5.1)
    ax.set_xticks(np.arange(-5,5.1,2))
    ax.set_yticks(np.arange(-5,5.1,2))
    
t = np.arange(0, 5*np.pi, 0.01)#将x从-5到5，间隔0.02进行取点
x=5*np.sin(2*t)
y=5*np.cos(2*t)
z=0.5*t
fig=plt.figure()
#线条绘制
ax=fig.add_subplot(2,3,1,projection='3d' )
p = ax.plot(x,y,z,c="m")
title_and_lablim(ax, "plot_3Dline")
#散点线条绘制
t = np.arange(0, 5*np.pi, 0.1)#将x从-5到5，间隔0.02进行取点
x=5*np.sin(2*t)
y=5*np.cos(2*t)
z=0.5*t
ax=fig.add_subplot(2,3,2,projection='3d' )
p = ax.scatter(x,y,z,c="blue",marker="*",s=20)
title_and_lablim(ax, "plot_3Dscatter")
#随机散点
ax=fig.add_subplot(2,3,3,projection='3d' )
x=2*np.random.randn(300)
y=2*np.random.randn(300)#随机产生300个数据
z=np.random.randn(300)
p=ax.scatter(x,y,z,c=z,cmap=mpl.cm.RdYlBu,marker="o",s=60,zdir="z")
fig.colorbar(p, ax=ax,shrink=0.5)
title_and_lablim(ax, "plot_randscatter")
#3D柱状图绘制
ax=fig.add_subplot(2,3,4,projection='3d' )
tkl=['有机','无机','物化','电工','金工','建工']
x=np.arange(0,6)
h1=[66,93,78,74,92,85]
h2=[87,75,81,91,86,69]
h3=[77,85,91,83,76,94]
ax.bar(x,h1,width=0.3,zs=0,zdir="y",tick_label=tkl,color="r",label="A班",hatch="////",edgecolor="b",align='edge')
ax.bar(x,h2,width=0.3,zs=2,zdir="y",alpha=0.5,label="B班",hatch="//",edgecolor="b",align='edge')
ax.bar(x,h3,width=0.3,zs=4,zdir="y",alpha=0.5,label="C班",hatch="//",edgecolor="b",align='edge')
ax.set(zlabel="z",yticks=[0,2,4],
       yticklabels=["A班","B班","C班"] )
ax.set_title("三个班级各科平均成绩比较")
#渐开线3D柱状图
ax=fig.add_subplot(2,3,5,projection='3d' )
thta=np.linspace(0,2*np.pi,12)
x=3*thta*np.cos(thta)
y=3*thta*np.sin(thta)
z=3*thta
p = ax.bar3d(x, y, 0* np.ones_like(x),
                     0.9* np.ones_like(x), 0.9 * np.ones_like(x),z,color="red",edgecolor="b")
ax.plot(x,y,z,c="b")
ax.set_title("渐开线立体柱状图")
ax.set(zlabel="z",xlabel="x",ylabel="y")

ax=fig.add_subplot(2,3,6,projection='3d' )
tkl=['有机','无机','物化','电工','金工','建工']
y=np.arange(0,6)
h1=[66,93,78,74,92,85]
h2=[87,75,81,91,86,69]
h3=[77,85,91,83,76,94]
ax.bar(y,h1,width=0.3,zs=0,zdir="x",color="r",label="A班",hatch="////",edgecolor="b",align='center')
ax.bar(y,h2,width=0.3,zs=2,zdir="x",alpha=0.5,label="B班",hatch="//",edgecolor="b",align='center')
ax.bar(y,h3,width=0.3,zs=4,zdir="x",alpha=0.5,label="C班",hatch="//",edgecolor="b",align='center')
ax.set(zlabel="z",xticks=[0,2,4],xticklabels=["A班","B班","C班"],
       yticks=np.arange(0,6),yticklabels=tkl)
ax.set_title("三个班级各科平均成绩比较")
fig.tight_layout()
plt.show()