#08-optimize库优化方法求解
from scipy import optimize
import scipy as scp
import numpy as np
import time

#自定义优化函数
def fun1(t):
    return 225*np.log(14-0.1*t)/(130-t)+480/(t-30)

def fun2(x):
    return (x - 2) * x * (x + 2)**2

def fun3(x):
    return 0.21*x**4-2*x**3+5.5*x**2-6*x+5

start_time = time.time()
res1=optimize.minimize_scalar(fun2)
optim=res1.x
minf=fun2(optim)
print(f'x={optim:.5f},minf={minf:.5f}')

res2=optimize.minimize(fun1,[60],method='L-BFGS-B',bounds=[(32,128)])
optim=res2.x
minf=fun1(optim)
print(f't={optim[0]},minf={minf[0]}')
#print("res2=",res2)
minf = optimize.golden(fun2,brack=(2,5),full_output=True)
print("golden_output_fun2=",minf)

minf = optimize.golden(fun3,brack=(2,5),full_output=True)
print("golden_output_fun3=",minf)

end_time = time.time()
print("程序运行计时", end_time - start_time)

