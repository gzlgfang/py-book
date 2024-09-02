#01-Exhaustive method 
import scipy as scp
import numpy as np
import time
#自定义优化函数
def func(t):
    return 225*np.log(14-0.1*t)/(130-t)+480/(t-30)
start_time = time.time()
t1,t2=32,128
f=np.ones(101)
for k in range(3):#进行3轮穷举
    t=np.linspace(t1,t2,101)
    for i in range(101):#每轮穷举100等分
       f[i]=func(t[i])
    fmin=min(f[:])#确定最小值
    index=list(f[:]).index(min(f[:]))#确定最小值所在的位置
    t1=t[index-1]#重新设置t1
    t2=t[index+1]
optim=t[index]
minf=func(t[index])
print(f't={optim:.8f},minf={minf:.8f}')
end_time = time.time()
print("程序运行计时", end_time - start_time)