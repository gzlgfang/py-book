#06-Series connection heat exchanger.py 串联换热器优化
from scipy import optimize
import scipy as scp
import numpy as np
import time
#自定义优化函数
def fun(x):
    T1,T2=x[0],x[1]
    return 10000*((T1-100)/(3600-12*T1)+(T2-T1)/(3200-8*T2)+(500-T2)/400)
start_time = time.time()
res=optimize.minimize(fun,[150,350],method='L-BFGS-B',bounds=[(101,299),(151,399)])
optim=res.x
minf=fun(optim)
print(f'T1={optim[0]:.5f},T2={optim[1]:.5f},minf={minf:.5f}')
end_time = time.time()
print("程序运行计时", end_time - start_time)