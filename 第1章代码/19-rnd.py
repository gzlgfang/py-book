#随机函数应用举例#
import random as rnd
import numpy as np
for i in range(3):
    print("random():%.5f" % rnd.random())
for i in range(3):
    rnd.seed(3)
    print("random():%.5f" % rnd.random())
rnd.seed(None)  # 消除种子
# rnd.seed(6)
# 随机整数
for i in range(3):
    print("randint():", rnd.randint(1, 100))
for i in range(3):
    print("randrange():", rnd.randrange(1, 20, 3))
# 随机浮点数
for i in range(3):
    print("uniform(1,10):", rnd.uniform(1, 10))
# 序列seq中随机取出一个元素
print("rnd.choice([2,6,7,9,12]):", rnd.choice([2, 6, 7, 9, 12]))
print("rnd.choice('scutgzws'):", rnd.choice('scutgzws'))
print("rnd.choice((52,63,73,92,12)):", rnd.choice((52, 63, 73, 92, 12)))
# 把列表 items 中的元素随机打乱
#li = [5, 6, 9, 12, 33]
li=np.arange(0,10)
print('rnd.shuffle(li):', rnd.shuffle(li))
print('li=', li)
# 从列表 items 中随机取出 n 个元素，但不改变原列表。
#li = [5, 6, 9, 12, 33]
print('rnd.sample(li,5):', rnd.sample(li, 2))
print('li=', li)
