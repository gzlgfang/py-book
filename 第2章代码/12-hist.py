#12-hist.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=18


plt.figure(dpi=120)
#绘制直方图
x=np.random.randint(0,100,1000)#随机产生100个0-100之间的整数
bins=10#数据统计的间隔及范围
plt.hist(x,bins=bins,histtype="bar",rwidth=1,color="m",hatch="/",alpha=0.6, edgecolor='b')
title="绘制randint直方图"
plt.title(title)
plt.xticks(np.arange(0,101,10))
plt.xlim(0,100)

plt.figure(dpi=120)
x=np.random.randn(1000)#随机产生1000正态分布数
bins=20
plt.hist(x,bins=bins,histtype="bar",rwidth=1,color="b",hatch="///",alpha=0.6, edgecolor='r')
title="绘制randn直方图"
plt.title(title)





plt.show()