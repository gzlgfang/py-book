#13-nonlin_fso_broy.py  布罗依登法求解非线性方程组
from scipy import optimize
import math
#f1=6*x-cos(x)-sin(y);
#f2=8*y-sin(x)-cos(y);

def fun(x):
    return[2.0*x[0]-0.5*math.sin(x[1]*x[2])-0.8 ,math.exp(x[0])-56*(x[1]+0.2)+math.cos(x[2])+1.22,
           0.7* x[0]**2+0.6*x[1]+x[2]-62]

def func(x):
    return[(x[0]**0.8+x[0]*x[1]**0.7+x[2]**0.8-1)**2,(x[0]**1.2*x[1]+x[1]**0.9+x[0]**0.5*x[2]-1)**2,(x[0]+x[1]**0.4*x[2]**0.5+x[2]**1.2-1)**2]
    

sol = optimize.broyden1(fun, [0.1, 0.1,0.1])
print("sol_broyden1=",sol.T)
print(fun(sol))

sol = optimize.broyden2(fun, [0.1, 0.1,-0.1])
print("sol_broyden2=",sol.T)
print(fun(sol))

sol = optimize.fsolve(fun, [0.8, 0.8,-0.5])
print("sol_fsolve=",sol.T)
print(fun(sol)) 

#第二个方程组求解
print("第二个方程组求解")
sol = optimize.broyden1(func, [0.3, 0.6,0.3])
print("sol_broyden1=",sol.T)
print(func(sol))

sol = optimize.broyden2(func, [0.3, 0.1,0.1])
print("sol_broyden2=",sol.T)
print(func(sol))

sol = optimize.fsolve(func, [0.1, 0.5,0.3])
print("sol_fsolve=",sol.T)
print(func(sol)) 


