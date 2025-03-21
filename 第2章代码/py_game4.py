import pygame
import random
import math

# 初始化pygame
pygame.init()
# 设置屏幕尺寸
screen_width = 3000
screen_height = 2000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball Animation")
# 定义大圆的参数
big_radius = 500
big_center = (screen_width // 2, screen_height // 2)
# 定义小球的参数
num_balls = 2
ball_radius = 25
ball_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
# 定义小球类
class Ball:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.collided = False

    def move(self, dt):
        # 计算在本次时间间隔内是否会碰到大球壁
        distance_to_wall = self._calculate_distance_to_wall()
        time_to_wall = self._calculate_time_to_wall(distance_to_wall)
        if time_to_wall <= dt:
            # 会碰到大球壁，先移动到碰撞点
            self._move_to_wall(time_to_wall)
            self._handle_wall_collision()
            # 处理剩余时间
            remaining_dt = dt - time_to_wall
            if remaining_dt > 0:
                self.x += self.vx * remaining_dt
                self.y += self.vy * remaining_dt
        else:
            # 不会碰到大球壁，正常移动
            self.x += self.vx * dt
            self.y += self.vy * dt

    def draw(self):
        pygame.draw.circle(
            screen, self.color, (int(self.x), int(self.y)), int(ball_radius)
        )

    def _calculate_distance_to_wall(self):
        current_distance = math.sqrt(
            (self.x - big_center[0]) ** 2 + (self.y - big_center[1]) ** 2
        )
        return big_radius - current_distance - ball_radius

    def _calculate_time_to_wall(self, distance_to_wall):
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed == 0:
            return float("inf")
        # 计算速度向量与球心到当前位置向量的夹角余弦值
        vector_to_center = [self.x - big_center[0], self.y - big_center[1]]
        dot_product = self.vx * vector_to_center[0] + self.vy * vector_to_center[1]
        if dot_product >= 0:
            return float("inf")  # 远离大球壁
        return abs(distance_to_wall / speed)

    def _move_to_wall(self, time_to_wall):
        self.x += self.vx * time_to_wall
        self.y += self.vy * time_to_wall

    def _handle_wall_collision(self):
        distance = math.sqrt(
            (self.x - big_center[0]) ** 2 + (self.y - big_center[1]) ** 2
        )
        normal_x = (self.x - big_center[0]) / distance
        normal_y = (self.y - big_center[1]) / distance
        incident_x = self.vx
        incident_y = self.vy
        dot_product = incident_x * normal_x + incident_y * normal_y
        reflection_x = incident_x - 2 * dot_product * normal_x
        reflection_y = incident_y - 2 * dot_product * normal_y
        self.vx = reflection_x
        self.vy = reflection_y

    def check_collision_with_other_balls(self, other_balls):
        if self.collided:
            return []
        for other_ball in other_balls:
            if other_ball is not self and not other_ball.collided:
                distance = math.sqrt(
                    (self.x - other_ball.x) ** 2 + (self.y - other_ball.y) ** 2
                )
                if distance <= 2 * ball_radius:
                    # 标记两个球为已碰撞
                    self.collided = True
                    other_ball.collided = True
                    # 随机选择一个碰撞球的颜色
                    color = random.choice([self.color, other_ball.color])
                    # 随机生成新球的位置、速度和方向
                    angle = random.uniform(0, 2 * math.pi)
                    speed = 100 * random.uniform(1, 3)
                    vx = speed * math.cos(angle)
                    vy = speed * math.sin(angle)
                    new_x = big_center[0] + random.uniform(
                        -big_radius + ball_radius, big_radius - ball_radius
                    )
                    new_y = big_center[1] + random.uniform(
                        -big_radius + ball_radius, big_radius - ball_radius
                    )
                    new_ball = Ball(new_x, new_y, vx, vy, color)
                    return [new_ball]
        return []


# 初始化小球
balls = []
for i in range(num_balls):
    angle = random.uniform(0, 2 * math.pi)
    speed = 100 * random.uniform(1, 3)
    vx = speed * math.cos(angle)
    vy = speed * math.sin(angle)
    x = big_center[0] + random.uniform(
        -big_radius + ball_radius, big_radius - ball_radius
    )
    y = big_center[1] + random.uniform(
        -big_radius + ball_radius, big_radius - ball_radius
    )
    ball = Ball(x, y, vx, vy, ball_colors[i % len(ball_colors)])
    balls.append(ball)
# 游戏主循环
clock = pygame.time.Clock()
running = True
dt = 1 / 60  # 固定时间步长
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    # 绘制大圆
    pygame.draw.circle(screen, (0, 0, 0), big_center, big_radius, 2)
    # 处理小球的移动和碰撞
    new_balls = []
    for ball in balls:
        ball.move(dt)
        new_balls.extend(ball.check_collision_with_other_balls(balls))
    # 重置所有球的碰撞标记
    for ball in balls:
        ball.collided = False
    # 添加新生成的球
    balls.extend(new_balls)
    # 绘制小球
    for ball in balls:
        ball.draw()
    pygame.display.flip()
    clock.tick(60)
# 退出pygame
pygame.quit()
