# 15_set.py#有关集合的创建、运算、方法和函数实例
set1 = set('gzhnlgdx05')  # 用set()创建集合
set2 = set('gzzsdx06')
set3 = {'g', 'z', 'd', 'x'}  # 直接用大括号{}创建集合
print('set1,set2,set3=', set1, ',', set2, ',', set3)
print('两个集合的并集=', set1 | set2)
print('两个集合的差集=', set1 - set2)  # 从集合set1中删除集合set2中相同的元素,创建新的集合
print('两个集合的补集=', set1 ^ set2)  # 不会修改原集合，包括集合set1和set2中的非相同元素
print('两个集合的交集=', set1 & set2)  # 不会修改原集合，集合set1和set2中的相同元素
set1.add('华工')  # 添加元素，无返回值，修改原集合
print('添加元素后的集合set1=', set1)
set2.clear()  # 移除集合set2中的所有元素,仅从内存清空集合，但内存地址不删除
print('set2=', set2)
set2 = set('gzzsdx06')  # 重新复制set2,以便后面操作
print('co_set=', set1.copy())  # 将set1拷贝co_set
# 返回set1与set2和set3的差集,但不改变原set1集合
print('差集方法11=', set1.difference(set2, set3))
print('差集方法12=', set1.difference('h', '空集'))  # 可删除单个元素，也可以是原集合中没有的元素不会出错
set2.difference_update(set3)  # 在set2中移除集合set3中的元素，无返回值，会修改原set2集合
print('差集方法2=', set2)
set2 = set('gzzsdx06')  # 重新复制set2,以便后面操作
set1.discard('n')  # 删除集合set1中的元素n,也可以是集合，无返回值，直接修改原集合set1
print('删除元素或集合=', set1)
print('交集方法1=', set1.intersection(set3))  # 返回集合set1和集合set2的交集，不会修改原集合
print('set1=', set1)
print('交集方法2=', set1.intersection_update(set3))  # 无返回值，直接修改set1为两者集合的交集
print('交集方法2.set1=', set1)  # 只有交集部分赋给set1
set1 = set('gzhnlgdx05')  # 恢复集合set1的原赋值，以便后续运算
# 判断两个集合是否含有相同的元素，如果没有相同元素返回 True，否则返回 False。
print('无相同元素判断=', {1, 2}.isdisjoint({3, 4}))
print(set3.issubset(set1))  # 判断set3集合是否为set1集合的子集。
print(set3, set1)
print(set1.issuperset(set3))  # 判断该方法的参数集合set3是否为指定集合set1的子集
set1.pop()  # 集合set1中随机移除1个元素，无返回值，但会修改set1
print('set1=', set1)  # 随机移除元素后的集合
set1.remove('g')  # 移除指定元素,无返回值，但会修改set1
print('set1=', set1)  # 移除指定元素后的集合
print('返回两集合不重复元素=', set2.symmetric_difference(set3))  # 返回两个集合中不重复的元素集合,不修改原集合
s1 = {1, 2, 3, 5}
s2 = {7, 8, 3, 5}
s1.symmetric_difference_update(s2)  # 移除s1集合中s2集合中相同的元素，并将s2集合中不同的元素插入到当前集合s1中。
print('s1=', s1)  # 前一语句没有返回值，直接改变集合set1是元素。
print(set1.union(set2))  # 将set2插入到当前集合set1中,构建一个新的集合，相当于集合并操作。
s3, s4 = {5, 6, 7}, {8, 9, 10}
s3.update(s4)  # 将集合或可迭代数据添加到指定集合中，无返回值，直接修改指定集合s3
print('s3=', s3)
s3.update('abcd')  # 给集合添加元素，无返回值，修改原集合,可迭代数据会自动拆分
print('s3=', s3)
