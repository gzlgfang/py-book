#02-wuxing
from typing import Type
import numpy as np
import pandas as pd
DF=pd.read_excel('xuexi.xlsx','Sheet1', na_filter=False,index_col=0)
a1 = DF['TB']
a2 = DF['TC']
a3 = DF['PC']
y = DF['HV']

#print(a1,a2,a3,y)
print(type(a1))
aa=np.array(y)
print(aa[:])
print(len(aa))#
print(type(aa))
