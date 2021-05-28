# 42-turtle2.py
# 彩色圆绘制
from turtle import *
import turtle as tu
dic = {
    1: 'red',
    2: 'orange',
    3: 'yellow',
    4: 'green',
    5: 'blue',
    6: 'purple',
    7: 'pink'}
tu.title('彩色圆绘制')
for i in range(7):
    tu.penup()
    tu.goto(0, -30 * (i + 1))  # 从里面最小的一个圆的底部，慢慢变大
    tu.pendown()
    tu.pensize(5 * (i + 1))
    tu.pencolor(dic[i + 1])
    tu.circle(30 * (i + 1))
tu.hideturtle()  # 隐藏海龟
tu.done()
