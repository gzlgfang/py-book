# 03-odeint.py
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# 设置刻度线朝内
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 24  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细


def dy(y, x):  # 注意是参数y在前面
    # ddy =y**2*np.cos(x)
    ddy = np.cos(x)
    # ddy=np.cos(6*x)+0.8*np.sin(6*x)
    return ddy


x = np.arange(0, 10.55, 0.01)  # 确定自变量范围
y0 = 0  # 确定初始状态
result = odeint(dy, y0, x)
ddy = dy(result[:], x[:])
print(ddy)
# for i in range(int(len(x)/2)):
# print(f"x={2*(i+1)*0.05:.2f},y={result[2*(i+1)-1,0]:.5f}")
print(result.T)
plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(x, result[:], label="y", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(x, ddy[:], label="dy/dx", color="green", linewidth=2.0, linestyle="--")
plt.xticks()
ymin = [min(result[:]), min(ddy[:])]
ymax = [max(result[:]), max(ddy[:])]
plt.ylim(min(ymin) - 1, max(ymax) + 1)  # 设置纵轴的上下限
plt.xlabel("x", color="blue")  # 设置x轴描述信息
plt.ylabel("y,dy", color="red")  # 设置y轴描述信息
plt.yticks()  # 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.savefig("g:\\odeint_03.png", dpi=72)  # 以分辨率 72 来保存图片
plt.show()  # 在屏幕上显示
