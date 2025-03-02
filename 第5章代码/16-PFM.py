from scipy import optimize
import scipy as scp
import numpy as np

# 定义目标函数
def fun(x):
    ie1 = -18 + 3 * x[0] + 2 * x[2]
    ie2 = 48 - 5 * x[0] - 3 * x[1] - 6 * x[2]
    e1 = x[0] ** 2 + x[1] + x[2] - 36
    e2 = 2 * x[1] ** 2 + x[2] ** 2 - 48
    J1 = 4 * x[0] ** 2 + 2 * x[0] * x[2] + x[1] ** 2 + x[2] ** 2
    J2 = 10000 * (e1**2 + e2**2)
    J3 = 10000 * (min(0, ie1) ** 2 + min(0, ie2) ** 2)
    J = J1 + J2 + J3
    return J


bnds = ((0, None), (0, None), (0, None))
res1 = optimize.minimize(fun, x0=(5, 4, 0.7), bounds=bnds)
print("res1=\n", res1)
