#DateFrame stats
import numpy as np
import pandas as pd
dict = {"GDP":[12390,10890,1900,8901,7821,6532],"Population":[103,98,160,102,98,89],"Incre_rate":[1.4,2.1,-1.5,3.2,3.1,0.8]}
df1=pd.DataFrame(dict) #字典数据创建DF 
df1.index=['A城', 'B城', 'C城', 'D城', 'E城','F城']
print(df1)
print(df1.sort_values("Population"))
print(df1.describe())
print("df1.loc['A城']:\n",df1.loc['A城'])

list1=[[138,129,148,88,97,78],[111,126,123,785,83,59],[99,133,127,79,91,83]]
df2=pd.DataFrame(list1)#列表数据创建DF
print(df2)
df3=pd.DataFrame(np.random.rand(8,6))#numpy数组创建DF
print(df3)

DF3=pd.read_excel('g:\city_gdp.xls','Sheet1', na_filter=False,index_col=0)
print(DF3)
print(DF3.info())
print(DF3.mean())
print(DF3.province.value_counts())

DF_city_top8=DF3.province.value_counts().head(8)
print("DF_city_top8:\n",DF_city_top8)


print("DF3.head(6):\n",DF3.head(6))
print("DF3.tail(6):\n",DF3.tail(6))

print("DF3.set_index('province').sort_values('GDP'):\n",DF3.set_index('province').sort_values('GDP'))
#print("DF3.loc['浙江']:\n",DF3.loc['宁波'])
DF4=DF3.set_index('province')

print("DF4.loc['浙江']:\n",DF4.loc['浙江'])

print(DF4.sum(level='province').sort_values("GDP",ascending=False))

print(DF4.mean(level='province').sort_values("GDP",ascending=False))

print(DF4.drop('number',axis=1).groupby('province').sum().sort_values('GDP',ascending=False))



DF_gk=pd.DataFrame(np.random.rand(10,6))#创建归一化六科成绩
DF_gk.index=["郭二","何三","黎五","李六","吕二","马三","莫二","彪三","庞一","欣三"]#添加行索引——姓名
DF_gk.columns=['数学','语文','英语','化学','物理','生物']#添加列索引——课程
print("        10人高考归一化成绩单\n",DF_gk)
print("DF_gk.sum():\n",DF_gk.sum())#统计10人每科的总分
print("DF_gk.mean():\n",DF_gk.mean())#统计10人每科的平均分
print("DF_gk.describe():\n",DF_gk.describe())#10人成绩的一些基本统计信息

print("DF_gk.sum(axis=1):\n",DF_gk.sum(axis=1))#统计每人六科的总分
print("DF_gk.mean(axis=1):\n",DF_gk.mean(axis=1))#统计每人六科的平均分
print("DF_gk.var(axis=1):\n",DF_gk.var(axis=1))#统计每人六科成绩分方差