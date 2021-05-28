# 利用矩阵函数mat求解线性方程组30—linefun.py
import numpy as np
flag = 1
while (flag):
    n = eval(input("请输入线性方程组变量数="))
    A, b = np.zeros((n, n)), np.zeros(n).reshape(n, 1)
    for i in range(n):
        temp = input(f'请以逗号间隔依次输入第{i+1}条方程的系数和常数')
        temp = temp.split(',')
        b[i][0] = eval(temp[n])
        for j in range(n):
            A[i][j] = eval(temp[j])
    A, b = np.mat(A), np.mat(b)
# 数据输入和转化完毕
    x = A.I * b  # 线性方程求解
# 输出数据打印
    for i in range(n):
        print("x(", i + 1, ")=", "{:.5f}".format(x[i, 0]))
    flag = input('是否需要继续计算其他方程组，是输入1，否回车')
