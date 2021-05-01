#subplot2grid布局
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"] = 12
mpl.rcParams["font.style"] = "oblique"
#normal	默认值，正常体
#italic	斜体，这是一个属性
#oblique 将字体倾斜，将没有斜体变量（italic）的特殊字体，要应用oblique

mpl.rcParams["font.weight"] ="bold"# "normal",=40


plt.figure(figsize=(12,16),num="subplot2grid布局")

ax1=plt.subplot2grid((3,4),(0,0),colspan=2)
ax1.set_title("ax1布局位置参数="+"(3,4),(0,0),colspan=2",fontsize=12 ,fontstyle= "oblique",fontweight =900)
x1=np.linspace(0,3*np.pi,500)
y1=3*np.cos(1.5*x1)
ax1.plot(x1,y1,lw=2)#绘制x1和y1之间的函数曲线
ax1.set_xticks([])
ax1.set_yticks([])


ax2=plt.subplot2grid((3,4),(1,0),colspan=2,rowspan=2)
ax2.set_title("ax2布局位置参数="+"(3,4),(1,0),colspan=2,rowspan=2",fontsize=12)
x2=np.arange(1,7)
y2=[3,8,1,5,7,4]
ax2.bar(x2,y2,color="pink",align="center",hatch="//")
ax2.set_xticks([])
ax2.set_yticks([])

ax3=plt.subplot2grid((3,4),(0,2),rowspan=3)
ax3.set_title("ax3布局位置参数="+"(3,4),(0,2),rowspan=3",fontsize=12)
x3=np.linspace(1,10,10)
y3=np.random.randn(10)
ax3.stem(x3,y3,linefmt="-.",markerfmt="*",basefmt="-")#linefmt=棉棒的样式，markerfmt=棉棒末端样式,basefmt=基线样式)
ax3.set_xticks([])
ax3.set_yticks([])

ax4=plt.subplot2grid((3,4),(0,3))
ax4.set_title("ax4布局位置参数="+"(3,4),(0,3)",fontsize=12)
labels=["数学","化学","物理","哲学"]
students=[0.35,0.25,0.10,0.30]
colors=["red","blue","green","pink"]
explode=(0.1,0.1,0.1,0.1)
ax4.pie(students,explode=explode,labels=labels,startangle=45,shadow=True,
        colors=colors,autopct="%3.1f%%")

ax5=plt.subplot2grid((3,4),(1,3),rowspan=2)
ax5.set_title("ax5布局位置参数="+"(3,4),(1,3),rowspan=2",fontsize=12)
x5=np.linspace(1,10,10)
y5=np.random.randn(10)
ax5.errorbar(x5,y5,fmt="bo:",yerr=0.2,xerr=0.1)
ax5.set_xticks([])
ax5.set_yticks([])
#plt.subplots_adjust(wspace=0.1,hspace=0.1)
#plt.tight_layout()
plt.show()