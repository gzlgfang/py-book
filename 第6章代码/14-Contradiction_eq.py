#14-Contradiction equation 
import numpy as np
from numpy import linalg
A=np.mat([[1.0,1,1],[1,3.0,-1],[2,5,2.0],[3,-1,5]])
b=np.mat([[2],[-1],[12],[10]])
 # 线性方程求解 A_TAx=A_Tb 
AA=A.T*A
bb=A.T*b
x=linalg.solve(AA,bb)
print("4×3矛盾方程组求解")
for i in range(len(x)):
    print(f"x{i+1}={x[i,0]:.5f}")
eer=sum(sum(np.array((A*x-b))**2))
print(f'均方误差={eer:.5f}')