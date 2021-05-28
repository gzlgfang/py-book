# 14-tup2.py 元组运算、函数及方法
tup1 = (1, 2, 3)
tup2 = ('s', 'c', 'u', 't')
print('元祖长度=', len(tup1))  # 计算元祖长度
print("元祖相加=", tup1 + tup2)
print("元祖重复=", 3 * tup1)
print("元祖索引=", tup1[1])
print("元祖切片=", tup2[1:3])
print("元祖逆转=", tup1[::-1])
print("求取元祖元素最大值=", max(tup1))  # 元祖中元素必须为数字
print("求取元祖元素最小值=", min(tup1))
print("求取元祖元素索引号=", tup2.index('u'))
print("求取某元祖元素出现次数=", (2, 6, 2, 7, 8).count(2))
print("元祖add相加=", tup1.__add__((5, 6)))
