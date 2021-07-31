# data_range index 时间序列数据
import numpy as np
from numpy.core.fromnumeric import mean, var
from numpy.lib.function_base import median
import pandas as pd
import datetime as dt



import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as mticker

#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小





time_id1=pd.date_range("2021-2-1 00:00",periods=8)
print(time_id1)
print(pd.Series(np.random.rand(8)*5+5,index=time_id1))

time_id2=pd.date_range("2021-2-1 00:00","2021-5-6 23:00",freq="H")
print(time_id2)
print(pd.Series(np.random.rand(len(time_id2))*10+20,index=time_id2).head(10))

time_id3=[dt.datetime(2021,1,1),dt.datetime(2022,1,1)]
print(pd.DataFrame(np.random.rand(2,3)*5+6,index=time_id3,columns=['温度','湿度','风速']))

time_id4=[]
for i in range(20):
    Tindex=dt.datetime(2000+i,1,1)
    time_id4.append(Tindex)
#print(pd.DataFrame(np.random.rand(20,3),index=time_id4,columns=['温度','湿度','风速']))
time_DF=pd.DataFrame(np.random.rand(20,3),index=time_id4,columns=['温度','湿度','风速'])
time_DF.温度=time_DF.温度*10+25
time_DF.湿度=time_DF.湿度*50+50
time_DF.风速=time_DF.风速*5+3
#print(time_DF.温度)
#print(type(time_DF.values))
#TDV=time_DF.values[0,1]
#print(TDV)
print(time_DF)

#某地2022年温度,湿度,风速数据按时记录，输出按天、日、月平均值
time_id2022=pd.date_range("2022-1-1 00:00","2022-12-31 23:00",freq="H")
weather_DF=pd.DataFrame(np.random.rand(len(time_id2022),3),index=time_id2022,columns=['温度','湿度','风速'])
weather_DF.温度=weather_DF.温度*30+5
weather_DF.湿度=weather_DF.湿度*65+35
weather_DF.风速=weather_DF.风速*15+0.5
print(weather_DF.head(100))
print(weather_DF.resample('D').mean())
print(weather_DF.resample('7D').mean())
print(weather_DF.resample('M').mean())
print(weather_DF.resample('15D').mean())
print(weather_DF.resample('8D').mean())#按8天采样平均数据
print(weather_DF.resample('D').std())
print(weather_DF.resample('W').std())
print(weather_DF.resample('M').median())
print(weather_DF.resample('15D').sum())
fig,ax=plt.subplots(figsize=(18, 9))
weather_DF.resample('M').mean().plot(ax=ax,kind='bar',lw=2)
ax.set_xticklabels(['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'])
plt.legend()
plt.grid()
plt.show()


WD=pd.DataFrame({"time":time_id2022,'温度':np.random.rand(len(time_id2022)),'湿度':np.random.rand(len(time_id2022)),'风速':np.random.rand(len(time_id2022))})
#print(WD)
WD.温度=WD.温度*18+7
WD.湿度=WD.湿度*35+65
WD.风速=WD.风速*10+2
DF_M=WD #.reset_index()
DF_M['month']=DF_M.time.apply(lambda x:x.month)
print(DF_M.head(6))
#print(DF_M.drop('index',axis=1).groupby("month").aggregate(np.median))

print(DF_M.groupby("month").aggregate(np.mean))
print(DF_M.groupby("month").aggregate(np.sum))
print(DF_M.groupby("month").aggregate(np.std))
print(DF_M.groupby("month").aggregate(np.var))

DF_M['day']=DF_M.time.apply(lambda x:x.day)
print(DF_M.head(36))

DF_M['week']=DF_M.time.apply(lambda x:x.week)
print(DF_M.head(236))

