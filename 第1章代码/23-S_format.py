# 23-S_format.py打印格式函数
# 字符串任意调用1
print('{1}{0}您'.format('欢迎', '华工'))
# 字符串任意调用2
print('{2}{1}{2}{0}'.format(3, 5, 6))
# 小数点位数调用
print('{:.3f}'.format(3.14159))
# 百分比格式调用
print('{:.2%}'.format(0.12356))  # 保留2位小数的百分比格式
# 科学计数法调用
print('{:.5e}'.format(1245689756))  # 保留5位小数的科学计数法
# 列表索引参数调用
list1 = ['华工', '化工']
list2 = ['广州', 'www.scut.edu.cn']
print('学校：{0[0]},专业：{0[1]},地址：{1[0]},网址：{1[1]}'.format(list1, list2))
# 字典参数调用
dict1 = {"school": "华工", "specialty": "化工"}
print("学校：{school},专业：{specialty}".format(**dict1))
# 键值对调用
print("学校：{学校},专业：{专业}".format(学校="华工", 专业="化工"))
# 左填充格式
print('{:9>4d}'.format(21))
# 右填充格式
print('{:9<4d}'.format(21))
# 右对齐格式
print('{:>4d}'.format(21))
# 左对齐格式
print('{:<4d}'.format(21))
# 中间对齐格式
print('{:^4d}'.format(21))
# 转二进制
print('{:b}'.format(21))
# 转八进制
print('{:o}'.format(21))
# 转十进制
print('{:d}'.format(0x21))
# 转小写字母十六进制
print('{:x}'.format(31))
# 转大写字母十六进制
print('{:X}'.format(31))
# 转有进制标志小写十六进制
print('{:#x}'.format(31))
# 转有进制标志大写十六进制
print('{:#X}'.format(31))
# 转有进制标志二进制
print('{:#b}'.format(21))
# 转有进制标志八进制
print('{:#o}'.format(21))
# 转有进制标志十进制
print('{:#d}'.format(0x21))
