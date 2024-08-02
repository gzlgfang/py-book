# 字符串运算、转义及基本函数
print("sc" + "ut")
print("sc" in "scut")
print("ce" in "scut")
print("sc" not in "scut")
print("ce" not in "scut")
print(r"ch\scut\'ce")
print(R"ch\scut\nce")
print(
    "ch.scut\
ce"
)
print("ch\\scutce")
print("ch'scutce")
print('ch"scutce')
print("ch\bscutce")
print("chscut\fce")
print("ch\nscutce")
print("ch\vscutce")
print("ch\tscutce")
print("ch\rscutce")

print("sc" + "ut")  ##连接操作
s = "123广州天河华工"
s1 = s
print(s1[::-1])  # 逆转运算
print("s=", s, "s1=", s1)
print(s.replace("华工", "华农"))
s2 = "  12345  "
print(s2.strip())  # 删除字符串前后空格
s3 = "I like reding"
print(s3.split())  # 默认空格拆分字符串，返回列表
print(s3.split(sep="e"))  # 以"e"作为拆分标记拆分字符串，返回列表
print("".join(reversed(s)))  # 字符串反转
s4 = "i love china "
print(s4.upper())  # 全部改为大小
s5 = "GUANGZHOU CHINA SCUT"
print(s5.lower())  # 全部改为小写
print(s4.title())  # 首字母改为大写
print(s4.find("v", 2, -1))  # 从序号2开始到结束（-1）寻找字符v，将对应的索引位置赋值
print(int("123456"))  # 字符串转数字
