# 09-linprogramming 线性规划
import numpy as np
from scipy.optimize import linprog

# 例5-6
c = [-7, -12, 0, 0, 0]
A_eq = [[3, 10, 1, 0, 0], [4, 5, 0, 1, 0], [9, 4, 0, 0, 1]]
b_eq = [30, 20, 36]
r = linprog(c, A_eq=A_eq, b_eq=b_eq, method="simplex")
print(r)
# 例5-7
c = [-1, 1]
A_ub = [[-2, 1], [1, -3], [1, 1]]
b_ub = [2, 2, 4]
bounds = ((0, None), (None, None))
r = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print("全部求解结果：\n", r)
print(f"x={r.x},J={r.fun:.5f}")

c = [-6, -5, -4, -3, -2, -1]
A_eq = [[8, 10, 1, 1, 2, 3], [4, 5, 2, 1, 3, 1], [9, 4, 2, 1, 1, 2]]
b_eq = [30, 20, 36]
A_ub = [[7, 4, 5, 1, 1, 6], [3, 8, 6, 2, 1, 2], [2, 5, 6, 2, 1, 8]]
b_ub = [40, 30, 60]
method = "interior-point"
r = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, method=method)
print("r-ip=:\n", r)

method = "simplex"
r = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, method=method)
print("r-simplex=:\n", r)
