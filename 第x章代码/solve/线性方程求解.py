import numpy as np

b = np.array([[5], [6], [7]])  # 线性方程右边常数项
a = np.array([[1, 2, 2], [3, 2, 1], [4, 1, 2]])  # 方程系数
bb = np.mat(b)  # 转为矩阵
aa = np.mat(a)  # 转为矩阵
c = aa.I     # 求逆运算
x = c*bb     # 结果计算
x = np.array(x)
for i in range(3):
    print("x(", i, ")=%10.7f" % x[i, 0])
print()
print("以上是线性方程解")
