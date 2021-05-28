#12-polyvarfit
from scipy import optimize as op
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt

def func(x, a0,  a1, a2):
        return a0+a1*x[0]+a2*x[1]
x=np.array([[1,2,3,4],[5,7,8,9]])
y_data=func(x, 2, 1,1)
y_real=y_data
print(y_real)#+np.random.random(5)

#最小二乘拟合
def J(alfai):
    return y_real-func(x,*alfai)
alf0=[1,1,2]
alf_opt,alf_cov=op.leastsq(J,alf0)
print('alf=',alf_opt)
print(alf_cov)
print(op.leastsq(J,alf0))
