import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, PathPatch
from matplotlib.path import Path
from matplotlib.transforms import Affine2D


def draw_yinyang(ax, center=(0, 0), radius=1.0, line_width=2):
    # 参数计算
    big_radius = radius
    s_r = big_radius / 6  # small_radius
    h_r = big_radius / 2  ##half_radius

    # 绘制外圆边框
    border = Circle(center, big_radius, fill=False, edgecolor="black", lw=line_width)
    ax.add_patch(border)

    # 阳中的阴眼（黑色小圆）
    upper_eye = Circle(
        (center[0], center[1] + h_r),
        s_r,
        facecolor="black",
        edgecolor="black",
        zorder=4,
    )
    ax.add_patch(upper_eye)

    # 阴中的阳眼（白色小圆）
    lower_eye = Circle(
        (center[0], center[1] - h_r),
        s_r,
        facecolor="red",
        edgecolor="black",
        zorder=4,
    )
    ax.add_patch(lower_eye)
    x1 = np.linspace(0, h_r, 100)
    x2 = np.linspace(h_r, radius, 100)
    y1 = h_r - np.sqrt(h_r**2 - x1**2)
    y2 = np.sqrt(radius**2 - x2**2)

    x3 = x1
    y3_1 = h_r + np.sqrt(h_r**2 - x3**2)
    y3_2 = np.sqrt(radius**2 - x3**2)

    ax.stackplot(x2, y2, colors="black")
    ax.stackplot(x3, y3_2, colors="black")
    ax.stackplot(x3, y3_1, colors="white")
    ax.stackplot(x1, y1, colors="black")

    x4 = np.linspace(-radius, 0, 100)
    y4 = -np.sqrt(radius**2 - x4**2)

    x5 = np.linspace(-h_r, 0, 50)
    y5_1 = -h_r - np.sqrt(h_r**2 - x5**2)

    y5_2 = -h_r + np.sqrt(h_r**2 - x5**2)
    ax.stackplot(x4, y4, colors="white")
    ax.stackplot(x5, y5_1, colors="black")
    ax.stackplot(x5, y5_2, colors="white")

    x6 = np.linspace(0, radius, 100)
    y6 = -np.sqrt(radius**2 - x6**2)
    ax.stackplot(x6, y6, colors="black")
    # print(y3_1, y3_2)
    # ax.plot(-x, -y, lw=line_width, c="black")
    # print(x, y)


fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
ax.axis("off")

# 绘制阴阳八卦图
draw_yinyang(ax, center=(0, 0), radius=3, line_width=3)

# 设置坐标范围
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-4.5, 4.5)

plt.show()
