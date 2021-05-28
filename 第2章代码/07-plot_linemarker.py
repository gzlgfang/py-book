#07-plot_linemarker.py#plot函数应用
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
#自定义绘制函数
def ax_draw(ax,x,y,title,lw,ls,color,marker,markersize,label):
    ax.plot(x,y,lw=lw,ls=ls,color=color,label=label,marker=marker,markersize=markersize)
    ax.set_title(title,fontsize=18)
    ax.legend(fontsize=18)
fig,ax=plt.subplots(2,4,figsize=(2,16))#设置2×4图组
#绘制线性关系曲线
x=np.linspace(0,10,11)
y=2*x+2
title,lw,ls,color,marker,markersize,label="线条与标记",2,"-.","b","*",12,"A"
ax_draw(ax[0,0],x,y,title,lw,ls,color,marker,markersize,label)
#绘制圆关系曲线
x=np.linspace(-5,5,201)
y=np.sqrt(25-x**2)
title,lw,ls,color,marker,markersize,label="纯圆线条",2,"-","r","",0,"B"
ax_draw(ax[0,1],x,y,title,lw,ls,color,marker,markersize,label)
label=""
ax_draw(ax[0,1],x,-y,title,lw,ls,color,marker,markersize,label)
#绘制倒三角点图
x=np.linspace(0,10,21)
y=x**2-4*x
title,lw,ls,color,marker,markersize,label="倒三角点图",2,"","m","v",12,"C"
ax_draw(ax[0,2],x,y,title,lw,ls,color,marker,markersize,label)

#绘制泡泡图
x=np.linspace(0,20,21)
y=np.random.randn(21)
title,lw,ls,color,marker,markersize,label="泡泡图",1,"-","g","o",12,"D"
ax_draw(ax[0,3],x,y,title,lw,ls,color,marker,markersize,label)

#绘制班级人数统计
x=['A班','B班','C班','D班','E班','F班']
y=[46,42,51,57,38,47]
title,lw,ls,color,marker,markersize,label="班级人数统计",2,"-","b","o",12,"E"
ax_draw(ax[1,0],x,y,title,lw,ls,color,marker,markersize,label)
ax[1,0].set_ylim(min(y)-2,max(y)+2)

#绘制显示数据点图线
x=['氮','磷','钾','钙','锌']
y=[0.36,0.16,0.25,0.21,0.04]
title,lw,ls,color,marker,markersize,label="显示数据点图线",2,"-","r","H",8,"F"
ax_draw(ax[1,1],x,y,title,lw,ls,color,marker,markersize,label)
for i,yy in enumerate(y):
    ax[1,1].text(i+0.2,yy,str(yy))
ax[1,1].set_xlim(-0.5,len(x))

#绘制显示水平垂直辅助线数据图
x=np.linspace(0,4*np.pi,201)
y=np.sin(x)
title,lw,ls,color,marker,markersize,label="水平垂直辅助线数据图",2,"-","m","",12,"G"
ax_draw(ax[1,2],x,y,title,lw,ls,color,marker,markersize,label)
ax[1,2].axhline(y=-1,ls=":",lw=2,c="r")
ax[1,2].axhline(y=1,ls=":",lw=2,c="r")
ax[1,2].axhline(y=0,ls=":",lw=2,c="r")
ax[1,2].axvline(x=2.5*np.pi,ls=":",lw=2,c="b")
#绘制显示水平垂直辅助区域数据图
x=np.linspace(0,4*np.pi,201)
y=np.sin(x)
title,lw,ls,color,marker,markersize,label="水平垂直辅助区域数据图",2,"-","g","",12,"H"
ax_draw(ax[1,3],x,y,title,lw,ls,color,marker,markersize,label)
ax[1,3].axhspan(ymin=-0.5,ymax=0.5,ls="-",lw=4,facecolor='b',alpha=0.5,edgecolor='r')
ax[1,3].axvspan(xmin=1.5*np.pi,xmax=2.5*np.pi,ls="-",lw=4,facecolor='b',alpha=0.5,edgecolor='r')



plt.show()