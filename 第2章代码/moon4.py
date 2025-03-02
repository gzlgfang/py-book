import pygame
import math
import sys

# 初始化Pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("太阳-地球-月球系统")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
GRAY = (169, 169, 169)

# 天体参数
CENTER = (WIDTH // 2, HEIGHT // 2)
SUN_RADIUS = 60
EARTH_RADIUS = 30
MOON_RADIUS = 16

# 轨道参数
EARTH_ORBIT = 400
MOON_ORBIT = 80

# 角速度（弧度/帧）
EARTH_SPEED = 0.005
MOON_SPEED = 0.05

# 初始化角度
earth_angle = 0
moon_angle = 0


def draw_dashed_circle(surface, color, center, radius, dash_length=10):
    """绘制虚线圆"""
    points = []
    for angle in range(0, 360, 5):
        x = center[0] + radius * math.cos(math.radians(angle))
        y = center[1] + radius * math.sin(math.radians(angle))
        if angle % (2 * dash_length) < dash_length:
            points.append((x, y))
        else:
            if points:
                pygame.draw.aalines(surface, color, False, points)
                points = []
    if points:
        pygame.draw.aalines(surface, color, False, points)


def draw_moon_phase(pos, sun_dir, size):
    """绘制月相"""
    # 绘制暗面
    pygame.draw.circle(screen, GRAY, pos, size)

    # 计算亮面方向
    angle = math.atan2(sun_dir[1], sun_dir[0])
    start_angle = angle - math.pi / 2
    end_angle = angle + math.pi / 2

    # 生成扇形点
    points = [pos]
    for i in range(31):  # 30 segments
        theta = start_angle + (end_angle - start_angle) * i / 30
        x = pos[0] + size * math.cos(theta)
        y = pos[1] + size * math.sin(theta)
        points.append((x, y))
    pygame.draw.polygon(screen, WHITE, points)


# 主循环
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # 绘制太阳
    pygame.draw.circle(screen, YELLOW, CENTER, SUN_RADIUS)

    # 更新地球位置
    earth_x = CENTER[0] + EARTH_ORBIT * math.cos(earth_angle)
    earth_y = CENTER[1] + EARTH_ORBIT * math.sin(earth_angle)
    earth_angle += EARTH_SPEED

    # 更新月球位置
    moon_x = earth_x + MOON_ORBIT * math.cos(moon_angle)
    moon_y = earth_y + MOON_ORBIT * math.sin(moon_angle)
    moon_angle += MOON_SPEED

    # 绘制地球轨道
    draw_dashed_circle(screen, WHITE, CENTER, EARTH_ORBIT)

    # 绘制地球
    pygame.draw.circle(screen, BLUE, (int(earth_x), int(earth_y)), EARTH_RADIUS)

    # 绘制月球轨道
    draw_dashed_circle(screen, WHITE, (int(earth_x), int(earth_y)), MOON_ORBIT)

    # 绘制月相（太阳到月球的方向向量）
    sun_to_moon = (CENTER[0] - moon_x, CENTER[1] - moon_y)
    draw_moon_phase((int(moon_x), int(moon_y)), sun_to_moon, MOON_RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
