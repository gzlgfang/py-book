from scipy import linalg as la
from numpy import *

a = mat([[1, 2, 4], [3, 5, 6], [12, 7, 9]])  # 输入方程系数
b = mat([[4], [11], [24]])  # 输入方程右边常数项
x1 = la.solve(a, b)
x2 = a.I*b
x1 = x1.T  # 转置
x2 = x2.T
n = len(x1[0])  # 求第1行的元素个数
for i in range(n):
    print('x1_', i+1, '=', x1[0, i])  # 第1种方法求解

for i in range(n):
    print('x2_', i+1, '=', x2[0, i])  # 第2种方法求解
