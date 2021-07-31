#creat Series data
import pandas as pd
import numpy as np

data=[74,85.5,94.5,79,72,86,93.5,85.5,95,75,97.5,87	,73,94.5,60,54.5,74,88,	71,89,75]
ds=pd.Series(data) # 列表创建Series
print(ds)
ds.name="CAD score"
print(ds)
ds.index=["张三","李四","方一","郭二","何三","何四","黎五","李六","吕二","马三","莫二","彪三","庞一","欣三","松二","周三","耿四","董三","文二","龙三","马尔"]
print(ds)
print(ds.mean())
print(ds.describe())
print(ds.argmin())#    统计最小值的索引位置
print(ds.argmax())#    统计最大值的索引位置
print(ds[15])
print(ds.index[15])


dict1 = dict(zip(['广州', '佛山', '深圳', '宁波', '上海'],
                 ['花城', '禅城', '鹏程', '甬城', '申城']))
print(pd.Series(dict1))#字典创建Series

d_list=[1,2,3,4,5,6]
print(pd.Series(d_list))

d_tu=(11,12,13,14,15,16)
print(pd.Series(d_tu))#元组创建Series

d_array=np.arange(10)
print(pd.Series(d_array))#数组创建Series

#张三2021高考成绩
ds=pd.Series([138,129,148,88,97,78])
ds.index=['数学','语文','英语','化学','物理','生物']
ds.name="张三2021高考成绩"
print("张三2021高考成绩单：")
print(ds)
print("总成绩=",ds.sum())