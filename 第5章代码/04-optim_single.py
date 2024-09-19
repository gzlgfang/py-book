# 04-optim_single库优化方法求解  Multiple
# （1）golden
# （2）fmin
# （3）minimize
# 0.21*x**4-2*x**3+5.5*x**2-6*x+5

from scipy import optimize
import scipy as scp
import numpy as np
import time

# 自定义优化函数
def func(x):
    return 0.21 * x**4 - 2 * x**3 + 5.5 * x**2 - 6 * x + 5


def funJ(x):  ##fitness
    a, b, c, d, e = 1, 3, 5, 7, 2
    f = (
        (x**2 + a**2) ** 0.5
        + ((x + b) ** 2 + c**2) ** 0.5
        + ((x + d) ** 2 + e**2) ** 0.5
    )
    return f


# 黄金分割法
minf = optimize.golden(func, brack=(1, 5), full_output=True)  # full_output=True
print("golden_output=", minf[:])

# fmin设置
minf = optimize.fmin(funJ, x0=5)
print("fmin_output_funJ:")
optim = minf[0]
minf = funJ(optim)
print(f"x={optim:.5f},minf={minf:.5f}")
# fmin全输出设置
minf = optimize.fmin(func, x0=5, full_output=True, retall=True)
print("fmin_output:\n", minf)


# 默认设置minimize_scalar
minf = optimize.minimize_scalar(func)
print("mini_scalar_output:")
optim = minf.x
minf = func(optim)
print(f"x={optim:.5f},minf={minf:.5f}")
# minimize函数优化
res = optimize.minimize(func, [4], method="CG")
optim = res.x
minf = func(optim)
print(f"minimize_output:\nx={optim[0]:.5f},minf={minf[0]:.5f}")
print(f"res=\n{res}")
print("res.fun=", res.fun)
