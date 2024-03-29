# 17-cal.py运算符应用实例
# 逻辑运算符and/or/not
print('逻辑与1=', False and True)
print('逻辑与2=', 0 and True)
print('逻辑与3=', 5 and 6)
print('逻辑与4=', 5 and 6 and 7)
print('逻辑与5=', bool('scut') and bool('gz'))
print('逻辑或1=', False or True)
print('逻辑或2=', 0 or True)
print('逻辑或3=', 5 or 6)
print('逻辑或4=', False or 0)
print('逻辑或5=', 0 or False)
print('逻辑非1=', not False)
print('逻辑非2=', not True)
print('逻辑非3=', not 0)
print('逻辑非4=', not 6)
print('逻辑非5=', not 'scut')
# 关系运算符(==，>，<，!=，<=，>=)
print('相等关系1=', 12 == 12)
print('相等关系2=', 12 == '12')
print('相等关系3=', 'gz' == 'GZ')
print('不相等关系1=', 12 != 12)
print('不相等关系2=', 12 != '12')
print('不相等关系3=', 'gz' != 'GZ')
print('小于关系1=', 8 < 9)
print('小于关系2=', 'g' < 'a')
print('小于关系3=', (1, 2, 3) < (7, 1, 1))  # 元祖从第一个元素开始比较 ，若相等则往下比较
print('大于关系1=', [3, 4] > [2, 8])  # 列表从第一个元素开始比较， ，若相等则往下比较
print('大于关系2=', 'ga' > 'ah')
print('大于关系3=', {3, 4, 5} > {1, 2, 12})  # 集合比较只返回False
print('小于等于关系1=', 6 <= 6)
print('小于等于关系2=', [1, 6] <= [1, 5])
print('小于等于关系3=', (1, 2, 3) <= (7, 1, 2))
print('大于等于关系1=', 6 >= 5)
print('大于等于关系2=', [7, 6] >= [2, 5])
print('大于等于关系3=', (1, 2, 3) >= (7, 1, 2))
