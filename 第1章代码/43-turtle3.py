# 43-turtle3.py
# 太阳花绘制
from turtle import *  # 方便函数直接调用
setup(400, 400)  # 设置窗体
screensize(800, 450, bg="blue")  # 设置画布
title('太阳花绘制')
tracer(False)
color("red", "yellow")
speed(1)
begin_fill()
goto(0, 0)
pendown()
for i in range(50):
    fd(280)
    left(170)
end_fill()
hideturtle()  # 隐藏海龟
done()
