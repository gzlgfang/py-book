#09-barh.py条形图绘制
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
x=['有机','无机','物化','电工','金工','建工']
y1=[86,93,78,90,92,85]
y2=[87,92,81,91,86,89]
plt.barh(x,y1,color="r",label="A班",hatch="////",edgecolor="b")
plt.barh(x,y2,tick_label=x,alpha=0.5,label="B班",left=y1,hatch="//",edgecolor="b")
plt.legend()
plt.xlabel("实验成功率（%）", size=18)       
plt.ylabel("实验名称", size=18)     
plt.show()

