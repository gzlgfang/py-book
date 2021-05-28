# scipy库符号运算例子38-scipy_cal.py
from scipy.integrate import odeint  # 导入库
import matplotlib.pyplot as plt
from scipy import *
import scipy.linalg as la
from scipy import optimize
import numpy as np
# 线性方程组集合求解AX=B
A = 10 * np.random.random((3, 3))
B = 18 * np.random.random((3, 3))
X = la.solve(A, B)
print("X=", X)
# 求行列式值
print("det(A)=", la.det(A))
# 求逆阵
print("inv(A)=", la.inv(A))
# 参数拟合
xdata = [-23.7, -10, 0, 10, 20, 30, 40]
ydata = [0.101, 0.174, 0.254, 0.359, 0.495, 0.662, 0.880]


def f(x, a0, a1, a2):
    return a2 * x**2 + a1 * x + a0


guess = [2, 2, 2]
params, params_covariance = optimize.curve_fit(f, xdata, ydata, guess)
print("params=", params)
for i, x in enumerate(params):
    print(f'a{i}={x:.7f}')
# 非线性方程求解


def f(x):
    return np.log(x) - np.log(1 - x) + 2.2 * (1 - 2 * x)  # 定义方程


# 调用fsolve函数
sol_fsolve = optimize.fsolve(f, [0.1, 0.9])  # 第一个参数为我们需要求解的方程，第二个参数为方程解的估计值
print(sol_fsolve)

# 求函数最小值
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
def f(x):
    return -x**3 + 200 * (1 - x)**2 + 2.2 * (1 - 2 * x)  # 定义方程


x_min = optimize.fminbound(f, -100, 100)  # 得到指定范围([a,b])内的局部最低点
print("x_min=", x_min)
# 解微分方程组


def du(u, t):
    u1, u2 = u[0], u[1]
    du1 = 0.09 * u1 * (1 - u1 / 20) - 0.45 * u1 * u2
    du2 = 0.06 * u2 * (1 - u2 / 15) - 0.01 * u1 * u2
    return [du1, du2]


# 确定初始状态
u0 = [1.6, 1.2]
# 设定时间：从0min - 5mins
t = np.linspace(0, 10, 100)
# 解常微分方程
u = odeint(du, u0, t)
# 绘制u1关于时间的函数图像
# print(u[:,0])
plt.figure()
plt.plot(t, u[:, 0], label='u1')  # u[:,0]即返回值的第一列，是u1的值。label是为了显示legend用的。
plt.plot(t, u[:, 1], label="u2")  # u[:,1]即返回值的第二列，是u2的值
plt.legend()
ax = plt.gca()
ax.grid(True)
plt.show()
