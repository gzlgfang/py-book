import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, PathPatch
from matplotlib.path import Path
from matplotlib.transforms import Affine2D


def draw_yinyang(ax, center=(0, 0), radius=1.0, line_width=2):
    # 参数计算
    big_radius = radius
    small_radius = big_radius / 6
    half_radius = big_radius / 2

    # 绘制外圆边框
    border = Circle(center, big_radius, fill=False, edgecolor="black", lw=line_width)
    ax.add_patch(border)

    # ===== 修复点：使用 Wedge 代替 Arc =====
    # 上半圆（白色阳）
    upper_half = Wedge(
        center,
        big_radius,
        0,
        180,
        facecolor="white",
        edgecolor="black",
        linewidth=line_width,
        zorder=2,
    )
    ax.add_patch(upper_half)

    # 下半圆（黑色阴）
    lower_half = Wedge(
        center,
        big_radius,
        180,
        360,
        facecolor="black",
        edgecolor="black",
        linewidth=line_width,
        zorder=2,
    )
    ax.add_patch(lower_half)

    # ===== 绘制S形曲线（使用贝塞尔曲线）=====
    verts = [
        (center[0] + big_radius, center[1]),  # 起点
        (center[0], center[1] + big_radius / 2),  # 控制点1
        (center[0] - big_radius, center[1]),  # 控制点2
        (center[0], center[1] - big_radius / 2),  # 控制点3
        (center[0] + big_radius, center[1]),  # 终点
    ]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4]

    path = Path(verts, codes)
    patch = PathPatch(
        path, facecolor="none", edgecolor="black", lw=line_width, zorder=3
    )
    ax.add_patch(patch)

    # ===== 绘制阴阳眼 =====
    # 阳中的阴眼（黑色小圆）
    upper_eye = Circle(
        (center[0], center[1] + half_radius),
        small_radius,
        facecolor="black",
        edgecolor="black",
        zorder=4,
    )
    ax.add_patch(upper_eye)

    # 阴中的阳眼（白色小圆）
    lower_eye = Circle(
        (center[0], center[1] - half_radius),
        small_radius,
        facecolor="white",
        edgecolor="black",
        zorder=4,
    )
    ax.add_patch(lower_eye)

    # ===== 绘制八卦符号 =====
    trigrams = [
        (22.5, [1, 1, 1]),  # 乾
        (67.5, [0, 1, 1]),  # 兑
        (112.5, [1, 0, 1]),  # 离
        (157.5, [0, 0, 1]),  # 震
        (202.5, [0, 0, 0]),  # 巽
        (247.5, [1, 0, 0]),  # 坎
        (292.5, [0, 1, 0]),  # 艮
        (337.5, [1, 1, 0]),  # 坤
    ]

    trig_radius = big_radius * 1.2
    trig_length = big_radius * 0.15
    trig_gap = big_radius * 0.05

    for angle_offset, yaos in trigrams:
        angle_rad = np.deg2rad(angle_offset)
        x = center[0] + trig_radius * np.cos(angle_rad)
        y = center[1] + trig_radius * np.sin(angle_rad)

        # 绘制三爻
        for i, yao in enumerate(yaos):
            yao_y = y - (i - 1) * (trig_length + trig_gap)
            if yao == 1:  # 阳爻
                ax.plot(
                    [x - trig_length / 2, x + trig_length / 2],
                    [yao_y, yao_y],
                    color="black",
                    lw=line_width * 0.8,
                )
            else:  # 阴爻
                ax.plot(
                    [x - trig_length / 2, x - trig_length / 6],
                    [yao_y, yao_y],
                    color="black",
                    lw=line_width * 0.8,
                )
                ax.plot(
                    [x + trig_length / 6, x + trig_length / 2],
                    [yao_y, yao_y],
                    color="black",
                    lw=line_width * 0.8,
                )

        # 调整卦象方向
        transform = Affine2D().rotate_around(x, y, angle_rad + np.pi / 2)
        ax.transData += transform


# 创建画布
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
ax.axis("off")

# 绘制阴阳八卦图
draw_yinyang(ax, center=(0, 0), radius=3, line_width=3)

# 设置坐标范围
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-4.5, 4.5)

plt.show()
