#11-rank_cond_norm.py
import numpy as np
A=np.array([[1,2],[3,5]])
b=np.array([[4],[11]])
x=np.linalg.solve(A,b)
print("np_x=",x.T)
A2=np.array([[2,2.99999],[2,3.00001]])
b2=np.array([[4],[8]])
rank=np.linalg.matrix_rank(A2)#秩
cond=np.linalg.cond(A2)#条件数
norm=np.linalg.norm(A2)#范数
x2=np.linalg.solve(A2,b2)
print("np_x=",x2.T)
print(f"np_rank,cond,norm={rank:.5f},{cond:.5f},{norm:.5f}")