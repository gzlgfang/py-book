# 24-def.py自定义函数编写
import math


def do_calm(x1, x2, x3=12, *args, **kwargs):
    return 2 * x1 + x2 + x3


M = do_calm(1, 18)
print("M=", M)
# 无参数自定义函数


def do_print_welicome():
    print("华南理工大学与中国邮政广东分公司欢迎您")


do_print_welicome()
# 单参数自定义函数计算


def do_calsum(x):
    sum = 0
    for i in range(x):
        sum = sum + (i + 1)**2
    return sum


print(do_calsum(10))
# 双参数自定义函数计算圆柱体体积和外表面积


def do_calvolum(r, h):
    v = math.pi * r**2 * h
    s = 2 * math.pi * r**2 + 2 * math.pi * r * h
    return v, s  # 以元组形式返回


vs = do_calvolum(1, 10)
print(do_calvolum(1, 10))
print(type(vs))  # 以元组形式返回
# 单值参数不确定


def find_add3(*args):
    sum3 = 0
    for i in args:
        sum3 = sum3 + i**3
    return sum3


print(find_add3(28, 45, 17, 67))
# 寻找素数


def find_PriNum(*args):
    prime = 0
    for i in args:
        Para = True
        m = int(math.sqrt(i) + 1)
        for j in range(2, m):
            if i % j == 0:
                Para = False
                break
        if Para == True:
            prime = i
            break
    return prime


print("找到的第一个素数是：", find_PriNum(28, 45, 17, 67, 53))
# 键值对参数不确定，打印成绩单


def print_score(*args, **kwds):
    print("华南理工大学化学与化工学院2021年学生成绩单")
    print(*args)  # 单值不确定参数
    dict1 = dict(kwds)  # 键值对转化为字典
    for k in dict1.keys():  # 取字典键名
        print(k, end='  ')
    print()  # 起到换行作用
    for v in dict1.values():  # 取字典值
        print("{:>4d}".format(v), end='       ')  # 4位右对齐
    print()


print_score('化工21班', '王正', '男', '广东', '2021123456', 分析化学=93, 物理化学=95, 化工原理=96)
