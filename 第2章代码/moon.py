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
sun.penup()
sun.goto(0, 0)
sun.pendown()

# 创建地球
earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.penup()
earth.goto(200, 0)
earth.pendown()

# 创建月亮
moon = turtle.Turtle()
moon.shape("circle")
moon.color("gray")
moon.penup()
moon.goto(250, 0)
moon.pendown()

# 定义地球和月亮的轨道半径和速度
earth_orbit_radius = 200
earth_orbit_speed = 0.01
moon_orbit_radius = 50
moon_orbit_speed = 0.05

# 定义初始角度
earth_angle = 0
moon_angle = 0

# 主循环
while True:
    # 计算地球的位置
    earth_x = earth_orbit_radius * math.cos(earth_angle)
    earth_y = earth_orbit_radius * math.sin(earth_angle)
    earth.goto(earth_x, earth_y)

    # 计算月亮的位置
    moon_x = earth_x + moon_orbit_radius * math.cos(moon_angle)
    moon_y = earth_y + moon_orbit_radius * math.sin(moon_angle)
    moon.goto(moon_x, moon_y)

    # 计算月相
    # 月相取决于月亮、地球和太阳的相对位置
    # 这里简单地根据月亮相对于地球和太阳的角度来计算月相
    moon_phase_angle = math.atan2(moon_y - earth_y, moon_x - earth_x) - math.atan2(
        earth_y, earth_x
    )
    moon_phase = (1 + math.cos(moon_phase_angle)) / 2

    # 根据月相改变月亮的颜色
    moon_color = (moon_phase, moon_phase, moon_phase)
    moon.color(moon_color)

    # 更新角度
    earth_angle += earth_orbit_speed
    moon_angle += moon_orbit_speed
