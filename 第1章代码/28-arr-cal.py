# 数组运算28-arr-cal.py
# 算术运算
import numpy as np

a_cal1 = np.arange(1, 13).reshape(3, 4)  # 3行4列数组
a_cal2 = np.arange(1, 5)  # 1行4列数组
a_cal3 = np.arange(1, 4).reshape(3, 1)  # 3行1列数组
a_cal4 = np.arange(10, 22).reshape(3, 4)  # 3行4列数组
a_div = a_cal1 / a_cal3
a_add = a_cal1 + a_cal2
a_mul = a_cal1 * a_cal3
a_minus = a_cal1 - a_cal2
a1 = np.arange(1, 5).reshape(2, 2)
a2 = np.arange(1, 5).reshape(2, 2)
a_pow = a1**a2  # 指数运算
a_int = a_cal4 // a_cal1  # 整除
print("a_add:\n", a_add)
print("a_minus:\n", a_minus)
print("a_mul:\n", a_mul)
print("a_div:\n", a_div)
print("a_pow:\n", a_pow)
print("a_int:\n", a_int)
# 单个元素函数运算
a_fun = np.array([[1, 2, 3], [4, 5, 6]])
print("np.sin(a_fun):\n", np.sin(a_fun))
print("np.arcsin(0.1*a_fun):\n", np.arcsin(0.1 * a_fun))  # 元素不能大于1
print("np.sinh(a_fun):\n", np.sinh(a_fun))  # 双曲
print("np.arcsinh(a_fun):\n", np.arcsinh(a_fun))  # 反双曲
print("np.sqrt(a_fun):\n", np.sqrt(a_fun))
print("np.exp(a_fun):\n", np.exp(a_fun))
print("np.log10(a_fun):\n", np.log10(a_fun))
print("np.log2(a_fun):\n", np.log2(a_fun))
# 聚合运算
a_aggre = np.arange(1, 28).reshape(3, 3, 3)
print("a_aggre=", a_aggre)


print("a_aggre.mean(axis=0):\n", a_aggre.mean(axis=0))  # 计算元素平均值
print("a_aggre.std(axis=0):\n", a_aggre.std(axis=0))  # 计算标准差
print("a_aggre.var(axis=None):\n", a_aggre.var(axis=None))  # 计算方差
print("a_aggre.sum(axis=(0,1):\n", a_aggre.sum(axis=(0, 1)))  # 计算元素和
print("a_aggre.prod(axis=0):\n", a_aggre.prod(axis=0))  # 计算元素乘积
print("a_aggre.cumsum():\n", a_aggre.cumsum())  # 计算所有元素的逐个累积和
print("a_aggre.cumprod(axis=0):\n", a_aggre.cumprod(axis=0))  # 计算所有元素的逐个累积乘
print("a_aggre.max(axis=(0,1):\n", a_aggre.max(axis=(0, 1)))  # 计算数组中元素的最大值
print("a_aggre.min(axis=(1,2)):\n", a_aggre.min(axis=(1, 2)))  # 最小值
print("a_aggre.argmax(axis=0):\n", a_aggre.argmax(axis=0))  # 计算数组中元素的最大值的索引
print("a_aggre.argmin(axis=0):\n", a_aggre.argmin(axis=0))  # 和最小值索引
print("a_aggre.all():\n", a_aggre.all())  # 所有元素不为零判断
print("a_aggre.any():\n", a_aggre.any())  # 任何一个元素不为零判断。
# 矩阵及向量运算
a34 = np.arange(1, 13).reshape(3, 4)
a4 = np.arange(1, 5)
a41 = np.arange(1, 5).reshape(4, 1)
a43 = np.arange(1, 13).reshape(4, 3)
a_dot1 = np.dot(a34, a43)
print("a_dot1:\n", a_dot1)
a_dot2 = np.dot(a34, a4)
print("a_dot2:\n", a_dot2)
a_dot3 = np.dot(a34, a41)
print("a_dot3:\n", a_dot3)
a_dot4 = np.dot(a43, a34)
print("a_dot4:\n", a_dot4)
a_in1 = np.inner(a4, a4)
print("a_in1:\n", a_in1)
a_in2 = np.inner(a34, a34)
print("a_in2:\n", a_in2)
a_out1 = np.outer(a4, a4)
print("a_out1:\n", a_out1)
a_out2 = np.outer(a34, a34)
print("a_out2:\n", a_out2)
a_cro1 = np.cross([1, 2, 4], [4, 5, 6])
print("a_cro1:\n", a_cro1)
a_cro2 = np.cross(a43, a43 + 2)
print("a_cro2:\n", a_cro2)
print("a000,a010,a020=", a_aggre[0, 0, 0], a_aggre[0, 1, 0], a_aggre[0, 2, 0])
print("a001,a011,a021=", a_aggre[0, 0, 1], a_aggre[0, 1, 1], a_aggre[0, 2, 1])
print("a002,a012,a022=", a_aggre[0, 0, 2], a_aggre[0, 1, 2], a_aggre[0, 2, 2])
# 逻辑运算

print("a100,a110,a120=", a_aggre[1, 0, 0], a_aggre[1, 1, 0], a_aggre[1, 2, 0])
print("a101,a111,a121=", a_aggre[1, 0, 1], a_aggre[1, 1, 1], a_aggre[1, 2, 1])
print("a102,a112,a122=", a_aggre[1, 0, 2], a_aggre[1, 1, 2], a_aggre[1, 2, 2])

print("a200,a210,a220=", a_aggre[2, 0, 0], a_aggre[2, 1, 0], a_aggre[2, 2, 0])
print("a201,a211,a221=", a_aggre[2, 0, 1], a_aggre[2, 1, 1], a_aggre[2, 2, 1])
print("a202,a212,a222=", a_aggre[2, 0, 2], a_aggre[2, 1, 2], a_aggre[2, 2, 2])
