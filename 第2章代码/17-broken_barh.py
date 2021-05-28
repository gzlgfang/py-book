#17-broken_barh.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=18
plt.figure(num="scatter_draw",figsize=(16,8))
ax1=plt.subplot(121)
ax2=plt.subplot(122)
#默认设置绘制
xranges=[(30,50),(100,60),(180,30),(220,80)]
yranges=(10,8)
ax1.broken_barh(xranges,yranges)
title="默认设置绘制"
ax1.set_title(title)
#多种参数设置绘制图
xranges1=[(30,50),(100,60),(180,30),(220,80)]
yranges1=(10,18)
ax2.broken_barh(xranges1,yranges1,facecolors=('gray', 'blue','pink','m'))
ax2.broken_barh(xranges1,(35,12),facecolors=('gray', 'green','pink','m'),hatch='x' )
ax2.broken_barh(xranges1,(53,10),facecolors=('gray', 'green','pink','m'),hatch='*', edgecolors="b")
xranges2=[(20,30),(70,50),(150,30),(200,90)]
ax2.broken_barh(xranges2,(70,8),facecolors=( 'blue','pink','m','yellow'),hatch='//', edgecolors="r",lw=2,ls=":")
title="多种参数设置绘制图"
ax2.set_title(title)
plt.subplots_adjust(wspace=0.2,hspace=0.3)
#plt.tight_layout()#和上面adjust语句功能相同
plt.show()