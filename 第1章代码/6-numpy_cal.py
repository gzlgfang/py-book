# numpy库计算36-numpy_cal.py
import numpy as np
# 多项式参数拟合
x = [1, 2, 3, 4, 5, 6]
y = [5, 9, 12, 19, 26, 36]
fitcoeff = np.polyfit(x, y, 3)
print("fitcoeff=", fitcoeff)
# 一维多项式处理
print("poly1d:\n", np.poly1d(fitcoeff))
p = np.poly1d([1, 2, 3, -18])
root3 = p.r  # 求多项式的根
print("root3:", root3)
# 线性方程组求解
A = np.mat('1 ,2, 3;3 ,-5 ,2;5 ,-7, 9')
b = np.array([9, 7, 12])
X = np.linalg.solve(A, b)
print('X=', X)
