# 16-dict.py有关字典的创建、运算、函数及方法
dict1 = {'张三': 89, '李四': 92, '王五': 93}
dict2 = dict([('化学', 6), ('物理', 3), ('数学', 8)])
print('dict2=', dict2)
dict3 = dict(广州='花城', 佛山='禅城', 深圳='鹏程')
print('dict3=', dict3)
dict4 = dict(zip(['广州', '佛山', '深圳', '宁波', '上海'],
                 ['花城', '禅城', '鹏程', '甬城', '申城']))
print('dict4=', dict4)
# 访问字典某个键对应的值
print('dict2中键名为化学对应的值=', dict2['化学'])  # 注意用中括号[]
# 列出字典中全部键名
print('列出dict4中全部键名=', dict4.keys())  # 返回的是列表的形式
# 列出字典中全部值
print('列出dict4中全部值=', dict4.values())  # 返回的是列表的形式
# 计算字典的键/值对数
print('字典dict1的键/值对数=', len(dict1))  # 返回的是int
# 向字典中添加键/值对及更新值
dict2['语文'] = 12  # 添加语文/12的键/值对
dict2['数学'] = 10  # 更新数学的学分
print('更新和添加后的字典dict2=', dict2)
# 删除某键/值对或整个字典
del dict1['张三']  # 删除dict1中键是'张山'的键/值对
dict2.clear()   # 清空字典所有键/值对，但保留字典名，可访问和添加
del dict3      # 删除字典,不再保留空字典，无法访问和添加
print('删除张山条目后的dict1=', dict1)  # 返回字典
print('清空所有条目后的字典dict2=', dict2)  # 返回空字典
d1 = {'a': 4 + 2j, 'b': [1, 3], 'c': {'a': 1}}  # 字典中的值可以任意数据类型
d2 = {'key': 1, 'key': 2, 'key': 3}  # 重复键名,只记住最后一个key=1
d3 = {'key1': 100, 'key2 ': 100, 'key3': 100}  # 键值可以重复
str1 = str(d3)  # 将字典整体转换为字符串以便打印
dict5 = dict4.copy()  # 返回一个字典dict4的浅复制
print('复制字典dict4=', dict5)
# 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值,val可以为空
print('一个初值创建字典=', dict.fromkeys(
    ['a', 'b', 'c', 'd', 'e', 'f'], 6))  # 如没有输入6，则默认为None
print('get广州返回值=', dict5.get('广州'))  # 返回指定键的值，如果值不在字典中返回default值
print('字典中键名重庆存在判断=', dict5.__contains__('重庆'))  # 如果键在字典dict里返回true，否则返回false
print('字典中键名宁波存在判断=', dict5.__contains__('宁波'))  # 如果键在字典dict里返回true，否则返回false
li_tu = dict5.items()  # items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回
print('items()方法返回：', li_tu)  # 返回元祖列表
print('字典d3中key1的值=', d3.setdefault('key1'))  # 返回字典中指定键名的值；，如键不存在于字典中；
d3.setdefault('key5')  # 如键不存在于字典中，则无返回值，但会将新的键名添加到字典中，键并将值设为None
print('添加key5键名后的字典d3:', d3)
d2 = {'d': 4, 'f': '泰山'}
print('将字典d2添加到字典d1中:', d1.update(d2), ',', d1)  # 把字典d2对添加到d1里，无返回值，只修改d1
print('pop方法上海返回值=', dict5.pop('上海'))  # 删除字典中键名上海所所对应的条目，并返回值键名所对应的值
print('popitem方法返回并删除的条目:', dict5.popitem())  # 返回并删除字典中的最后一对键和值。
tup1 = (4, 6, 8, 10)
tr = tup1.__add__((5, 6))
print(tr)
