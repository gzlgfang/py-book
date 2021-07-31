#CAD_stats
import pandas as pd
import numpy as np

data=[74,85.5,94.5,79,72,86,93.5,85.5,95,75,97.5,87	,73,94.5,60,54.5,74,88,	71,89,75]
ds=pd.Series(data) # 列表创建Series
ds.name="CAD score"
ds.index=["张三","李四","方一","郭二","何三","何四","黎五","李六","吕二","马三","莫二","彪三","庞一","欣三","松二","周三","耿四","董三","文二","龙三","马尔"]
print("考试人数：",ds.count())
print("最低成绩：",ds.min())
print("平均成绩：",ds.mean())
print("中位成绩：",ds.median())
print("成绩方差：",ds.var())
print("成绩标准差：",ds.std())
print("最小成绩索引位置：",ds. argmin ())
print("最小成绩索引值：",ds.idxmin())
print("最大成绩索引位置：",ds. argmax ())
print("最大成绩索引值：",ds.idxmax())