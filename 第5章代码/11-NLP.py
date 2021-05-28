#11-Non-linear programming 非线性规划
from scipy import optimize
import scipy as scp
import numpy as np
def func(x):
    return x[0]**2-2*x[0]-4*x[1]
def cons(x):
    constr1=4-4*x[0]**2-x[1]**2+x[0]*x[1]
    constr2=x[0]
    constr3=x[1] 
    return [constr1,constr2,constr3]
sol=optimize.fmin_cobyla(func,x0=(1,1),cons=cons,rhoend=1e-7)
print(f'x={sol[0]:.5f},y={sol[1]:.5f},minJ={func(sol):.5f}')

#采用slsqp方法验证：
cons = ({'type': 'ineq', 'fun': lambda x: 4-4*x[0]**2-x[1]**2+x[0]*x[1]},
         {'type': 'ineq', 'fun': lambda x:x[0]},
         {'type': 'ineq', 'fun': lambda x: x[1]}) 
res=optimize. minimize(func, (1,1), method='SLSQP', constraints=cons).x
#print(res)
print(f'x={res[0]:.5f},y={res[1]:.5f},minJ={func(res):.5f}')


