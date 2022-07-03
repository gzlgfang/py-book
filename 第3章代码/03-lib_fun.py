#03-lib_fun
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt
from scipy.optimize import fsolve,bisect,newton,brentq,brenth
import  sympy  as syp
import scipy as scp
f1 = lambda x: 3-x *np.sin(x) #超越方程
def f2(x):
    return x ** 3 - 7.7 * x ** 2 + 19.2 * x - 15.3 #多项式方程
def f3(x):
    return  x**0.5-1.74+2*np.log10(0.1+18.7*x**0.5/5000) #摩擦系数方程
x = syp.symbols('x')
syp_sol0=syp.solve(3*syp.cos(x)+7.0 *syp.sin(x)-4,x)#可解析求解的超越方程
#syp_sol0=syp.solve(x**7+x**8+x**9,x)#可解析
#print("x^99=",syp_sol0[1]**99)
syp_sol2=syp.solve(x ** 3 - 7.7 * x ** 2 + 19.2 * x - 15.3,x)
print(f"syp_sol0={syp_sol0},syp_sol2={syp_sol2}")
sol1=[]
for i in np.arange(6,30,3):
      k=fsolve(f1,i)
      sol1.append(list(k)[0])
print(f"fsolve_sol1={sol1}")
print(f"f3_bisect={1/bisect(f3,0,20):.5f}")
print(f"f3_newton={1/newton(f3,1):.5f}")
print(f"f3_brentq={1/brentq(f3,0,20):.5f}")
print(f"f3_brenth={1/brenth(f3,0,20):.5f}") 
#print(fsolve(f2,[1,4]))
print(f"f2_bisect={bisect(f2,0,4):.5f}")
print(f"f2_newton={newton(f2,1):.5f}")
print(f"f2_brentq={brentq(f2,0,4):.5f}")
print(f"f2_brenth={brenth(f2,0,4):.5f}")
