# 求四面开花数33-fourflower
n = 0
num = []
for i in range(1000, 10000):
    str_num = str(i)
    fourpower = eval(str_num[0])**4 + eval(str_num[1])**4 + \
        eval(str_num[2])**4 + eval(str_num[3])**4
    if fourpower == i:
        n = n + 1
        num.append(i)
        print(f"找到第{n}个四面开花数：{i}")
print(f"共找到{n}个四面开花数", num)
