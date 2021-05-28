#画布figure添加fig_add_axes布局策略
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
fig=plt.figure(figsize=(16,8),facecolor="white",num="fig_add_axes布局策略")
loc1=(0.05,0.05,0.4,0.4)
ax1=fig.add_axes(loc1,facecolor="#e1e1e1")
x1=np.linspace(0,3*np.pi,500)
y1=2*np.sin(x1)**2
ax1.plot(x1,y1,color='r')
ax1.set_title("三角函数绘制loc1="+str(loc1),fontsize=12)

loc2=(0.55,0.05,0.4,0.4)
ax2=fig.add_axes(loc2,facecolor="#e1e1e1")
x2=np.linspace(0,100,300)
y2=3*np.log(x2)+1
ax2.plot(x2,y2,color='b')
ax2.set_title("对数函数绘制loc2="+str(loc2),fontsize=12)

loc3=(0.05,0.55,0.4,0.4)
ax3=fig.add_axes(loc3,facecolor="#e1e1e1")
x3=np.linspace(0,10,300)
y3=2*x3**1.2
ax3.plot(x3,y3,color='g')
ax3.set_title("1.2次方函数绘制loc3="+str(loc3),fontsize=12)

loc4=(0.55,0.55,0.4,0.4)
ax4=fig.add_axes(loc4,facecolor="#e1e1e1")
x4=np.linspace(0,10,300)
y4=5*np.exp(-0.1*x4**2+3)
ax4.plot(x4,y4,color='purple',lw=2)
ax4.set_title("指数衰减函数绘制loc4="+str(loc4),fontsize=12)
plt.figure(num="fig_add_axes布局策略")
plt.show()
