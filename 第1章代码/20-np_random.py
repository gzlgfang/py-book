#20-np_random.py数组随机数#
import numpy as np
# 生成[0,1)的随机array数组数据
print("np.random.rand(2,3)=\n{}".format(np.random.rand(2, 3)))
# 生成随机的以0为均值、以1为标准差的正态分布array数组数据
print("np.random.randn(2,3)=\n{}".format(np.random.randn(2, 3)))
# 产生10个大于等于1，小于10的随机整数
print("np.random.randint(1,10,size=10)={}".format(
    np.random.randint(1, 10, size=10)))
# 产生2×3随机数组，数组元素大于等于1，小于10的随机整数
print("np.random.randint(1,10,size=(2,3))=\n{}".format(
    np.random.randint(1, 10, size=(2, 3))))
print("np.random.randint(1,10)={}".format(np.random.randint(1, 10)))
print("np.random.randint(10)={}".format(np.random.randint(10)))
print("np.random.randint([7,8,10])={}".format(np.random.randint([7, 8, 10])))
# size的值必须和low及high相互匹配，下面的size只能n×3
print("np.random.randint([7,8,10],[20,30,40],size=(2,3))=\n{}".format(
    np.random.randint([7, 8, 10], [20, 30, 40], size=(2, 3))))
# 产生随机浮点数或数组
print("np.random.uniform(1,10,size=(2,3))=\n{}".format(
    np.random.uniform(1, 10, size=(2, 3))))
print("np.random.uniform(1,10)={}".format(np.random.uniform(1, 10)))
print("np.random.uniform(10)={}".format(np.random.uniform(10)))
print("np.random.uniform([7,8,10])={}".format(np.random.uniform([7, 8, 10])))
# 返回均值为loc，标准差为scale，大小为size的正态分布数组
print("np.random.normal(5,10,size=(2,3))=\n{}".format(
    np.random.normal(5, 10, size=(2, 3))))
print("np.random.normal(10,2,size=(2,3))=\n{}".format(
    np.random.normal(10, 2, size=(2, 3))))
print("np.random.normal()=", np.random.normal())
# 返回在半开区间 [0.0, 1.0) 随机的浮点数或数组，数组大小为size，默认为1
print("np.random.sample()=", np.random.sample())
print("np.random.sample((2,3))=\n{}".format(np.random.sample((2, 3))))
