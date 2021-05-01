#22-axes_set.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
#设置刻度线朝内
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
mpl.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 16#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
#normal	默认值，正常体
#italic	斜体，这是一个属性
#oblique 将字体倾斜，将没有斜体变量（italic）的特殊字体，要应用oblique
#cy_color= ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'
# , '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
#设置单个画布
plt.figure(num="坐标轴名称及范围设置",figsize=(8,8))
x=np.linspace(0,6*np.pi,500)
y=3*np.cos(x)
plt.plot(x,y,lw=2)#绘制x和y之间的函数曲线
plt.xlabel("x",fontname="serif")
plt.ylabel("y",labelpad=5,fontname="serif")
#plt.spines['bottom'].position(('data', 2))无此特性

plt.xlim(0,18)#设置x轴范围
#plt.xaxis.set_major_locator(mpl.ticker.MaxNLocator(5))单个画布无此方法可调用只能在subplots布局中
#plt.xaxis.set_minor_locator(mpl.ticker.MaxNLocator(5))

#plt.figure(num="删除部分坐标轴",figsize=(8,8))
x=np.linspace(0,6*np.pi,500)
y=3*np.cos(x)
plt.plot(x,y,lw=2)#绘制x和y之间的函数曲线
plt.xlabel("x",fontname="serif")
plt.ylabel("y",labelpad=5,fontname="serif")
#plt.grid(which="both")
plt.grid(True)
plt.xlim(0,18)#设置x轴范围





#plt.tick_params(top='on', right='on') # 显示上侧和右侧的刻度
#设置2×4布局
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'
mpl.rcParams['ytick.right']=False
mpl.rcParams['xtick.top']=False


fig,ax=plt.subplots(2,5,figsize=(15,6))
ax[0,0].plot(x,y,lw=2,color="b")#
ax[0,0].set_xlabel(r"$x$")
ax[0,0].set_ylabel("y",labelpad=3)
ax[0,0].set_xlim(0,18)
ax[0,0].set_ylim(-3,3)#设置y轴范围
ax[0,0].set_title("设置数字坐标范围")
#ax[0,0].tick_params(direction = 'out')

x2=("A","B","C","D","E","F","G")
#x2=np.arange(7)
ax[0,1].plot(x2,x2,lw=2,color="r")#
ax[0,1].set_xlim("B","F")#设置x轴范围
ax[0,1].set_title("设置字符串坐标范围")
#ax[0,1].tick_params(direction = 'out')
#ax[0,1].spines['right'].set_ytick(True)
#设置刻度线朝内
ax[0,2].plot(x,y**2,lw=2,color="m")#
ax[0,2].set_title("坐标刻度线朝内")
ax[0,2].tick_params(direction ='in')

#设置顶部和右边坐标轴刻度线
x4=np.linspace(-12,6*np.pi,500)
y4=3*np.sin(x4-5)/(x4-5)
ax[0,3].plot(x4,y4,lw=2,color="b")#
ax[0,3].set_title("设置顶部和右边坐标轴刻度线")
ax[0,3].tick_params(top='on', right='on', which='both',direction = 'in')

#设置主次刻度线
x5=np.linspace(-12,6*np.pi,500)
y5=3*np.sin(x5-5)/(x5-5)
ax[0,4].plot(x5,y5,lw=2,color='#2ca02c')#
ax[0,4].set_title("设置主次刻度线")
ax[0,4].tick_params(top='on', right='on', which='both',direction = 'in')
ax[0,4].xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))#主刻度间隔4
ax[0,4].xaxis.set_minor_locator(mpl.ticker.MultipleLocator(2.5))#次刻度间隔2
ax[0,4].yaxis.set_major_locator(mpl.ticker.MaxNLocator(10))#主刻度最大10个
ax[0,4].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(10))#
ax[0,4].set_xlim(-12.5,20)
ax[0,4].set_ylim(-1,3.1)

#任意设置刻度线
x5=np.linspace(-12,6*np.pi,500)
y5=3*np.sin(x4-5)/(x4-5)
ax[1,0].plot(x4,y4,lw=2,color='#d62728')#
ax[1,0].set_title("设置任意刻度线")
ax[1,0].tick_params(top='on', right='on', which='both',direction = 'in')
ax[1,0].set_xticks(np.arange(-14,21,4))
ax[1,0].set_yticks(np.arange(-1,3.1,0.25))
ax[1,0].set_xlim(-14,21)
ax[1,0].set_ylim(-1,3.1)

#设置pi刻度线
x5=np.linspace(-12,6*np.pi,500)
y5=3*np.sin(x5-5)/(x5-5)
ax[1,1].plot(x5,y5,lw=2,color='#9467bd')#
ax[1,1].set_title("设置pi刻度线")
ax[1,1].tick_params(top='on', right='on', which='both',direction = 'in')
x_labels=[r"$-4\pi$" ,r"$-2\pi$",0,r"$2\pi$",r"$4\pi$",r"$6\pi$"]
ax[1,1].set_xticks(np.arange(-4*np.pi,7*np.pi,2*np.pi))
ax[1,1].set_xticklabels(x_labels,rotation=0,alpha=1)
ax[1,1].set_yticks(np.arange(-1,3.1,0.5))
ax[1,1].set_xlim(-14,21)
ax[1,1].set_ylim(-1,3.1)


#取消坐标轴
x=np.linspace(-10,10,201)
y=0.01*(x+8)*(x+4)*(x-8)*(x-4)
ax[1,2].plot(x,y,lw=2,color='#e377c2')#
ax[1,2].spines['right'].set_color('none')
ax[1,2].spines['top'].set_color('none')
ax[1,2].spines['bottom'].set_position(('data', 0))
ax[1,2].spines['left'].set_position(('data',0))
ax[1,2].set_xticks(np.arange(-9,10,3))
ax[1,2].set_title("取消顶部和右边坐标轴")

#x坐标轴移到y=10
x=np.linspace(-10,10,201)
y=0.01*(x+8)*(x+4)*(x-8)*(x-4)
ax[1,3].plot(x,y,lw=2,color='#bcbd22')#
ax[1,3].spines['right'].set_color('none')
ax[1,3].spines['top'].set_color('none')
ax[1,3].spines['bottom'].set_position(('data', 10))
ax[1,3].spines['left'].set_position(('data',0))
ax[1,3].set_xticks(np.arange(-9,10,3))
ax[1,3].set_title("x坐标轴移到y=10")

#y坐标轴移到x=4
x=np.linspace(-10,10,201)
y=0.01*(x+8)*(x+4)*(x-8)*(x-4)
ax[1,4].plot(x,y,lw=2,color='#7f7f7f')#
ax[1,4].spines['right'].set_color('none')
ax[1,4].spines['top'].set_color('none')
ax[1,4].spines['bottom'].set_position(('data', 0))
ax[1,4].spines['left'].set_position(('data',4))
ax[1,4].set_xticks(np.arange(-9,10,3))
ax[1,4].set_title("y坐标轴移到x=4")





plt.subplots_adjust(wspace=0.2,hspace=0.3)



#plt.tight_layout()#和上面adjust语句功能相同
plt.show()