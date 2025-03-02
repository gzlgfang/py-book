import turtle
import math

# 设置画布和画笔
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Earth - Moon - Sun System")
screen.bgcolor("black")

# 创建太阳
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(stretch_len=3, stretch_wid=3)
sun.penup()
sun.goto(0, 0)

# 创建地球
earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.shapesize(stretch_len=1.5, stretch_wid=1.5)
earth.penup()
earth.goto(200, 0)

# 创建月亮
moon = turtle.Turtle()
moon.color("gray")
moon.penup()
moon.goto(250, 0)

# 定义地球和月亮的轨道半径和速度
earth_orbit_radius = 200
earth_orbit_speed = 0.01
moon_orbit_radius = 50
moon_orbit_speed = 0.05

# 定义初始角度
earth_angle = 0
moon_angle = 0


def draw_moon_phase(phase):
    """
    根据月相绘制月亮
    :param phase: 月相值，范围从 0 到 1
    """
    moon.clear()
    moon.begin_fill()
    # 绘制圆形部分
    moon.circle(10)
    # 根据月相绘制月牙部分
    if phase < 0.5:
        # 绘制左月牙
        moon.penup()
        moon.goto(moon.xcor(), moon.ycor() - 10)
        moon.pendown()
        moon.setheading(90)
        arc_angle = 180 - 360 * phase
        moon.circle(10, arc_angle)
    elif phase > 0.5:
        # 绘制右月牙
        moon.penup()
        moon.goto(moon.xcor(), moon.ycor() + 10)
        moon.pendown()
        moon.setheading(270)
        arc_angle = 360 * (phase - 0.5)
        moon.circle(-10, arc_angle)
    moon.end_fill()


# 主循环
while True:
    # 计算地球的位置
    earth_x = earth_orbit_radius * math.cos(earth_angle)
    earth_y = earth_orbit_radius * math.sin(earth_angle)
    earth.goto(earth_x, earth_y)

    # 计算月亮相对地球的位置
    moon_relative_x = moon_orbit_radius * math.cos(moon_angle)
    moon_relative_y = moon_orbit_radius * math.sin(moon_angle)

    # 计算月亮的绝对位置
    moon_x = earth_x + moon_relative_x
    moon_y = earth_y + moon_relative_y
    moon.goto(moon_x, moon_y)

    # 计算月相
    moon_phase_angle = math.atan2(moon_relative_y, moon_relative_x) - math.atan2(
        earth_y, earth_x
    )
    moon_phase = (1 + math.cos(moon_phase_angle)) / 2

    # 根据月相绘制月亮
    draw_moon_phase(moon_phase)

    # 更新角度
    earth_angle += earth_orbit_speed
    moon_angle += moon_orbit_speed
