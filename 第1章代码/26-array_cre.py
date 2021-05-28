# 创建数组各种方法26-array_cre.py
import numpy as np
print("任意维度的零数组:\n", np.zeros((2, 3)))
print("任意维度元素为1的数组:\n", np.ones((2, 2)))  # 注意数组的大小需用元组表示
print("任意值的对角数组阵:\n", np.diag([1, 2, 3]))  # [1,2,3]可以换成其他数据
print(np.diag(np.arange(8, 24, 8), k=1))
print(np.diag(np.arange(8, 24, 8), k=-1))
print("任意增量序列整数一维数组:\n", np.arange(1, 11, 2))
print("任意数目的一维等差数组\n", np.linspace(1, 11, 6))
# （元素是10^x，x∈[0,2]的等间隔4个数，如指定base=2，则元素是2^x）
print("任意数目的一维等比数组\n", np.logspace(0, 2, 4, base=2))
# 创建网格数组，用于立体图绘制
x = np.arange(1, 4)
y = np.arange(4, 7)
X, Y = np.meshgrid(x, y)
print("X,Y:\n", X, "\n", Y)
# 创建方阵数组（行数和列数相等，对角线元素为1，其余为0）
print("np.identity(3):\n", np.identity(3))
# 创建相同属性数组shape和dtype一致
A = np.array([[1, 2, 3], [4, 5, 6]])
print("np.ones_like(A)\n", np.ones_like(A))
print("np.zeros_like(A)\n", np.zeros_like(A))
print("np.empty_like(A)\n", np.empty_like(A))
print("np.full_like(A,3)\n", np.full_like(A, 3))
print("np.eye(3):\n", np.eye(3))
print("np.eye(3,k=1):\n", np.eye(3, k=1))
print("np.eye(3,k=-1):\n", np.eye(3, k=-1))
# 数组索引
A2 = np.arange(1, 26).reshape(5, 5)
print("A2[3,4]:", A2[3, 4])  # 第4行第5列元素
print("A2[0,0]:", A2[0, 0])  # 第1行第1列元素
print("A2[-1,-1]:", A2[-1, -1])  # 第5行第5列元素
print("A2[-2,-3]:", A2[-2, -3])  # 倒数第2行倒数第3列元素
# 一维数组切片
A1 = np.array([1, 2, 3, 4, 5, 6])
print("A1[1:3]:", A1[1:3])
print("A1[::2]:", A1[::2])
print("A1[:]:", A1[:])
print("A1[:4]:", A1[:4])
print("A1[2:]:", A1[2:])
print("A1[1::2]:", A1[1::2])
print("A1[5:0:-2]:", A1[5:0:-2])
print("A1[5:0:-1]:", A1[5:0:-1])
# 二维数组切片
print("A2[:,:]:\n", A2[:, :])
print("A2[1:4,3:]:\n", A2[1:4, 3:])
print("A2[:4:2,:4:2]:\n", A2[:4:2, :4:2])
print("A2[4:0:-2,1:4:2]:\n", A2[4:0:-2, 1:4:2])  # 行从第5行到第1行间隔-2，列中第2列到第4列，间隔2
print("A2[::2,::2]:\n", A2[::2, ::2])
print("A2[:3,:3]:\n", A2[:3, :3])
print("A2[3:,3:]:\n", A2[3:, 3:])
