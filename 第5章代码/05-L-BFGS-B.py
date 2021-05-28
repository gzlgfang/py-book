#05-L-BFGS-B.py
from scipy import optimize
import scipy as scp
import numpy as np
import time
#自定义优化函数
def fun(t):
    return 225*np.log(14-0.1*t)/(130-t)+480/(t-30)
start_time = time.time()
res=optimize.minimize(fun,[60],method='L-BFGS-B',bounds=[(32,138)])
optim=res.x
minf=fun(optim)
print(f't={optim[0]:.5f},minf={minf[0]:.5f}')
end_time = time.time()
print("程序运行计时", end_time - start_time)
