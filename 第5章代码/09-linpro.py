#09-linprogramming 线性规划
import numpy as np
from scipy.optimize import linprog
#例5-6
c = [-7,-12,0,0,0]
A_eq =[[3,10,1,0,0],[4,5,0,1,0],[9,4,0,0,1]]
b_eq = [30,20,36]
r = linprog(c,A_eq=A_eq,b_eq=b_eq,method='simplex')
print(r)
#例5-7
c = [-1,1]
A_ub =[[-2, 1],[1,-3],[1,1]]
b_ub = [2,2,4]
r = linprog(c,A_ub=A_ub,b_ub=b_ub, bounds=( (0,None),(None,None)),method='simplex')
print(r)
print(f'x={r.x},J={r.fun:.5f}')