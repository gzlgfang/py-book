# 数组属性25—array_cal.py
import numpy as np
ar1 = np.array([[1, 2], [3, 4], [5, 6]])  # 二维数组
ar2 = np.array([[[12.3, 16.8], [3, 4], [7, 0]], [
               [7, 1], [2, 5], [1, 2 + 3j]]])  # 三维数组
print("数组维度ndim1:", ar1.ndim)
print("数组维度ndim2:", ar2.ndim)
print("数组尺寸shape1:", ar1.shape)
print("数组尺寸shape2:", ar2.shape)
print("数组元素总数size1:", ar1.size)
print("数组元素总数size2:", ar2.size)
print("数组元素类型dtype1:", ar1.dtype)
print("数组元素类型dtype2:", ar2.dtype)
print("元素的字节大小itemsize1:", ar1.itemsize)
print("元素的字节大小itemsize2:", ar2.itemsize)
print("无非零元素判断1:", ar1.all())
print("无非零元素判断2:", ar2.all())
print("元素最大值1:", ar1.max())
print("元素最大值2:", ar2.max())
print("元素最小值1:", ar1.min())
print("元素最小值2:", ar2.min())  # 数组中有一个元素为复数时，其他实数都按复数处理
print("元素平均值1:", ar1.mean())
print("元素平均值2:", ar2.mean())
print("数组转置1:", ar1.T)
print("数组转置2:", ar2.T)
