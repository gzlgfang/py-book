#本文标注26-arrow_set.py
import matplotlib  as mpl
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

#mpl.rcParams['axes.grid']=True
#normal	默认值，正常体
#italic	斜体，这是一个属性
#oblique 将字体倾斜，将没有斜体变量（italic）的特殊字体，要应用oblique
#cy_color= ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'
# , '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']


#设置1×3布局
fig,ax=plt.subplots(1,3,figsize=(18,6))
x5=np.linspace(-12,6*np.pi,500)
y5=3*np.sin(x5-5)/(x5-5)
ax[0].plot(x5,y5,lw=2,color='#2ca02c')#
ax[0].set_title("普通箭头")
ax[0].tick_params( right='on', which='both',direction = 'in')
ax[0].xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))#主刻度间隔5
ax[0].yaxis.set_major_locator(mpl.ticker.MaxNLocator(10))#主刻度最大10个
ax[0].annotate( '最高点', xy=(5,3), xytext=(10,2.4), arrowprops=dict(arrowstyle='->',color="r"))
ax[0].set_xlim(-12.5,20)
ax[0].set_ylim(-1,3)


ax[1].plot(x5,y5,lw=2,color='#d62728')#
ax[1].set_title("加框文本箭头")
ax[1].tick_params(top='on', right='on', which='both',direction = 'in')
ax[1].xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))#主刻度间隔5
ax[1].xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2.5))#次刻度间隔2.5
ax[1].yaxis.set_major_locator(mpl.ticker.MaxNLocator(10))#主刻度最大10个
ax[1].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(20))#
ax[1].annotate('主刻度线',xy=(5,-0.97),xytext=(12,-0.6) ,bbox=dict( facecolor="w",alpha=1,edgecolor='b',lw=2),
                arrowprops=dict(arrowstyle='->',color="b"))
ax[1].set_xlim(-12.5,20)
ax[1].set_ylim(-1,3)


ax[2].plot(x5,y5,lw=2,color='#1f77b4')#
ax[2].set_title("上色文本双箭头")
ax[2].tick_params(top='on', right='on', which='both',direction = 'in')
ax[2].xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))#主刻度间隔4
ax[2].xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2.5))#次刻度间隔2
ax[2].yaxis.set_major_locator(mpl.ticker.MaxNLocator(10))#主刻度最大10个
ax[2].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(20))#
ax[2].annotate('次高点',xy=(12.5,0.38),xytext=(11,1.3) ,bbox=dict( facecolor="pink",alpha=0.5,edgecolor='b',lw=2),
               arrowprops=dict(arrowstyle='<->',color="g"))
                     
ax[2].set_xlim(-12.5,20)
ax[2].set_ylim(-1,3)



plt.show()
