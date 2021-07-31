#Basic Calculation
import pandas as pd
import numpy as np

ds=pd.Series([138,129,148,88,97,78])
ds.index=['数学','语文','英语','化学','物理','生物']
ds1=pd.Series([138,129,148])
ds2=pd.Series([128,109,118,67,89,92])
print("ds1+2*ds2:\n",ds1+2*ds2)
print("ds1/ds2:\n",ds1/ds2)
print("ds1-ds2:\n",ds1-ds2)
print("ds1*ds2:\n",ds1*ds2)
print("ds2**0.8:\n",ds2**0.8)
print("ds1+ds2:\n",ds1+ds2)
print("log(ds2):\n",np.log(ds2))
print("sin(ds2):\n",np.sin(ds2))
print("tan(ds2):\n",np.tan(ds2))
print("exp(0.01*ds2):\n",np.exp(0.01*ds2))



