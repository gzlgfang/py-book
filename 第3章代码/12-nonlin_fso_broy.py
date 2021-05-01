#12-nonlin_fso_broy.py  布罗依登法求解非线性方程组
from scipy import optimize
import math
#f1=6*x-cos(x)-sin(y);
#f2=8*y-sin(x)-cos(y);

def fun(x):
    return[ 8.0-x[0]**2-0.5*x[1]**2.0 , 
    4.0-math.exp(x[0])-2*x[1]] 
sol = optimize.broyden1(fun, [0.8, -1.8])
print("sol_broyden1=",sol.T)
print(fun(sol))

sol = optimize.broyden2(fun, [-1.8, 0.8])
print("sol_broyden2=",sol.T)
print(fun(sol))

sol = optimize.fsolve(fun, [-1.8, 0.8])
print("sol_fsolve=",sol.T)
print(fun(sol)) 