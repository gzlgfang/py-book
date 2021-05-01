#16-stem.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=18
plt.figure(num="scatter_draw",figsize=(16,4))

ax1=plt.subplot(141)
ax2=plt.subplot(142)
ax3=plt.subplot(143)
ax4=plt.subplot(144)
#默认设置绘制
x=np.linspace(1,10,10)
y=np.random.randn(10)
ax1.stem(x,y)#linefmt=棉棒的样式，markerfmt=棉棒末端样式,basefmt=基线样式)
title="默认设置绘制棉棒图"
ax1.set_title(title)
ax1.set_xticks(np.linspace(1,10,10))
#设置三种参数棉棒图
ax2.stem(x,y,linefmt="-.",markerfmt="*",basefmt="C3-.")#linefmt=棉棒的样式，markerfmt=棉棒末端样式,basefmt=基线样式,C3表示颜色序号)
title="设置三种参数棉棒图"
ax2.set_title(title)
ax2.set_xticks(np.linspace(1,10,10))
#基线位置数据设置图
ax3.stem(x,y,linefmt="b-.",markerfmt="d",basefmt="C3-.",bottom=0.5)
title="基线位置数据设置图"
ax3.set_title(title)
ax3.set_xticks(np.linspace(1,10,10))
#添加网格图例棉棒图
ax4.stem(x,y,linefmt="b-.",markerfmt="d",basefmt="C3-.",label="网格图")
title="添加网格图例棉棒图"
ax4.set_title(title)
ax4.legend()
ax4.grid(True,color="m",lw=2,ls=":")
ax4.set_xticks(np.linspace(1,10,10))
#plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.tight_layout()#和上面adjust语句功能相同
plt.show()