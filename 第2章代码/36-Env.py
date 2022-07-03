#某市气候环境数据径向柱状图
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm#,colors
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
import matplotlib  as mpl
#全局设置字体
mpl.rcParams["font.sans-serif"]=["FangSong"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 18#设置字体大小
#mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
font1 = {'family': 'Times New Roman'} 
labels=[]
for i in range(12):
       label=str(i+1)+"月"
       labels.append(label)
print(labels)

#temperature, rainfall, environmental index
#温度，降雨量，环境指数
Tem=np.array([15,18,20,23,25,27,31,33,32,28,24,20])#°C
Rainfall=np.array([9,11,21,27,25,21,12,8,11,7,10,6])#cm为单位
E_index=np.array([31,28,26,29,25,23,20,22,18,19,29,28])#32为最佳环境

def ax_draw(ax,x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label):
    ax.bar(x,height,align=align,color=color, tick_label=tick_label,
    alpha=alpha, width=width,bottom=bottom, edgecolor=edgecolor, lw=lw,ls=ls,hatch=hatch,label=label)
    ax.set_title(title,fontsize=22)
    ax.legend(fontsize=16,edgecolor="b")
N=len(Tem)
fig = plt.figure(figsize=(8,6), dpi=100)
ax = plt.subplot(111, polar=True)
# 绘制径向柱状图图
angles = np.linspace(0, 2*np.pi,N,endpoint=False)
width=2*np.pi/N-0.05#留下一点缝隙
x=angles
height=Tem
DT=max(Tem)-min(Tem)
c =mpl.cm.Spectral_r((Tem-min(Tem))/float(DT))
align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label="center",c,labels,1,width,0,"k",1,"-","","温度"
title="某市气候环境径向柱状图绘制"
ax_draw(ax,x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label)

height=Rainfall
DF=max(Rainfall)-min(Rainfall)
c =mpl.cm.Blues((Rainfall-min(Rainfall))/float(DF))  
align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label="center",c,labels,1,width,Tem,"k",1,"-","","降雨量"
ax_draw(ax,x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label)

height=E_index
bottom=Tem+Rainfall
#print(bottom)
DE=max(E_index)-min(E_index)
c =mpl.cm.copper((E_index-min(E_index))/float(DE))  
align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label="center",c,labels,1,width,bottom,"k",1,"-","","环境指数"
ax_draw(ax,x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label)

ax.set_theta_direction(-1)
plt.legend(bbox_to_anchor=(1.3,1.03))
plt.ylim(0,90)
ax.spines['polar'].set_visible(False)


ax2 = fig.add_axes([0.76, 0.45, 0.02, 0.3])
cmap = mpl.cm.Spectral_r
norm = mpl.colors.Normalize(vmin=15, vmax=33)
bounds = np.arange(15,35.1,0.1)
#norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap,norm=norm,boundaries=bounds,ticks=np.arange(15,35.1,5)
                                ,spacing='proportional',label='Temperature,℃')


ax3 = fig.add_axes([0.84, 0.45, 0.02, 0.3])
cmap = mpl.cm.Blues
norm = mpl.colors.Normalize(vmin=min(Rainfall), vmax=max(Rainfall))
bounds = np.arange(min(Rainfall),max(Rainfall)+0.1,0.1)
#norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
cb3 = mpl.colorbar.ColorbarBase(ax3, cmap=cmap,norm=norm,boundaries=bounds,ticks=np.arange(min(Rainfall)
      ,max(Rainfall),5),spacing='proportional',label='Rainfall,cm')


ax4 = fig.add_axes([0.92, 0.45, 0.02, 0.3])
cmap = mpl.cm.copper
norm = mpl.colors.Normalize(vmin=min(E_index), vmax=max(E_index))
bounds = np.arange(min(E_index),max(E_index)+0.1,0.1)
#print(cmap.N)

#norm = mpl.colors.BoundaryNorm(bounds, 256)
cb4 = mpl.colorbar.ColorbarBase(ax4, cmap=cmap,norm=norm,boundaries=bounds,ticks=np.arange(min(E_index)
      ,max(E_index),5),spacing='proportional',label='E_index')

plt.show()

