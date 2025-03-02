import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定义太阳和行星数据，轨道半径经过平方根缩放，周期使用真实数据：
sun = {"color": "red", "size": 500}
planets = [
    {
        "name": "Mercury",
        "orbital_radius": np.sqrt(0.387 * 10),
        "period": 0.24,
        "color": "gray",
        "size": 20,
    },
    {
        "name": "Venus",
        "orbital_radius": np.sqrt(0.723 * 10),
        "period": 0.615,
        "color": "orange",
        "size": 25,
    },
    {
        "name": "Earth",
        "orbital_radius": np.sqrt(1.0 * 10),
        "period": 1.0,
        "color": "blue",
        "size": 30,
    },
    {
        "name": "Mars",
        "orbital_radius": np.sqrt(1.524 * 10),
        "period": 1.88,
        "color": "red",
        "size": 22,
    },
    {
        "name": "Jupiter",
        "orbital_radius": np.sqrt(5.203 * 10),
        "period": 11.86,
        "color": "brown",
        "size": 50,
    },
    {
        "name": "Saturn",
        "orbital_radius": np.sqrt(9.539 * 10),
        "period": 29.46,
        "color": "gold",
        "size": 45,
    },
    {
        "name": "Uranus",
        "orbital_radius": np.sqrt(19.18 * 10),
        "period": 84.01,
        "color": "lightblue",
        "size": 40,
    },
    {
        "name": "Neptune",
        "orbital_radius": np.sqrt(30.06 * 10),
        "period": 164.8,
        "color": "blue",
        "size": 40,
    },
    {
        "name": "Pluto",
        "orbital_radius": np.sqrt(39.48 * 10),
        "period": 247.9,
        "color": "darkgray",
        "size": 15,
    },
]
# 初始化图形：
fig, ax = plt.subplots(figsize=(16, 16))
ax.set_aspect("equal")
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.axis("off")
# 绘制太阳：
sun_scatter = ax.scatter(0, 0, color=sun["color"], s=sun["size"], zorder=5)
# 初始化行星的位置和角度：
planet_scatters = []
angles = np.zeros(len(planets))  # 初始角度为90
for planet in planets:
    x = planet["orbital_radius"] * np.cos(0)
    y = planet["orbital_radius"] * np.sin(0)
    scatter = ax.scatter(
        x, y, color=planet["color"], s=5 * planet["size"], label=planet["name"]
    )
    planet_scatters.append(scatter)
# 定义更新函数，使用真实周期计算角速度：
speed_factor = 0.3  # 调整这个值以改变整体速度
dt = 0.1  # 时间步长，单位是年


def update(frame):
    for i, planet in enumerate(planets):
        # 计算角速度（弧度/年）
        omega = (2 * np.pi / planet["period"]) * speed_factor
        # 更新角度
        angles[i] += omega * dt
        # 计算新位置
        x = planet["orbital_radius"] * np.cos(angles[i])
        y = planet["orbital_radius"] * np.sin(angles[i])
        # 更新散点位置
        planet_scatters[i].set_offsets(np.c_[x, y])
    return [sun_scatter] + planet_scatters


# 创建动画：
ani = FuncAnimation(fig, update, frames=range(500), interval=50, blit=True)
# 添加图例：
plt.legend(loc="lower left", bbox_to_anchor=(0, 0))
# 显示动画：
plt.show()

# 在这个代码中，speed_factor和dt的值可以调整以控制动画的速度。例如，speed_factor=5，dt=0.02，可能得到更平滑的动画。用户可以根据需要调整这些参数。

# 此外，行星的大小和颜色也可以根据实际外观进行调整，例如，木星更大，颜色更接近真实颜色。

# 最后，可能需要添加轨道线，让每个行星的路径显示出来。这可以通过在初始化时绘制每个行星的轨道圆，或者在更新函数中记录轨迹。但为了代码简洁和性能，可能不添加轨迹线。

# 综上，以上代码应该能够展示九大行星绕太阳运行的动画，虽然轨道半径经过缩放，角速度基于真实周期调整，整体视觉效果能够展示内层行星转得快，外层转得慢的特点。
