##seaborn plot1
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
mpl.rcParams["font.size"] = 16#设置字体大小
tips = sn.load_dataset("tips")
DF=pd.read_excel('g:\income.xls','Sheet1', na_filter=False,index_col=0)
#绘制条形图baaplot
figure,ax=plt.subplots(2,2,figsize=(16,16),num="barplot四种不同调用格式")
#ax1:具有误差帽的性别分层统计
ax1=sn.barplot(x="sex", y="total_bill", data=tips,ax=ax[0,0],capsize=0.5)
#ax2:sex-smoker二级分层统计
ax2=sn.barplot(x="sex", y="total_bill", hue="smoker",data=tips,ax=ax[0,1])
#ax3:按学历分层统计收入
ax3=sn.barplot(y = 'income', x ='Education',data=DF,ax=ax[1,0])
#ax4:按省分层统计收入_置信度为65%
ax4=sn.barplot(y = 'income', x ='province',data=DF,ax=ax[1,1],ci=65)



#绘制箱型图
figure,ax=plt.subplots(2,2,figsize=(16,16),num="boxplot四种不同调用格式")
flp1={'marker': 'o', 'markersize':16,'markerfacecolor' : 'red','color' : 'black'}
ax1=sn.boxplot(x="sex", y="total_bill", data=tips,ax=ax[0,0])
ax2=sn.boxplot(x="sex", y="total_bill", hue="smoker",data=tips,ax=ax[0,1])
ax3=sn.boxplot(y = 'income', x ='Education',data=DF,ax=ax[1,0],flierprops=flp1)
ax4=sn.boxplot(y = 'income', x ='province',data=DF,ax=ax[1,1])

#绘制小提琴图与箱型图比较图

#figure,ax=plt.subplots(2,2,figsize=(16,16),num="violinplot不同调用格式")
#sn.boxplot(x="sex", y="total_bill", hue="smoker",data=tips,ax=ax[0,0])
#sn.violinplot(x="sex", y="total_bill", hue="smoker",data=tips,ax=ax[0,1])
#sn.boxplot(y = 'income', x ='Education',data=DF,ax=ax[1,0])
#sn.violinplot(y = 'income', x ='Education',data=DF,ax=ax[1,1])

#绘制内部不同图形的小提琴图，该段代码需单独运行，否则坐标标注会出现混乱

figure,ax=plt.subplots(2,2,figsize=(16,16),num="violinplot不同调用格式")
sn.violinplot(y = 'income', x ='Education',data=DF,inner="box",ax=ax[0,0])#内部显示箱型
sn.violinplot(y = 'income', x ='Education',data=DF,inner="quartile",ax=ax[0,1])#内部显示四分位数线（右上）
sn.violinplot(y = 'income', x ='Education',data=DF,ax=ax[1,0],inner="point")#内部显示具体数据点
sn.violinplot(y = 'income', x ='Education',data=DF,ax=ax[1,1],inner='stick')#图内显示具体数据棒（右下）
#数据分布图
plt.figure()
figure,ax=plt.subplots(1,3,figsize=(36,6))
sn.distplot(x =DF['age'],ax=ax[0],bins=10,color="m" )#按年龄分布
sn.distplot(x =DF['income'],ax=ax[1], bins=10,color='b')#按收入分布
ax = sn.distplot(x=DF['height'], rug=True, rug_kws={"color": "g"},kde_kws={"color": "k", "lw": 3, "label": "KDE"},hist_kws={"histtype": "step", "linewidth": 3, "alpha": 1, "color": "g"},ax=ax[2])


#直方图数据分布
#stat : {"count", "frequency", "density", "probability"}
        #ggregate statistic to compute in each bin.
        
        #- ``count`` shows the number of observations
        #- ``frequency`` shows the number of observations divided by the bin width
        #- ``density`` normalizes counts so that the area of the histogram is 1
        #- ``probability`` normalizes counts so that the sum of the bar heights is 1

plt.figure()
figure,ax=plt.subplots(2,2,figsize=(24,12))
hist1=sn.histplot(y = 'income', x ='age',data=DF,bins=10,color="m", edgecolor='b',ax=ax[0,0])#
sn.histplot(data=DF['income'],color="pink",hatch="//", edgecolor='b',bins=10,ax=ax[0,1])
sn.histplot(data=DF['income'],color="red",hatch="/", edgecolor='b',bins=10,ax=ax[1,0],stat='frequency')
sn.histplot(data=DF['income'],color="red",hatch="'///'", edgecolor='k',bins=10,ax=ax[1,1],stat='probability')

sn.pairplot(data=DF)#配对图

plt.figure()
figure,ax=plt.subplots(3,2,figsize=(12,8))
#绘制带状图
sn.stripplot(y="total_bill", x ='sex',data=tips,ax=ax[0,0])
sn.stripplot(y="total_bill", x ='sex',hue='time',data=tips,ax=ax[0,1])#分层带状图
sn.countplot(x=DF["province"],data=DF,ax=ax[1,0])#个数统计
sn.swarmplot(y ='income', x = 'sex',data=DF,ax=ax[1,1])#群图
sn.kdeplot(x='age' ,y='income',data=DF,ax=ax[2,0])#kde图
D2_data=np.random.rand(12, 12)
sn.heatmap(D2_data,vmin=0,vmax=1,cmap="YlGnBu",  yticklabels=np.arange(1,13,1),xticklabels=np.arange(1,13,1),ax=ax[2,1])
plt.subplots_adjust(wspace=0.2,hspace=0.3)
#catplot
sn.catplot(x="sex", y="total_bill", hue="smoker", col="time",data=tips, kind="bar", height=4, aspect=.7)

#plt.figure()
#sn.stripplot(x = 'Education', y ='income',data=DF)

plt.show()