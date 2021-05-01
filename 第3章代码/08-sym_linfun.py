#08-sym_linfun
import sympy as syp
import numpy as np
A=syp.Matrix([[5.0,1,1],[15,9.0,3],[2,2,7.0]])
b=syp.Matrix([12,42,13])#注意和numpy库中mat表达的不同
 # 线性方程求解 Ax=b 
x=A.solve(b)
print("固定3×3方程组求解")
for i in range(len(x)):
    print(f"x{i+1}={x[i,0]:.5f}")

#随机10×10方程组
print("随机10×10方程组求解")
a=10*np.random.rand(10,10)#产生系数
A=syp.Matrix(a)
b=syp.Matrix(20*np.random.rand(10))
x=A.solve(b)
for i in range(len(x)):
        print(f"x{i+1}={x[i,0]:.5f}")
##随机3×4欠定方程组求解
print("随机3×4欠定方程组求解")
x_syb=syp.symbols("x_1,x_2,x_3,x_4")#"_"表示下标，构建变量符号
a=10*np.random.rand(3,4)#产生系数
A=syp.Matrix(a)
b=syp.Matrix(20*np.random.rand(3))
x=syp.Matrix(x_syb)
x=syp.solve(A*x-b,x_syb)
print(x)

