# 06-react_fit
from scipy import optimize as op
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def func(x, a0, a1, a2):
    return a0 + a1 * x[0] ** 0.6 + a2 * x[1] ** 1.3


x = np.array([[280, 320, 350, 280, 320, 350, 280, 320], [5, 5, 5, 10, 10, 10, 15, 15]])
y_real = np.array([43.67, 45.63, 47.04, 61.45, 63.41, 64.82, 82.2, 84.2])
fit_cc, fit_cv = op.curve_fit(func, x, y_real)  # 拟合曲线curvefit方法
print(f"a_0={fit_cc[0]:.5f},a_1={fit_cc[1]:.5f}, a_2={fit_cc[2]:.5f}")
# print("fit_cv=", fit_cv)=func(x, *fit_cc)-y_real

ydata = z = func(x, *fit_cc)
# 计算绝对百分误差平均值
print("ydata=", ydata)

abseer = np.mean(abs(y_real - ydata) / ydata) * 100
print("abseer=", f"{abseer:.5f}", "%")


# 图形绘制
from mpl_toolkits.mplot3d import Axes3D

# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 16
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
fig = plt.figure()
# 指定图形类型是 3d 类型
ax = fig.add_subplot(projection="3d")
# 构造数据
x = np.array([280, 320, 350, 280, 320, 350, 280, 320])
y = np.array([5, 5, 5, 10, 10, 10, 15, 15])

# Plot the line and scatter
ax.scatter(x, y, z, s=58, color="red", label="实验数据")
ax.plot(x, y, z, color="b", lw=2, label="拟合数据")
ax.text(310, 10, 50, f"abseer={abseer:.5f}%", zdir="x")
ax.text(
    310,
    5,
    50,
    f"a$_0$={fit_cc[0]:.5f}, a$_1$={fit_cc[1]:.5f}, a$_2$={fit_cc[2]:.5f}",
    zdir="x",
)

ax.set_xlabel("$T$", fontsize=16)
ax.set_ylabel("$W$", fontsize=16)
ax.set_zlabel("$β$", fontsize=16)
plt.legend()
plt.show()
