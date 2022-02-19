#08-bar.py各种条状图绘制
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
#自定义绘制函数
#变量说明：
#      ax                 # 坐标系名称
#      x                  # 柱体在 x 轴上的坐标位置
#      height,            # 柱体的高度
#      align='center',    #  x 轴上的坐标与柱体对其的位置
#      color='bisque',    # 柱体的填充颜色
#      alpha=0.6,         # 柱体填充颜色的透明度
#      width=0.8,         # 柱体的宽度
#      bottom=None,       # 柱体基线的 y 轴坐标
#      edgecolor=None,    # 柱体的边框颜色
#      linewidth=1,       # 柱体边框线的宽度
#      ls="-"             # 柱体边框线型
#      hatch              #填充形式
#      label              #图例

def ax_draw(ax,x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label):
    ax.bar(x,height,align=align,color=color, tick_label=tick_label,
    alpha=alpha, width=width,bottom=bottom, edgecolor=edgecolor, lw=lw,ls=ls,hatch=hatch,label=label)
    ax.set_title(title,fontsize=16)
    ax.legend(fontsize=16,edgecolor="b")
fig,ax=plt.subplots(2,4,figsize=(16,8))#设置2×4图组
#绘制六个实验成功率数据      
x=['有机','无机','物化','电工','金工','建工']
height=[86,93,78,90,92,86]
align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label="center","gray",x,0.5,0.8,0.5,"None",1,"-","","A"
title="默认绘制"
ax_draw(ax[0,0],x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label)
ax[0,0].set_ylabel("实验成功率（%）", size=16)       
#ax[0,0].set_xlabel("实验名称", size=18)     
#柱体边缘对齐绘制粉色填充
x=np.arange(0,6)
height=[18,5,32,21,19,7]
align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label="edge","pink",x,0.5,0.8,0.5,"None",1,"-","","B"
title="柱体边缘对齐粉色填充"
ax_draw(ax[0,1],x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label)
#显示柱体边框线条
x=np.arange(0,6)
height=[18,5,32,21,19,7]
align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label="edge","pink",x,0.5,0.8,0.5,"blue",3,"-","","C"
title="显示柱体边框线条"
ax_draw(ax[0,2],x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label)
#显示剖面线填充
x=np.arange(0,6)
height=[18,5,32,21,19,7]
align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label="edge","pink",x,0.5,0.8,0.5,"blue",3,"-","////","D"
title="显示剖面线填充"
ax_draw(ax[0,3],x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label)
#同类数据垂直叠加
x=['有机','无机','物化','电工','金工','建工']
height=[86,93,78,90,92,85]
bottom=[87,92,81,91,86,89]
ax[1,0].bar(x,bottom,color="r",label="A班",hatch="////",edgecolor="b")
ax[1,0].bar(x,height,tick_label=x,alpha=0.5,label="B班",bottom=bottom,hatch="//",edgecolor="b")
ax[1,0].legend()
ax[1,0].set_ylabel("实验成功率（%）", size=16)     
ax[1,0].set_title("同类数据垂直叠加",fontsize=16)
#同类数据水平比较
tkl=['有机','无机','物化','电工','金工','建工']
x=np.arange(0,6)
height1=[66,93,78,74,92,85]
height2=[87,75,81,91,86,69]
ax[1,1].bar(x,height1,width=0.3,color="r",label="A班",hatch="////",edgecolor="b",align='edge')
ax[1,1].bar(x+0.3,height2,width=0.3,tick_label=tkl,alpha=0.5,label="B班",hatch="//",edgecolor="b",align='edge')
ax[1,1].legend()
ax[1,1].set_title("同类数据水平比较",fontsize=16)
#柱体上端标注数据
x=np.arange(0,6)
height=[18,5,32,21,19,72]
align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label="edge","pink",x,0.5,0.8,0.5,"blue",3,"-","////","G"
title="柱体上端标注数据"
ax_draw(ax[1,2],x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label) 
for x,y in enumerate(height):
   ax[1,2].text(x+0.3,y+1,str(y))
#柱体与折线组合
x=np.arange(0,6)
height=[18,5,32,21,19,7]
align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label="center","pink",x,0.5,0.8,0.5,"blue",1,"-","////","H"
title="柱体与折线组合"
ax_draw(ax[1,3],x,height,align,color, tick_label, alpha, width,bottom, edgecolor, lw,ls,hatch,label)
ax[1,3].plot(x,height+0.5*np.ones(6),lw=2,color="r")
plt.subplots_adjust(0.05,0.05,0.95,0.95,wspace=0.1,hspace=0.1)
#plt.tight_layout()**使用此语句系统可能出错，提示无法安排全部内容，建议用adjust语句
plt.show()
