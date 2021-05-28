#二分法bisection method
#02-Bisection
import scipy as scp
import numpy as np
import time
#自定义优化函数
def func(t):
    return 225*np.log(14-0.1*t)/(130-t)+480/(t-30)
start_time = time.time()
t1,t2,n=32,128,0
a0,b0=t1,t2
beita=0.005
eer1=0.000001
eer2=0.000001
flag=True
while flag:
    n=n+1
    a=t1
    b=t2
    x1=(a+b)/2-beita*(b-a)
    x2=(a+b)/2+beita*(b-a)  
    f1=func(x1)
    f2=func(x2)
    if f1>=f2:
        t1=x1
        e1=(b-x1)/(a0-b0)
        optim=x2
        minf=f2
    else: 
        t2=x2
        e1=(b-x1)/(a0-b0)
        optim=x1
        minf=f1
    e2=abs(f2-f1)/(1+abs(f1))  
    if e1<=eer1 and  e2<=eer2:
        flag=False
print(f't={optim:.8f},minf={minf:.8f},n={n}')
end_time = time.time()
print("程序运行计时", end_time - start_time)





