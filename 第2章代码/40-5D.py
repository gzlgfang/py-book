#40-5D.py
#某空间区域微粒大小及浓度分布图
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from matplotlib import cm, ticker#,colors
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
x,y,z,radius, concentration=[],[],[],[],[]
for i in range(10):#随机产生微粒半径和浓度数据
        for j in range(10):
            for k in range(10):
                x.append(i+1)
                y.append(j+1)
                z.append(k+1)
                rnd1=100*rnd.random()
                radius.append(rnd1)
                rnd2=100*rnd.random()
                concentration.append(rnd2)
x=np.array(x)
y=np.array(y)
z=np.array(z)
radius, concentration=np.array(radius), np.array(concentration)
norm = mpl.colors.Normalize(0, 100)#确定映射数据范围
#DT=max(concentration)-min(concentration)
#c =mpl.cm.Spectral_r(concentration-min(concentration)/(DT))#cmap=mpl.cm.RdYlBu

fig=plt.figure(figsize=(8,6),dpi=100)#设置布局
ax=fig.add_subplot(1,1,1,projection='3d' )#设置第一子图ax
p=ax.scatter(x,y,z,c=concentration,cmap=mpl.cm.RdYlBu,marker="o",norm=norm,s=radius,zdir="z")
ax.set(xlabel="x",ylabel="y",zlabel="z")
fig.colorbar(p, ax=ax,shrink=1,label="浓度")
ax.set_title("空间污染状况五维数据可视图")

#设置第二子图
loc1=(0.2,0.2,0.1,0.4)
ax1=fig.add_axes(loc1)
x=np.array(5*[0.3])
y=np.array([0.2,0.4,0.6,0.8,1])
s=100*y
ax1.scatter(x,y,marker="o",s=s)
ax1.spines['right'].set_color('none')#取消坐标轴
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_color('none')
ax1.spines['left'].set_color('none')
ax1.axes.xaxis.set_visible(False)
ax1.axes.yaxis.set_visible(False)
ax1.text(0.29,0.1,"污染颗粒直径")
for i in range(5):
    str1=str((i+1)*20)
    ax1.text(.305,0.195*(i+1),str1)
plt.show()