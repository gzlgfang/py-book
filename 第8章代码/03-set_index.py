#set_index.py
import pandas as pd
import numpy as np

data=[74,85.5,94.5,79,72,86,93.5,85.5,95,75,97.5,87	,73,94.5,60,54.5,74,88,	71,89,75]
ds=pd.Series(data) # 列表创建Series
print(ds)
ds.name="CAD score"
ds.index=["张三","李四","方一","郭二","何三","何四","黎五","李六","吕二","马三","莫二","彪三","庞一","欣三","松二","周三","耿四","董三","文二","龙三","马尔"]
print(ds)
print('ds[["方一","郭二","何三"]]:\n',ds[["方一","郭二","何三"]])
print('ds[["马三"]]:\n',ds[["马三"]])
print('ds["马三"]=',ds["马三"])
print("ds.欣三=",ds.欣三)
print(ds.values[1:11:2])
print(ds.index[16:])
print(pd.Series([3,4,np.NaN]).count())
print(pd.Series([3,4,5]).min())
print(pd.Series([3,4,5,6]).describe())
print(pd.Series([3,4,5,6]).mean())
print(pd.Series([3,4,5,5.5,6,18,45]).median())
print(pd.Series([3,4,5,6,7]).var())
print(pd.Series([3,4,5,6,7]).std())
print(pd.Series([3,4,5,1,6,7]). argmin ())
print(pd.Series([3,4,5,1,6,7]).idxmin())