sum1, sum2, sum3 = 0, 0, 0
for x in range(10):  # x取0到9，每次增加1
    sum1 = sum1 + (x + 1)  # 缩进4格
    sum2 = sum2 + (x + 1) * (x + 1)
    sum3 = sum3 + (x + 1) * (x + 1) * (x + 1)  # 循环到此为止
print("sum1,sum2,sum3=", sum1, sum2, sum3)
