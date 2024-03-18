##各种迭代计算
from sympy import *
import sympy
import numpy as np
import math

k, x0, eer0 = 0, 10, 1e-6
flag = True
## equation: xe^x=1
## method: direct itera
while flag:
    x = 1 / np.exp(x0)
    # x = np.exp((500 - 1.68 * np.exp(0.02 * x0) * x0**0.3) / 100)
    # print(x)
    eer = abs(x - x0)
    if eer <= eer0:
        flag = False
    x0 = x
    k = k + 1
print("直接法迭代次数=", k)
print("x={:.8f}".format(x))

##method relax itera
k, x0, eer0, omiga1, omiga2 = 0, 10, 1e-6, 0.5, 0.9
flag = True
while flag:
    # x = x0 + omiga1 * (1 / np.exp(x0) - x0)
    x = x0 + omiga2 * (np.exp((500 - 1.68 * np.exp(0.02 * x0) * x0**0.3) / 100) - x0)
    print(x)
    eer = abs((x - x0) / x0)
    if eer <= eer0:
        flag = False
    x0 = x
    k = k + 1
print("松弛法迭代次数=", k)
print("x={:.8f}".format(x))
