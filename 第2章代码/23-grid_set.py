#23-grid_set.py
import matplotlib  as mpl
from matplotlib.colors import rgb_to_hsv
import matplotlib.pyplot as plt
import numpy as np
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
#mpl.rcParams['axes.grid']=True
#normal	默认值，正常体
#italic	斜体，这是一个属性
#oblique 将字体倾斜，将没有斜体变量（italic）的特殊字体，要应用oblique
#cy_color= ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'
# , '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
#设置单个画布
plt.figure(num="单个画布网格线设置",figsize=(8,8))
x=np.linspace(0,6*np.pi,500)
y=3*np.cos(x)
plt.plot(x,y,lw=2,color="b")#绘制x和y之间的函数曲线
plt.xlabel("x",fontname="serif")
plt.ylabel("y",labelpad=5,fontname="serif")
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.xlim(0,18)#设置x轴范围


plt.figure(num="默认网格线设置",figsize=(8,8))
x=np.linspace(0,6*np.pi,500)
y=3*np.cos(x)
plt.plot(x,y,lw=2)#绘制x和y之间的函数曲线
plt.xlabel("x",fontname="serif")
plt.ylabel("y",labelpad=5,fontname="serif")
#plt.grid(which="both")
plt.grid()
plt.xlim(0,18)#设置x轴范围





#plt.tick_params(top='on', right='on') # 显示上侧和右侧的刻度
#设置2×4布局


fig,ax=plt.subplots(1,4,figsize=(16,4))
x5=np.linspace(-12,6*np.pi,500)
y5=3*np.sin(x5-5)/(x5-5)
ax[0].plot(x5,y5,lw=2,color='#2ca02c')#
ax[0].set_title("默认网格线设置")
ax[0].tick_params(top='on', right='on', which='both',direction = 'in')
ax[0].xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))#主刻度间隔4
ax[0].xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2.5))#次刻度间隔2
ax[0].yaxis.set_major_locator(mpl.ticker.MaxNLocator(10))#主刻度最大10个
ax[0].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(10))#
ax[0].set_xlim(-12.5,20)
ax[0].set_ylim(-1,3)
ax[0].grid()

ax[1].plot(x5,y5,lw=2,color='#d62728')#
ax[1].set_title("主刻度网格线设置")
ax[1].tick_params(top='on', right='on', which='both',direction = 'in')
ax[1].xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))#主刻度间隔4
ax[1].xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2.5))#次刻度间隔2
ax[1].yaxis.set_major_locator(mpl.ticker.MaxNLocator(10))#主刻度最大10个
ax[1].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(10))#
ax[1].set_xlim(-12.5,20)
ax[1].set_ylim(-1,3)
ax[1].grid(which='major',color='b', linestyle=':', linewidth=1.5)

ax[2].plot(x5,y5,lw=2,color='#1f77b4')#
ax[2].set_title("主次刻度网格线设置")
ax[2].tick_params(top='on', right='on', which='both',direction = 'in')
ax[2].xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))#主刻度间隔4
ax[2].xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2.5))#次刻度间隔2
ax[2].yaxis.set_major_locator(mpl.ticker.MaxNLocator(10))#主刻度最大10个
ax[2].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(10))#
ax[2].set_xlim(-12.5,20)
ax[2].set_ylim(-1,3)
ax[2].grid(color="purple", which="both", linestyle=':', linewidth=1.5)

ax[3].plot(x5,y5,lw=2,color='#ff7f0e')#
ax[3].set_title("x轴单独设置网格线")
ax[3].tick_params(top='on', right='on', which='both',direction = 'in')
ax[3].xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))#主刻度间隔4
ax[3].xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2.5))#次刻度间隔2
ax[3].yaxis.set_major_locator(mpl.ticker.MaxNLocator(10))#主刻度最大10个
ax[3].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(10))#
ax[3].set_xlim(-12.5,20)
ax[3].set_ylim(-1,3)
ax[3].grid(which='both',axis='x',color='m', linestyle=':', linewidth=1.5)
plt.show()