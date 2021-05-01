#13-nonlin_fso_broy.py  布罗依登法求解非线性方程组
from scipy import optimize
import math
#f1=6*x-cos(x)-sin(y);
#f2=8*y-sin(x)-cos(y);

def fun(x):
    return[2.0*x[0]-0.5*math.sin(x[1]*x[2])-0.8 ,math.exp(x[0])-56*(x[1]+0.2)+math.cos(x[2])+1.22,
           0.7* x[0]**2+0.6*x[1]+x[2]-62]
sol = optimize.broyden1(fun, [0.1, 0.1,-0.1])
print("sol_broyden1=",sol.T)
print(fun(sol))

sol = optimize.broyden2(fun, [1.8, 0.8,0.1])
print("sol_broyden2=",sol.T)
print(fun(sol))

sol = optimize.fsolve(fun, [0.8, 0.8,-0.5])
print("sol_fsolve=",sol.T)
print(fun(sol)) 