#19-multi_stack.py
import matplotlib  as mpl
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=16
plt.figure(num="直方阶梯图")
x1= np.random.normal(60, 120, 1000)
x1=(x1-min(x1))/(max(x1)-min(x1))*150
x2= np.random.normal(70, 160, 1000)
x2=(x1-min(x1))/(max(x1)-min(x1))*150
x=[x1,x2]
bins=range(0,151,10)
labels=["甲地","乙地"]
colors=["pink","#66c2a5"]
plt.hist(x, bins=bins,color=colors,rwidth=1.2,edgecolor="black",
        histtype="stepfilled",stacked=True,label=labels)
title="甲乙两地高考数学成绩直方阶梯图"
plt.title(title)
plt.legend()
plt.xlabel("高考数学成绩")
plt.ylabel("学生人数")

plt.figure(num="直方堆积图")
x1= np.random.normal(60, 120, 1000)
x1=(x1-min(x1))/(max(x1)-min(x1))*150
x2= np.random.normal(70, 160, 1000)
x2=(x1-min(x1))/(max(x1)-min(x1))*150
x=[x1,x2]
bins=range(0,151,10)
labels=["甲地","乙地"]
colors=["pink","#66c2a5"]
plt.hist(x, bins=bins,color=colors,rwidth=1.2,edgecolor="r",
        histtype="bar",stacked=True,label=labels)
title="甲乙两地高考数学成绩堆积图"
plt.title(title)
plt.legend()
plt.xlabel("高考数学成绩")
plt.ylabel("学生人数")

plt.figure(num="条形堆积图")
x=np.arange(1,13)
y1=[3,3.6,4,4.3,5,5.6,5,4.8,7,8,8.2,9]
y2=[3.3,3.9,4.8,4.1,5,4.5,6.2,5.1,7.2,7.8,8.5,9.1]
plt.barh(x,y1,color="r",label="甲地",hatch="////",edgecolor="b")
plt.barh(x,y2,tick_label=x,alpha=0.5,label="乙地",left=y1,hatch="//",edgecolor="b")
title="甲乙两地2020年汽油消耗量万吨"
plt.title(title)
plt.legend()
plt.xlabel("汽油消耗万吨/月")
plt.ylabel("月份")
plt.show()
