#07-CG.py
from scipy import optimize
import scipy as scp
import numpy as np
import time
from sympy.abc import x
from sympy import *


#自定义优化函数
def fun(x):
    x1,x2,x3=x[0],x[1],x[2]
    return (x1-2)**2+(x2-3*x1-2)**2+(x3-2*x2-3)**2+x1*x2
res=optimize.minimize(fun,[6,6,6],method='CG')
optim=res.x
minf=fun(optim)
print(f'X={optim},minf={minf}')

#导数验证求解结果
x1,x2,x3 = symbols('x1,x2,x3')
expr = (x1-2)**2+(x2-3*x1-2)**2+(x3-2*x2-3)**2+x1*x2 
dify = [expr.diff(x1).subs([(x1,optim[0]), (x2, optim[1]), (x3, optim[2])]),
       expr.diff(x2).subs([(x1,optim[0]), (x2, optim[1]), (x3, optim[2])]),
       expr.diff(x3).subs([(x1,optim[0]), (x2, optim[1]), (x3, optim[2])])] # f对x求导并代入最优解
print("dify=", dify)