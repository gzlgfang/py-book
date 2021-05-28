# 数组调整27-arrar_reshape.py
import numpy as np
ar1 = np.arange(1, 25)
# 调整形状
print("np.reshape(ar1,(3,8)):\n", np.reshape(ar1, (3, 8)))
print("ar1.reshape((3,8)):\n", ar1.reshape((3, 8)))
print("ar1.reshape((2,12)):\n", ar1.reshape((2, 12)))
# 折叠为一维数组
ar2 = ar1.reshape((2, 12))
print("ar2:", ar2)
print("ar2_11:", np.ndarray.flatten(ar2))  # 默认order='C',行为主序
print("ar2_12:", ar2.flatten(order='F'))  # 列为主序
print("ar2_13:", ar2.ravel(order='F'))  # 创建视图优先
print("ar2_14:", np.ndarray.ravel(ar2))
# 数组转置
arT = np.array([[1, 2, 3], [4, 7, 9]])
print("arT1:", arT.T)
print("arT2:", np.ndarray.transpose(arT))
ar1 = np.array([1, 2, 3])
print("ar1.T:", ar1.T)  # 一维数组无转置效果
ar1_2 = np.array([[1, 2, 3]])
print("ar1_2.T:", ar1_2.T)
ar1_22 = np.array([1, 2, 3], ndmin=2)
print("ar1_22.T:", ar1_22.T)
# 水平堆叠
arHr = np.array([1, 2, 3, 4])  # 单行数组
arHc = np.array([[1], [2], [3], [4]])  # 单列数组
print("np.hstack([arHr,arHr,arHr]):\n", np.hstack((arHr, arHr, arHr)))
print("np.hstack([arHc,arHc,arHc]):\n", np.hstack((arHc, arHc, arHc)))
# 垂直堆叠
arV1 = np.array([1, 2, 3, 4])  # 单行数组
arV2 = np.array([['a', 'b'], ['c', 'd']])  # 二维数组
print("np.vstack((arV1,arV1,arV1)):\n", np.vstack((arV1, arV1, arV1)))
print("np.vstack((arV2,arV2,arV2)):\n", np.vstack((arV2, arV2, arV2)))
# 深度堆叠
arD1 = np.array([1, 2, 3, 4])  # 一维数组
arD2 = np.array([5, 6, 7, 8])  # 一维数组
print("np.dstack((arD1,arD2)):\n", np.dstack((arD1, arD2)))
print("arD.shape", np.dstack((arD1, arD2)).shape)
arD1 = np.array([[1, 2], [3, 4]])  # 二维数组
arD2 = np.array([[5, 6], [7, 8]])  # 二维数组
print("np.dstack((arD1,arD2)):\n", np.dstack((arD1, arD2)))
print("arD.shape", np.dstack((arD1, arD2)).shape)
# 添加元素
ar_app1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  # 元组也可以转换为数组
print("无轴添加结果:\n", np.append(ar_app1, [[10, 12, 14, 16], [21, 22, 23, 24]]))
print("轴0添加结果:\n", np.append(
    ar_app1, [[10, 12, 14, 16], [21, 22, 23, 24]], axis=0))
print("轴1添加结果:\n", np.append(
    ar_app1, [[10, 12, 14, 16], [21, 22, 23, 24]], axis=1))
# ⑧插入元素
ar_ins = np.array([[1, 2, 3], [5, 6, 7]])
print("np.insert(ar_ins,(1,2),13):\n", np.insert(
    ar_ins, [1, 2], 13))  # 在原数组位置1,2前面插入13
print("np.insert(ar_ins,1,[12,13,14],axis=0):\n",
      np.insert(ar_ins, 1, [12, 13, 14], axis=0))
b2 = np.arange(1, 13).reshape((4, 3))  # 创建4行3列数组
print("np.insert(b2,[2],[21,22,23])\n", np.insert(b2, [2], [21, 22, 23]))
print("np.insert(b2,2,[21,22,23],axis=0)\n",
      np.insert(b2, 2, [21, 22, 23], axis=0))
print("np.insert(b2,[2],[21,22,23],axis=1)\n",
      np.insert(b2, [2], [21, 22, 23], axis=1))
print("np.insert(b2,2,[21,22,23,24],axis=1)\n",
      np.insert(b2, 2, [21, 22, 23, 24], axis=1))
print("np.insert(b2,[2],[21,22,23,24],axis=1)\n",
      np.insert(b2, [2], [21, 22, 23, 24], axis=1))
# 删除元素delete
arr_Del = np.arange(1, 16).reshape(3, 5)
print("np.delete(arr_Del,[3,4]):", np.delete(
    arr_Del, [3, 4]))  # 一维折叠后删除序号3,4的元素
print("np.delete(arr_Del,1,0):\n", np.delete(arr_Del, 1, 0))  # 沿0轴删除序号1的元素
print("np.delete(arr_Del,[2,3],1):\n", np.delete(
    arr_Del, [2, 3], 1))  # 沿1轴删除序号2,3的元素
print("np.delete(arr_Del,np.s_[::2],1):\n", np.delete(
    arr_Del, np.s_[::2], 1))  # 沿1轴删除序号0,2,4的元素
# ⑨删除元素#⑩删除长度为1的维度squeeze
ar_squ = np.arange(1, 7).reshape((1, 6))
ar_d1 = np.squeeze(ar_squ)
print("ar_squ.shape,ar_d1.shape:", ar_squ.shape, ",", ar_d1.shape)
# ⑪增加长度为1的维度:newaxis
arr = np.array([1, 2, 3])
arr1_3_1 = arr.reshape(1, 3, 1)
arr3_1 = arr[:, np.newaxis]
arr1_3 = arr[np.newaxis, :]
arr3_12 = np.expand_dims(arr, axis=1)
arr1_32 = np.expand_dims(arr, axis=0)
print("arr1_3_1.shape,arr3_1.shape,arr1_3.shape,arr3_12.shape,arr1_32.shape:\n",
      arr1_3_1.shape, ",", arr3_1.shape, ",", arr1_3.shape, ",", arr3_12.shape, ",", arr1_32.shape)
# ⑫数组大小调整resize
a_resize = np.arange(1, 9)
print("np.resize(a_resize,(3,3)):\n", np.resize(a_resize, (3, 3)))
print("np.resize(a_resize,(2,2)):\n", np.resize(a_resize, (2, 2)))
