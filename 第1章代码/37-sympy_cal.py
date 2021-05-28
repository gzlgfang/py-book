# sympy库符号运算例子37-sympy_cal.py
from sympy.plotting import plot
from sympy.abc import x
from sympy import *
import sympy as smp
# 解方程
x, y = smp.symbols("x y")
f1 = 3.0 * x**2 + y - 28  # 用3.0是为了保证返回浮点数而不是其他类型
f2 = 2 * x + 3 * y - 12  # 变量的次数非整数时可能无法得到解
sol = smp.solve([f1, f2], [x, y])
print(sol)  # 单个解时返回字典，多个解时返回列表，列表中以元组为单位表示一组解
aa = smp.solve([x * x + y**1.2 - 3, x - 3. * y + 5], [x, y])  # 此题耗时较长
# [(-1.31086461575200, 1.22971179474933), (0.872411667038352, 1.95747055567945)]
print(aa)
# 积分
t = Symbol('t')
x = Symbol('x')
m = integrate(2 * sin(t) / (pi - t), (t, 0, x))
print(integrate(m, (x, 0, pi)))  # 返回4
# 微分
x = symbols('x')
f = log(x) - log(1 - x) + 2.2 * (1 - 2 * x) / (1 + x**2)
dify = diff(f, x)  # f对x求导
print("dify=", dify)
# 求极限
lim1 = limit(sin(x) / x, x, 0)
print("lim1=", lim1)
# 因式分解
f = x**6 + 1
ff = factor(f)
print("ff=", ff)
# 绘制函数图
plot(2 * sin(x))
# 到此为止，其他读者自己练习添加
