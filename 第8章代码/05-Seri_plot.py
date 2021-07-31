#Series plot 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as mticker
import pandas as pd
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小

data=[74,85.5,94.5,79,72,86,93.5,85.5,95,75,97.5,87	,73,94.5,60,54.5,74,88,	71,89,75]
ds=pd.Series(data) # 列表创建Series
ds.name="CAD score"
ds.index=["张三","李四","方一","郭二","何三","何四","黎五","李六","吕二","马三","莫二","彪三","庞一","欣三","松二","周三","耿四","董三","文二","龙三","马尔"]
dxt=["张三","李四","方一","郭二","何三","何四","黎五","李六","吕二","马三","莫二","彪三","庞一","欣三","松二","周三","耿四","董三","文二","龙三","马尔"]
fig, ax = plt.subplots(figsize=(9, 9))##绘制直方图
ds.plot(kind="hist",bins=range(50,101,10),rwidth=0.5,align="left",edgecolor='r',label="课程成绩分布图")
plt.xlabel("CAD成绩")
plt.ylabel("学生人数")
ax.set_xticklabels(['','50-60','60-70','70-80','80-90','90-100'])
plt.ylim(0,9)
plt.legend()

fig, ax = plt.subplots(figsize=(9, 9))#绘制线条图
ds.plot(kind="line",label="score",lw=2,color="blue")
plt.ylabel("CAD成绩")
plt.xlabel("学生姓名",labelpad=5)
ax.set_xticks(np.arange(0,21))
ax.set_yticks(np.arange(50,101,2))
ax.set_xticklabels(dxt)
plt.legend()
plt.grid()

plt.figure()#绘制饼图
ds.name=""
ds.plot(kind="pie",startangle=45,shadow=True,autopct="%3.1f%%")
plt.title("CAD成绩各人百分占比图",fontsize=28)

plt.show()
