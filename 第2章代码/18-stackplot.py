#18-stackplot.py堆积折线绘制 
import matplotlib  as mpl
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=18
plt.figure(num="stackplot_draw",figsize=(16,8))
ax1=plt.subplot(121)
ax2=plt.subplot(122)
#普通堆积坐标设置
x=np.linspace(0,4*np.pi,100)
y1=np.sin(x)
y2=np.cos(x)
ax1.stackplot(x, [y1,y2],colors=["b","#66c2a5"])
title="普通堆积图"
ax1.set_title(title)
xt=[0,np.pi/2,np.pi,3/2*np.pi,2*np.pi,5/2*np.pi,3*np.pi,7/2*np.pi,4*np.pi]
x_labels=[0,r"$\pi/2$" ,r"$\pi$",r"$3\pi/2$",r"$2\pi$",r"$5\pi/2$",r"$3\pi$",r"$7\pi/2$",r"$4\pi$"]
ax1.set_xticks(xt,x_labels)
#[0,r"$\pi/2$" ,r"$\pi$",r"$3\pi/2$",r"$2\pi$",r"$5\pi/2$",r"$3\pi$",r"$7\pi/2$",r"$4\pi$"])
#设置填充图形
x=np.linspace(1,8,8)
y1=[0,2,3,5,3,7,8,9]
y2=[1,3,6,7,4,3,5,7]
y3=[2,4,7,8,3,5,10,6]
ax2.stackplot(x, y1,y2,y3,hatch='*')
title="设置填充图形"
ax2.set_title(title)
ax2.set_xticks(np.linspace(1,8,8))
ax2.set_xlim(1,8)
#plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.tight_layout()#和上面adjust语句功能相同

plt.figure()#
#普通堆积坐标设置
x=np.linspace(0,4*np.pi,100)
y1=np.sin(x)
y2=np.cos(x)
plt.stackplot(x, [y1,y2],colors=["b","#66c2a5"])
title="普通堆积图"
plt.title(title)
xt=[0,np.pi/2,np.pi,3/2*np.pi,2*np.pi,5/2*np.pi,3*np.pi,7/2*np.pi,4*np.pi]
x_labels=[0,r"$\pi/2$" ,r"$\pi$",r"$3\pi/2$",r"$2\pi$",r"$5\pi/2$",r"$3\pi$",r"$7\pi/2$",r"$4\pi$"]
plt.xticks(xt,x_labels,rotation=0,alpha=1)

plt.show()