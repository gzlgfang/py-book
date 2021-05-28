#13-slsqp_fmin
from scipy import optimize
import scipy as scp
import numpy as np

#定义目标函数
fun = lambda x:  4*x[0]**2 +2*x[0]*x[2]+x[1]**2+x[2]**2
#用于minimize调用的约束条件
cons1= ({'type': 'eq', 'fun': lambda x:  x[0]**2+ x[1] +x[2]-36},
         {'type': 'eq', 'fun': lambda x: 2*x[1]**2+ x[2]**2-48},
         {'type': 'ineq', 'fun': lambda x: 48-5*x[0] -3* x[1]-6*x[2]},
         {'type': 'ineq', 'fun': lambda x: -18+3*x[0] + 2 * x[2]})
bnds = ((0, None), (0, None),(0, None))
res1 =optimize.minimize(fun, x0=(1, 0,0), method='SLSQP', bounds=bnds,constraints=cons1)
print(res1)
#用于f_min_slsqp调用的约束条件
def cons(x):
    constr1=-18+3*x[0] + 2 * x[2]
    constr2=48-5*x[0] -3* x[1]-6*x[2]
    return [constr1,constr2]
def eq_cons(x):
    coneq1=x[0]**2+ x[1] +x[2]-36
    coneq2=2*x[1]**2+ x[2]**2-48
    return [coneq1,coneq2]
res2=optimize.fmin_slsqp(fun,x0=(2,2,2),f_eqcons=eq_cons,f_ieqcons=cons,bounds=bnds)
print(res2)