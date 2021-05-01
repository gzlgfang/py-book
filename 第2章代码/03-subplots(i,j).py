import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
fig,ax=plt.subplots(2,4,figsize=(20,4),num="subplot(i,j,**kwargs)布局")
x= np.linspace(0, 3*np.pi, 100)
dic={1:'red',2:'orange',3:'yellow',4:'green',5:'blue',6:'purple',7:'pink',8:'black'}#设置颜色字典
for i in range(1,9):#i取值为1-8，不包含9
    y=np.cos(x*(0+i)) 
    ax[i//5,i-i//5*4-1].plot(x,y,lw=2,color=dic[i]) #i//5表示行减1，i-i//5*4-1表示列号减1
    ax[i//5,i-i//5*4-1].set_title('ax['+str(i//5)+','+str(i-i//5*4-1)+'].plot')
    #plt.title('ax['+str(i//5)+','+str(i-i//5*4-1)+'].plot')
    ax[i//5,i-i//5*4-1].axhline(y=0,ls="--",c="r")#绘制水平线
    ax[i//5,i-i//5*4-1].set_xticks([])#隐藏刻度线
    #axes[i//5,i-i//5*4-1].set_yticks([])
#plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.tight_layout()#和上面adjust语句功能相同
plt.show()
