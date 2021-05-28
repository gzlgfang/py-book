from numpy import *
from numpy.linalg import *  # 次库函数全部调入
from numpy.linalg import solve  # 次库函数只调入solve
import numpy.linalg as lg  # 次库缩写成lg整体调入
a = mat([[1, 2], [3, 5]])  # 主库函数直接调用
b1 = mat([[4], [11]])
b2 = mat([[4, 8], [11, 15]])
aa = a.I
x1 = aa * b1
x2 = linalg.solve(a, b2)  # 主库-次库-函数调用
x3 = solve(a, b2)  # 次库函数直接调用
x4 = lg.solve(a, b2)  # 次库缩写-函数调用
print("X1=", mean(x1[0]), mean(x1[1]))
print("X2=", x2)
print("X3=", x3)
print("X4=", x4)
