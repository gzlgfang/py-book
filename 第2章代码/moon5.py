import pygame
import math
import sys
import numpy as np

# 初始化Pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D 太阳系模拟")

# 颜色定义
COLORS = {
    "bg": (0, 0, 20),
    "sun": (255, 255, 100),
    "earth": (70, 120, 200),
    "moon_dark": (80, 80, 80),
    "moon_light": (255, 255, 150),
}

# 天体参数
CENTER = (WIDTH // 2, HEIGHT // 2)
SUN_RADIUS = 40
EARTH_RADIUS = 20
MOON_RADIUS = 10

# 轨道参数
EARTH_ORBIT = 300
MOON_ORBIT = 50

# 运动参数
EARTH_SPEED = 0.002
MOON_SPEED = 0.02


class CelestialBody:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.cache = {}  # 缓存不同光照角度的表面

    def get_illuminated_surface(self, light_angle):
        """生成带光照效果的表面"""
        if light_angle in self.cache:
            return self.cache[light_angle]

        # 创建透明表面
        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        center = (self.radius, self.radius)

        # 生成渐变遮罩
        for y in range(self.radius * 2):
            for x in range(self.radius * 2):
                dx = x - self.radius
                dy = y - self.radius
                distance = math.sqrt(dx**2 + dy**2)

                if distance > self.radius:
                    continue

                # 计算光照强度（点积）
                angle = math.atan2(dy, dx)
                intensity = math.cos(angle - light_angle)
                intensity = max(0, intensity**0.5)  # 增强对比度

                # 混合颜色
                if isinstance(self.color, tuple):  # 单色天体
                    base_color = np.array(self.color)
                    light_color = np.array(COLORS["sun"])
                else:  # 月球特殊处理
                    base_color = np.array(COLORS["moon_dark"])
                    light_color = np.array(COLORS["moon_light"])

                final_color = base_color * (1 - intensity) + light_color * intensity
                surface.set_at((x, y), final_color.astype(int))

        self.cache[light_angle] = surface
        return surface


# 创建天体对象
sun = CelestialBody(SUN_RADIUS, COLORS["sun"])
earth = CelestialBody(EARTH_RADIUS, COLORS["earth"])
moon = CelestialBody(MOON_RADIUS, "moon")


def draw_orbit(surface, center, radius):
    """绘制虚线轨道"""
    dash_len = 10
    for angle in range(0, 360, 5):
        x = center[0] + radius * math.cos(math.radians(angle))
        y = center[1] + radius * math.sin(math.radians(angle))
        if angle % (2 * dash_len) < dash_len:
            pygame.draw.circle(surface, (100, 100, 100), (int(x), int(y)), 1)


# 初始化角度
earth_angle = 0
moon_angle = 0

# 主循环
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(COLORS["bg"])

    # 绘制太阳
    sun_surf = sun.get_illuminated_surface(0)
    screen.blit(sun_surf, (CENTER[0] - SUN_RADIUS, CENTER[1] - SUN_RADIUS))

    # 更新地球位置
    earth_x = CENTER[0] + EARTH_ORBIT * math.cos(earth_angle)
    earth_y = CENTER[1] + EARTH_ORBIT * math.sin(earth_angle)

    # 绘制地球轨道
    draw_orbit(screen, CENTER, EARTH_ORBIT)

    # 绘制地球
    earth_surf = earth.get_illuminated_surface(earth_angle + math.pi)
    screen.blit(earth_surf, (int(earth_x) - EARTH_RADIUS, int(earth_y) - EARTH_RADIUS))

    # 更新月球位置
    moon_x = earth_x + MOON_ORBIT * math.cos(moon_angle)
    moon_y = earth_y + MOON_ORBIT * math.sin(moon_angle)

    # 计算月球光照角度（太阳方向到月球的夹角）
    sun_dir = math.atan2(CENTER[1] - moon_y, CENTER[0] - moon_x)

    # 绘制月球
    moon_surf = moon.get_illuminated_surface(sun_dir)
    screen.blit(moon_surf, (int(moon_x) - MOON_RADIUS, int(moon_y) - MOON_RADIUS))

    # 绘制月球轨道
    draw_orbit(screen, (int(earth_x), int(earth_y)), MOON_ORBIT)

    # 更新角度
    earth_angle += EARTH_SPEED
    moon_angle += MOON_SPEED

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
