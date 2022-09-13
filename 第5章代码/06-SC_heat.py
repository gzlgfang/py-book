#06-Series connection heat exchanger.py 串联换热器优化
from scipy import optimize
import scipy as scp
import numpy as np
import time
#自定义优化函数
def fun(x):
    T1,T2=x[0],x[1]
    return 10000*((T1-100)/(3600-12*T1)+(T2-T1)/(3200-8*T2)+(500-T2)/400)

def func(x):
    x,y,z=x[0],x[1],x[2]
    f=lambda x:(x**0.8+x*y**0.7+z**0.8-1)**2+(x**1.2*y+y**0.9+x**0.5*z-1)**2+(x+y**0.4*z**0.5+z**1.2-1)**2
    return f(x)  # 求最大变成求最小，前面加负号



start_time = time.time()
res=optimize.minimize(fun,[150,350],method='L-BFGS-B',bounds=[(101,299),(151,399)])
optim=res.x
minf=fun(optim)
print(f'T1={optim[0]:.5f},T2={optim[1]:.5f},minf={minf:.5f}')
end_time = time.time()
print("程序运行计时", end_time - start_time)

#另一问题求解：
print("另一问题求解:")
start_time = time.time()
res=optimize.minimize(func,[0.5,0.5,0.5],method='L-BFGS-B',bounds=[(0,1),(0,1),(0,1)])
optim=res.x
minf=func(optim)
print(f'x={optim[0]:.5f},y={optim[1]:.5f},z={optim[2]:.5f},minf={minf:.10f}')
end_time = time.time()
print("程序运行计时", end_time - start_time)





