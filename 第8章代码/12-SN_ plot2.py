#seaborn plot2
from datetime import date
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib as mpl
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

tips = sn.load_dataset("tips")
DF=pd.read_excel('g:\income.xls','Sheet1', na_filter=False,index_col=0)

figure,ax=plt.subplots(1,2,figsize=(16,16))
ax1=sn.barplot(x="sex", y="total_bill", data=tips,ax=ax[0],capsize=0.5)
ax[0].set_title="具有误差帽的sex一级分层统计"
ax2=sn.barplot(x="sex", y="total_bill", hue="smoker",data=tips,ax=ax[1])
ax[1].set_title="sex-hue二级分层统计"




g = sn.catplot(x="sex", y="total_bill", hue="smoker", col="time",data=tips, kind="bar", height=4, aspect=.7)
plt.figure()
f=sn.boxplot(x="sex", y="total_bill", hue="smoker",data=tips)
plt.figure()
f=sn.violinplot(x="sex", y="total_bill", hue="smoker",data=tips)

plt.figure()

sn.stripplot(y = 'age', x ='sex',data=DF)
plt.title="stripplot"
plt.figure()
sn.violinplot(y = 'income', x = 'Education',  data=DF)

plt.figure()
sn.violinplot(x = 'income', y = 'Education',  data=DF)

plt.figure()
sn.violinplot(y = 'income', hue = 'Education',x='province',  data=DF)


plt.figure()
sn.barplot(y ='income', x = 'age',data=DF)

plt.figure()
sn.barplot(y = 'income', x ='Education',data=DF)

plt.figure()
sn.boxplot(y = 'income', x = 'Education',data=DF)

plt.figure()
sn.boxplot(y ='income', x = 'sex',data=DF)

plt.figure()
sn.histplot(data=DF['income'],bins=10)

plt.figure()
sn.kdeplot(x='age' ,y='income',data=DF)

plt.figure()
print("stop=","T")
sn.countplot(x=DF["province"],data=DF)
plt.figure()
sn.swarmplot(y = 'income', x = 'Education',data=DF)
plt.figure()
sn.swarmplot(y ='income', x = 'sex',data=DF)

plt.figure()
sn.swarmplot(y = 'height', x = 'sex',data=DF)

plt.figure()

cy_color= ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']# '#bcbd22', '#17becf']
DF.groupby('province').mean()['income'].plot(kind='bar',color=cy_color,edgecolor='k',lw=2)



sn.pairplot(data=DF)#配对图


plt.figure()
#flights = sn.load_dataset("flights")
#print(flights.head(6))
#flights = flights.pivot("month", "year", "passengers")
#print(flights.head(6))
#ax=sn.heatmap(flights)
D2_data=np.random.rand(24, 12)
ax = sn.heatmap(D2_data,vmin=0,vmax=1,cmap="YlGnBu",annot = True,  yticklabels=np.arange(1,25,1),xticklabels=np.arange(1,13,1))


plt.show()