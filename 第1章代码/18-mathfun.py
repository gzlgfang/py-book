#数学函数应用例子#
from math import *
import numpy as np
print("sin(pi/4)=%.4f" % sin(pi / 4))  # 保留三位小数点
print("cos(pi/3)=%.4f" % cos(pi / 3))  # 保留四位小数点
# 只有numpy库中的函数可以对列表进行处理
print("sin([pi/8,pi/6,pi/3])=", np.sin([pi / 8, pi / 6, pi / 3]))
print("tan(pi/4)=%.4f" % tan(pi / 4))  # 保留四位小数点
print("atan(1)=%.4f" % atan(1))  # 保留四位小数点
print("asin(0.5)=%.4f" % asin(0.5))  # 保留四位小数点
print("acos(0)=%.4f" % acos(0))  # 保留四位小数点
print("exp(2))=", exp(2))
print("log(10)=", log(10))
print("int (99.8)=", int(99.8))
print("int (-99.2)=", int(-99.2))
print("fix(99.8)=", np.fix(99.8))
print("fix(-99.2)=", np.fix(-99.2))
print("np.sign(-8)=", np.sign(-8))
print("np.sign(0)=", np.sign(0))
print("np.sign(3)=", np.sign(3))
print("hypot(3,4)=", hypot(3, 4))
print("degrees(pi)=", degrees(pi))
print("radians(180)=", radians(180))
