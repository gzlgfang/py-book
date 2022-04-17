import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
fig=plt.figure(figsize=(8,16),num="subplot(ijn)布局")
axes_num=[241,242,243,244,245,246,247,248]#布局图号列表
for i,axn in enumerate(axes_num):
    ax=plt.subplot(axn)#将布局图号为axn的子图赋给ax,以便后续用ax调用
    x= np.linspace(0, 3*np.pi, 100)
    y=np.sin(x)**(i+1)#调整次方
    ax.plot(x,y,lw=2)#可以添加其他各种属性
    plt.title('subplot('+str(axn)+')')
    #ax.set_title('subplot('+str(axn)+')')
    plt.axhline(y=0,ls="--",c="r")#绘制水平线
    plt.xticks([])#隐藏刻度线
    plt.yticks([])
plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.tight_layout()#和上面adjust语句功能相同
plt.show()
