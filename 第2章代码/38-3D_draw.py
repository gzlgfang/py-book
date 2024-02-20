# 38-3D_draw.py
# 3D图形绘制
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as mticker

# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 16
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
# from mpl_toolkits.mplot3d.axes3d import Axes3D
# 数据处理
x = np.arange(-5, 5.01, 0.02)  # 将x从-5到5，间隔0.02进行取点
y = np.arange(-5, 5.01, 0.02)
X, Y = np.meshgrid(x, y)
R = np.sqrt((X**2 + Y**2) / 2)
Z = (
    -20 * np.exp(-0.2 * R)
    + 20
    + np.exp(0.5)
    - np.exp(0.5 * (np.cos(2 * np.pi * X) + np.cos(2 * np.pi * Y)))
)


norm = mpl.colors.Normalize(-abs(Z).max(), abs(Z).max())  # 确定映射数据范围
# 布局设置
def title_and_lablim(ax, title):  # 常规坐标轴特性设置，可通用
    ax.set_title(title)
    ax.set_xlabel("$x$", fontsize=16)
    ax.set_ylabel("$y$", fontsize=16)
    ax.set_zlabel("$z$", fontsize=16)
    ax.set_xlim(-5, 5.1)
    ax.set_ylim(-5, 5.1)
    ax.set_xticks(np.arange(-5, 5.1, 1))
    ax.set_yticks(np.arange(-5, 5.1, 1))


fig = plt.figure()
ax = plt.subplot(131, projection="3d")
p = ax.plot_surface(
    X,
    Y,
    Z,
    rstride=1,
    cstride=1,
    linewidth=0,
    antialiased=False,
    norm=norm,
    cmap=mpl.cm.copper,
)
# ax.contour(X, Y, Z, zdir='z', offset=0, norm=norm, cmap=mpl.cm.copper)
fig.colorbar(p, ax=ax, shrink=0.8)
title_and_lablim(ax, "plot_surface+z_contour")

ax = plt.subplot(132, projection="3d")
p = ax.plot_wireframe(
    X, Y, Z, rstride=5, cstride=5, norm=norm, cmap=mpl.cm.RdBu, lw=0.5
)
ax.contour(X, Y, Z, zdir="z", offset=0, norm=norm, cmap=mpl.cm.RdBu)
title_and_lablim(ax, "plot_wireframe+z_contour")

ax = plt.subplot(133, projection="3d")
ax.contour(X, Y, Z, zdir="z", offset=0, norm=norm, cmap=mpl.cm.Blues)
ax.contour(X, Y, Z, zdir="y", offset=5, norm=norm, cmap=mpl.cm.copper)
ax.contour(X, Y, Z, zdir="x", offset=-5, norm=norm, cmap="Purples")
title_and_lablim(ax, "3D_contour")
fig.tight_layout()
fig.savefig("ch2-38-3D_draw.png", dpi=400)

plt.show()
