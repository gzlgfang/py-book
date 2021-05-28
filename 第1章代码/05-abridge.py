import matplotlib.pyplot as plt  # 缩写导入次级库
import numpy as np  # 缩写导入主库
import matplotlib  # 导入主库
x = np.linspace(-3 * np.pi, 3 * np.pi, 300)
y1 = 2 * np.sin(x)
y2 = np.cos(2 * x)**2
fig, ax = plt.subplots()  # 设置画布及布局
matplotlib.pyplot.plot(x, y1, color="blue", label="y1(x)", lw=2)
#plt.plot(x, y1, color="blue", label="y1(x)")
plt.plot(x, y2, color="red", label="y2(x)", linestyle='-.')
ax.set_xlabel("x")
ax.set_ylabel("y")  # 设置坐标轴名称
ax.set_xlim(-10, 10)
ax.set_ylim(-3, 3)
plt.grid(True)
plt.legend()  # 显示图例
fig.savefig("g:/pybook/05-abridge.png", dpi=100)
plt.show()  # 显示图形，此句要放在保存语句后面
