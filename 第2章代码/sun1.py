import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定义常量
G = 6.67430e-11  # 引力常数 (m^3 kg^-1 s^-2)
M_sun = 1.989e30  # 太阳质量 (kg)

# 行星数据: 名称, 质量(kg), 半长轴(m), 偏心率
planets_data = [
    ("Mercury", 3.301e23, 5.791e10, 0.2056),
    ("Venus", 4.867e24, 1.082e11, 0.0068),
    ("Earth", 5.972e24, 1.496e11, 0.0167),
    ("Mars", 6.417e23, 2.279e11, 0.0934),
    ("Jupiter", 1.898e27, 7.785e11, 0.0484),
    ("Saturn", 5.683e26, 1.434e12, 0.0542),
    ("Uranus", 8.681e25, 2.871e12, 0.0472),
    ("Neptune", 1.024e26, 4.497e12, 0.0086),
]


def keplerian_orbit(a, e, t):
    """计算开普勒椭圆轨道上的位置"""
    n = np.sqrt(G * M_sun / a**3)  # 平均运动角速度
    mean_anomaly = n * t  # 平均近点角
    eccentric_anomaly = mean_anomaly.copy()
    for _ in range(10):  # 牛顿迭代法求解偏近点角
        eccentric_anomaly -= (
            eccentric_anomaly - e * np.sin(eccentric_anomaly) - mean_anomaly
        ) / (1 - e * np.cos(eccentric_anomaly))
    true_anomaly = 2 * np.arctan(
        np.sqrt((1 + e) / (1 - e)) * np.tan(eccentric_anomaly / 2)
    )
    r = a * (1 - e * np.cos(eccentric_anomaly))  # 极径
    x = r * np.cos(true_anomaly)
    y = r * np.sin(true_anomaly)
    return x, y


# 初始化图形
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
ax.set_xlim(-5e12, 5e12)
ax.set_ylim(-5e12, 5e12)
ax.scatter([0], [0], color="yellow", label="Sun")  # 太阳

planet_lines = []
for planet_name, mass, semi_major_axis, eccentricity in planets_data:
    (line,) = ax.plot([], [], label=planet_name)
    planet_lines.append(line)

# 时间步长和总时间
dt = 24 * 3600  # 每天
total_time = 365 * dt * 5  # 5年


def update(frame):
    t = frame * dt
    for i, (_, _, a, e) in enumerate(planets_data):
        x, y = keplerian_orbit(a, e, t)
        planet_lines[i].set_data(x, y)
    return planet_lines


ani = FuncAnimation(fig, update, frames=int(total_time / dt), interval=100, blit=True)
plt.legend()
plt.title("Solar System Planetary Orbits")
plt.show()
