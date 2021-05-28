#图中图绘制布局策略fig_in_fig
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
fig=plt.figure(figsize=(16,8),num="图中图布局策略")
#主图绘制
loc1=(0.1,0.1,0.85,0.85)
ax1=fig.add_axes(loc1,facecolor="#e1e1e1")
x1=np.linspace(0,50,500)
y1=2*np.sin(x1)*np.exp(-x1/8)
ax1.plot(x1,y1,color='r')
ax1.set_xlim(0,51)

#图中图绘制
ax1.axvline(20,ymax=0.5,c="r",ls=":")
ax1.axvline(40,ymax=0.5,c="r",ls=":")
loc2=(0.57,0.55,0.35,0.35)
ax2=fig.add_axes(loc2,facecolor="none")
x2=np.linspace(20,40,500)
y2=2*np.sin(x2)*np.exp(-x2/8)
ax2.plot(x2,y2,color='b')
plt.show()

