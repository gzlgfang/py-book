#14-SLSQP.py
from scipy import optimize
import scipy as scp
import numpy as np
fun = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2+(x[2]-2*x[1])**2
cons1= ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
         {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
         {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] +x[2]+1},
         {'type': 'eq', 'fun': lambda x:x[0]-1.5/1.7*x[1]})

bnds = ((0, None), (0, None),(0, None))
res1 =optimize.minimize(fun, (2, 0,1), method='SLSQP', bounds=bnds,
                constraints=cons1)
print(res1)
def cons(x):
    constr1=x[0] - 2 * x[1] + 2
    constr2=-x[0] - 2 * x[1] + 6
    constr3=-x[0] + 2 * x[1] + 2
    return [constr1,constr2,constr3]
def eq_cons(x):
    return x[0]-1.5/1.7*x[1]
res2=optimize.fmin_slsqp(fun,(2,0,1),f_eqcons=eq_cons,f_ieqcons=cons,bounds=bnds)
print(res2)#