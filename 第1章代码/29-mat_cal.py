# 29-mat_cal.py矩阵运算
import numpy as np
arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(10, 13)
arr3 = np.arange(20, 23).reshape(3, 1)
M_arr1 = np.mat(arr1)
M_arr2 = np.mat(arr2)
M_arr3 = np.mat(arr3)
print("M_arr1+arr1:\n", M_arr1 + arr1)
print("M_arr1+M_arr2:\n", M_arr1 + M_arr2)
print("M_arr1-M_arr3:\n", M_arr1 - M_arr3)
print("M_arr1/M_arr2:\n", M_arr1 / M_arr2)
print("arr1*arr2:\n", arr1 * arr2)
print("M_arr1*arr3:\n", M_arr1 * arr3)
