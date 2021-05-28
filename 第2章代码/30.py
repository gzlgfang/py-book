#30.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
#设置刻度线朝内
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
mpl.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 18#设置字体大小
fig,ax=plt.subplots(figsize=(12,6))
x=np.linspace(0,30,301)
y=x-4*x*np.sin(2*x)-2
ax.plot(x,y,lw=2,color='b')#
ax.spines['right'].set_color('none')#取消坐标轴
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data',0))
ax.set_xticks(np.arange(3,31,3))
ax.set_yticks(np.arange(-100,140,20))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1.5))#次刻度间隔1.5
ax.set_xlim(-0.25,32)
ax.set_ylim(-105,145)
ax.fill([31,32,31,31],[3,0,-3,3],c="k")#x坐标箭头
ax.fill([0.20,0,-0.20,-0.20],[125,145,125,125],c="k")#y坐标箭头
#ax.annotate('',xy=(32,-0.1),xytext=(31.5,-0.1) , arrowprops=dict(arrowstyle='->',color="k",lw=0.8))
#ax.annotate('',xy=(0.01,145),xytext=(0.01,141) , arrowprops=dict(arrowstyle='->',color="k"))
ax.set_title("多根方程示意图")
fig.savefig("ch2-figure-30.pdf")
plt.show()