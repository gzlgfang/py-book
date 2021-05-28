# 多段函数计算32-multifun.py
flag = 1
while (flag):
    x = eval(input("请输入自变量x的值并回车"))
    if x <= 10:
        print("y=", 3 * x)
    elif x <= 20:
        print("y=", 2 * x + 10)
    elif x <= 30:
        print("y=", x + 40)
    elif x > 30:
        print("y=", 0.5 * x + 50)
    flag = input('是否需要继续计算其他x的y值，是输入1，否回车')
