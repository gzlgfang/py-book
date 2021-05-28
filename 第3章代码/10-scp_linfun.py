#10-scp_linfun
import numpy as np
from scipy import linalg 
A=np.mat([[5.0,1,1],[15,9.0,3],[2,2,7.0]])
b=np.mat([[12],[42],[13]])
 # 线性方程求解 Ax=b 
x=linalg.solve(A,b)
print("固定3×3方程组求解")
for i in range(len(x)):
    print(f"x{i+1}={x[i,0]:.5f}")
#随机10×10方程组
print("随机10×10方程组求解")
a=10*np.random.rand(10,10)#产生系数
A=np.mat(a)
b=np.mat(20*np.random.rand(10)).reshape(10,1)
x=linalg.solve(A,b)
for i in range(len(x)):
        print(f"x{i+1}={x[i,0]:.5f}")