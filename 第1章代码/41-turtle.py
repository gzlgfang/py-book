# turtle库应用41-turtle.py
from turtle import *  # 方便函数直接调用
import numpy as np
from time import *
# tracer(False)# 直接出结果
speed(10)
setup(650, 650)
dic = {
    1: 'red',
    2: 'orange',
    3: 'yellow',
    4: 'green',
    5: 'blue',
    6: 'purple',
    7: 'pink',
    8: 'purple'}
title('彩色三角函数绘制')
penup()
goto(-400, 0)
pendown()
pensize(5)
for i in range(0, 7 * 360 + 1):
    x = i * 2 * np.pi / 360
    y = 100 * np.sin(x)
    j = int(i / 360)
    if j >= 7:
        j = 6
    pencolor(dic[j + 1])
    goto(20 * x - 400, y)
    # print(x,y)
pencolor('black')
penup()
goto(-400, 0)
pendown()
goto(520, 0)
penup()
goto(-400, -200)
pendown()
goto(-400, 200)
goto(-410, 170)
goto(-390, 170)
goto(-400, 200)
penup()
goto(520, 0)
pendown()
goto(490, 10)
goto(490, -10)
goto(520, 0)
penup
hideturtle()  # 隐藏海龟
sleep(3)  # 休眠3秒
reset()  # 回到原点
# from turtle import *
#import turtle as tu
dic = {
    1: 'red',
    2: 'orange',
    3: 'yellow',
    4: 'green',
    5: 'blue',
    6: 'purple',
    7: 'pink'}
title('彩色圆绘制')
for i in range(7):
    penup()
    goto(0, -30 * (i + 1))  # 从里面最小的一个圆的底部，慢慢变大
    pendown()
    pensize(5 * (i + 1))
    pencolor(dic[i + 1])
    circle(30 * (i + 1))
    hideturtle()  # 隐藏海龟
sleep(3)
reset()
# from turtle import * #方便函数直接调用
setup(400, 400)  # 设置窗体
screensize(800, 450, bg="blue")  # 设置画布
title('太阳花绘制')
tracer(False)
color("red", "yellow")
speed(10)
begin_fill()
goto(0, 0)
pendown()
for i in range(50):
    fd(280)
    left(170)
end_fill()
hideturtle()  # 隐藏海龟
done()
