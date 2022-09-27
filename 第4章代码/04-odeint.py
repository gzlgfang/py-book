# 04-odeint.py
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


def dy(y, x):
    ddy = -0.03 * np.exp(0.0015 * (y - 300)) * (y - 300) ** 0.85
    return ddy


x = np.arange(0, 300.1, 0.5)  # 确定自变量范围
y0 = 2000  # 确定初始状态
#条件反转，已知某一时刻，求0时刻
# x = np.arange(300, -0.1, -0.5)  # 确定自变量范围
# y0 = 302.0521  # 确定初始状态

result = odeint(dy, y0, x)
ddy = dy(result[:, 0], x[:])
print(ddy)
# for i in range(int(len(x)/2)):
# print(f"x={2*(i+1)*0.05:.2f},y={result[2*(i+1)-1,0]:.5f}")
print(result.T)
plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(x, result, label="T", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(x, ddy[:], label="dT/dt", color="green", linewidth=2.0, linestyle="--")
plt.xticks(np.linspace(0, 300, 31, endpoint=True))  # 设置横轴刻度
plt.ylim(-400, 2000)  # 设置纵轴的上下限
plt.xlim(min(x[:]), max(x[:]))  # 设置x轴的上下限
plt.xlabel("时间", color="blue")  # 设置x轴描述信息
plt.ylabel("铁球温度", color="red")  # 设置y轴描述信息
plt.yticks(np.linspace(-400, 2000, 25, endpoint=True))  # 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.savefig("g:\\odeint_04.png", dpi=72)  # 以分辨率 72 来保存图片
plt.show()  # 在屏幕上显示
