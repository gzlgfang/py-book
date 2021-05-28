# 12-list_2.py 列表操作及内置函数
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ['city', 'guzhou']
list4 = list1 + list2 + list3
print("list4=", list4)
list5 = 3 * list1
list6 = list3 * 2
list7 = list1 * (-1)
list8 = list1 * True
list9 = list1 * False
list10 = list1 * 0
print("list5=", list5)
print("list6=", list6)
print("list7=", list7)
print("list8=", list8)
print("list9=", list9)
print("list10=", list10)
print(len([1, 2, 3]), ",", len([1, 3, [4, 6], "abc"]), ",", len([]))
li_1 = [1, 2, 3, [4, 5], 5, 6, 7, 8, 9]
print(li_1[2], ",", li_1[3], ",", li_1[4:8])
print(li_1[2:-1:2], ",", li_1[-5:-1])  # -1表示最后一个元素
print(li_1[:], ",", li_1[3:])  # 默认step为1
print(type(li_1[2]))
print("m1=", max([1, 2, 9, 7]), ",", "m2=", min([1, 2, 9, -8]))
li_2 = [1, 2, 3]
li_2.append(4)
print("li_2=", li_2)
li_2.append("abc")
print("li_2=", li_2)
li_2.append([5, 6])
print("li_2=", li_2)
li_2.append((7, 8))
print("li_2=", li_2)
list_3 = [1, 2, 3, "a", "b", [7, 8]]
print("list_3=", list_3)
print(list_3.reverse())
print("list_3=", list_3)
list_4 = [6, 7, 8, 9]
print("newlist=", list_4[::-1], ",list_4=", list_4)
list_5 = ["s", "c", "u", "t"]
print(list_5.insert(2, "华工"))
print("list_5=", list_5)
list_6 = [5, 1, 5, 6, 7, 6]
print(list_6.remove(5))
print("list_6=", list_6)
li_px1 = [3, 12, 1, 9, 2]
li_px2 = ["r", "x", "2", "-2", "e"]
li_px3 = ["b", "b2", "ba", "bc", "a", "β"]
li_px4 = [[1, 2], [5, 1], [4, 7], [3, 6]]
li_px1.sort(), li_px2.sort(), li_px3.sort(), li_px4.sort()
print("li_px1=", li_px1)
print("li_px2=", li_px2)
print("li_px3=", li_px3)
print("li_px4=", li_px4)
# 获取子列表的第二个元素


def takeSecond(li_px):
    return li_px[1]


li_px4.sort(key=takeSecond, reverse=True)
print("以子列表第2个元素降序排列的列表=", li_px4)
print(2 in [3, 6, 2])  # 判断数字是否在列表中
print("a" in ["b", "c", "A", "aa"])  # 判断字符串是否在列表中
print([3, 4] in (6, 5, [3, 4]))  # 判断子列表串是否在列表中
print((1, 2) in [8, "9", (1, 2)])  # 判断元祖是否在列表中
li_ext = [1, 2, 3]
li_ext.extend([5, 6, 7])  # 扩展序列为列表
print(li_ext)
li_ext.append([5, 6, 7])  # append方法是单个对象添加，不对添加对象展开
li_ext.extend((8, 9, 10))  # 扩展序列为元祖
print(li_ext)
li_ext.extend({11, 12, 13})  # 扩展序列为集合
print(li_ext)
li_ext.extend("广州华工")  # 扩展序列为字符串
print(li_ext)
li_ext.append(510640)  # int类数据不能扩展，只能作为单个对象添加
print(li_ext)
li_cot = [1, 2, 1, "ab", "a", "中国", [5, 6], (1, 2, 3), {"a", "b", "c"}]
print(li_cot.count(1))
print(li_cot.count("a"))
print(li_cot.count([5, 6]))
print(li_cot.count((1, 2, 3)))
print(li_cot.count({"a", "b", "c"}))
print(li_cot.count(-8))
li_ind = [1, 2, (3, 4), "sc", 2, "sc", (3, 4), {"a", "b", "c"}]
print("index1=", li_ind.index(2))
print("index2=", li_ind.index((3, 4)))
print("index3=", li_ind.index("sc"))
print("index4=", li_ind.index({"a", "b", "c"}))
li_del = [1, 2, 3, 4, 5, 6]
print(li_del.pop())
print(li_del.pop(2))
print(li_del)
print(list("123"), list((4, 5, 6)), list(
    {"7", "8", "9"}), list({"Hu": 90, "Wang": 80}))
print("list1=", list({"Hu": 90, "Wang": 80}.values()))
print("list1=", list({"Hu": 90, "Wang": 80}.keys()))
listr = ['华', '南', '理', '工', '大', '学']
print(str(listr), type(str(listr)))
str2 = ''.join(listr)
print("str2=", str2, type(str2))
