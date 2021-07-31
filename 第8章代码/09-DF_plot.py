#DF_plot
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib as mpl
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小

DF_GDP=pd.DataFrame({"A城":1000*np.random.rand(10)+3000,"B城":1500*np.random.rand(10)+4500,"C城":4000*np.random.rand(10)+4000})
#print(DF_GDP)
DF_GDP.index=np.arange(2010,2020)
print(DF_GDP)
#plt.figure()

DF_GDP.plot(kind="line",lw=2,color=["blue","k","red"])
plt.ylabel("GDP")
plt.xlabel("年份",labelpad=5)
plt.grid()
DF_GDP.plot(kind="bar",align="center",edgecolor='k',lw=2,color=["blue","purple","pink"])
plt.ylabel("GDP")
plt.xlabel("年份",labelpad=5)
plt.legend()

plt.figure()
DF_GDP.A城.plot(kind="pie",startangle=45,shadow=True,autopct="%3.1f%%")
plt.legend(bbox_to_anchor=(0.9,0,0.3,0.8))

plt.figure()
DF_GDP.B城.plot(kind="pie",startangle=45,shadow=True,autopct="%3.1f%%")
plt.legend(bbox_to_anchor=(0.9,0,0.3,0.8))

plt.figure()
DF_GDP.C城.plot(kind="pie",startangle=45,shadow=True,autopct="%3.1f%%")
plt.legend(bbox_to_anchor=(0.9,0,0.3,0.8))

#fig, ax = plt.subplots(1,3,figsize=(18, 6))##绘制直方图
DF_GDP.plot(kind="pie",startangle=45,shadow=True,autopct="%3.1f%%",subplots=True)
plt.legend(bbox_to_anchor=(1.01,0,0.45,1))



plt.show()