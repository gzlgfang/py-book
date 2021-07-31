#creat DataFrame
import pandas as pd
import numpy as np
dict = {"GDP":[12390,10890,1900,8901,7821,6532],"Population":[103,98,160,102,98,89],"Incre_rate":[1.4,2.1,-1.5,3.2,3.1,0.8]}
df1=pd.DataFrame(dict) #字典数据创建DF 
print(df1)
print(df1.columns)
#['A城', 'B城', 'C城', 'D城', 'E城','F城']
list1=[[138,129,148,88,97,78],[111,126,123,785,83,59],[99,133,127,79,91,83]]
df2=pd.DataFrame(list1)#列表数据创建DF
print(df2)
df3=pd.DataFrame(np.random.rand(8,6))#numpy数组创建DF
print(df3)
print(pd.read_excel('g:\city_gdp.xls','Sheet1', na_filter=False,index_col=0))