# 11-newtow_itera  牛顿迭代法求解非线性方程组
from sympy import *
import sympy
import numpy as np
import math

x1 = symbols("x1")
x2 = symbols("x2")
f1 = 8.0 - x1**2 - 0.5 * x2**2.0
f2 = 4.0 - sympy.exp(x1) - 2 * x2  # x
t10 = 1.0
t20 = -2
t0 = np.array([[t10], [t20]])


def jacobi(t1, t2):  # 构建雅各比矩阵
    dF11 = diff(f1, x1)
    dF11 = dF11.subs([(x1, t1), (x2, t2)])
    dF12 = diff(f1, x2)  ##表达式
    dF12 = dF12.subs([(x1, t1), (x2, t2)])  ##具体数值
    dF21 = diff(f2, x1)
    dF21 = dF21.subs([(x1, t1), (x2, t2)])
    dF22 = diff(f2, x2)
    dF22 = dF22.subs([(x1, t1), (x2, t2)])
    return np.array([[dF11, dF12], [dF21, dF22]])


def F00(t1, t2):  # 构建迭代起点
    ff1 = f1.subs([(x1, t10), (x2, t20)])
    ff2 = f2.subs([(x1, t10), (x2, t20)])
    F0 = np.mat([[ff1], [ff2]])
    return F0


flag = True
eps = 0.0000000001
k = 0
while flag == True:
    k = k + 1
    F0 = F00(t10, t20)
    F0 = F0.astype(np.float64)
    ja = jacobi(t10, t20).astype(np.float64)
    ja = np.linalg.inv(ja)
    x = -ja * F0 + t0
    if max(abs(x - t0)) <= eps:
        flag = False
    t0[:] = x[:]  # 注意不能用t0=x互换
    # print("x0=",x0)
    t10 = t0[0, 0]
    t20 = t0[1, 0]
    if k == 201:
        flag = False
print(f"k={k}\nx={x.T}\nF={F0.T}")
