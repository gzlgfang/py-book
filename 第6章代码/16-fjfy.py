# 用optimize.minimize求解
##发酵反应八参数拟合
from scipy import optimize as op
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as scp
from scipy.integrate import odeint

# 输入数据
C1 = np.array([6.53, 9.38, 19.67, 25.31, 34.66, 40.30, 45.94, 39.48, 33.96])  ##x
C2 = np.array([1.88, 4.73, 12.23, 29.03, 38.39, 54.26, 67.33, 83.20, 95.35])  ##p
C3 = np.array([169.32, 158.68, 136.41, 113.21, 80.25, 48.67, 32.92, 19.02, 9.77])  ##s
C = np.array([C1, C2, C3]).T
# 定义微分方程组
def dy(y, t, um, ks, kx, alpha, beta, yx, yp, ms):
    (y1, y2, y3) = (
        y[0],
        y[1],
        y[2],
    )
    dy1 = (um * y3 / (ks * y1 + y3) - kx) * y1  ###x
    dy2 = alpha * (um * y3 / (ks * y1 + y3) - kx) * y1 + beta * y1  ##p
    dy3 = -(
        ((um * y3 / (ks * y1 + y3) - kx) * y1) / yx
        + (alpha * (um * y3 / (ks * y1 + y3) - kx) * y1 + beta * y1) / yp
        + ms * y1
    )  ##s
    return [dy1, dy2, dy3]


y0 = [6.53, 1.88, 169.32]  # 确定初始状态
tspan = np.linspace(0, 96, 9)  # 确定自变量范围
k0 = np.array([0.05, 1.15, 0.01, 0.3, 0.03, 0.5, 0.9, 0.001])  # 参数初值
##定义优化目标函数，目的求该目标函数最小值是对应的变量值
def fun(x):
    um, ks, kx, alpha, beta, yx, yp, ms = x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]
    # sum=J(um, ks, kx, alpha, beta, yx, yp, ms)
    JJ = sum(
        sum(
            (odeint(dy, y0, tspan, args=(um, ks, kx, alpha, beta, yx, yp, ms)) - C) ** 2
        )
    )  # 先求解微分方程组，再将求解结果和实际数据相减，
    # 将所有差的平方和进行和列的相加，得到一个数值
    return JJ


res = op.minimize(
    fun,
    k0,
    method="L-BFGS-B",
    tol=1e-6,
    bounds=[
        (0.04, 0.08),
        (1, 2.7),
        (0.008, 0.05),
        (0.2, 0.9),
        (0.01, 0.05),
        (0.3, 0.6),
        (0.7, 1.0),
        (0.0001, 0.006),
    ],
)

k = res.x  # 获取参数
j = res.fun  # 获取目标函数值即sum1
print("j=", j)  #
##um,ks, kx, alpha, beta, yx, yp, ms=0.06,1.14,0.0184,0.31,0.028,0.543,0.943,0.002
print(
    f"辨识参数:k_1={k[0]:.5f}, k_2={k[1]:.5f}, k_3={k[2]:.5f},k_4={k[3]:.5f}, k_5={k[4]:.5f}, k_6={k[5]:.5f},k_7={k[6]:.5f}, k_8={k[7]:.5f}"
)
###
# 图形绘制，#全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 20
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否

t = np.linspace(0, 96, 97)
y_data = odeint(
    dy, y0, t, args=(k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7])
)  # 根据辨识参数，重新求解微分方程
fig = plt.figure()
plt.scatter(tspan, C1, s=68, color="red", label="实验数据C$_A$", clip_on=False)
plt.scatter(tspan, C2, s=68, color="b", label="实验数据C$_B$", clip_on=False)
plt.scatter(tspan, C3, s=68, color="purple", label="实验数据C$_B$", clip_on=False)

plt.plot(t, y_data[:, 0], color="red", lw=2, label="拟合数据C$_A$")
plt.plot(t, y_data[:, 1], color="b", lw=2, label="拟合数据C$_B$")
plt.plot(t, y_data[:, 2], color="purple", lw=2, label="拟合数据C$_C$")

plt.text(45, 130, f"abseer={j:.4f}")
plt.text(45, 145, f"k$_1$={k[0]:.4f}, k$_2$={k[1]:.4f}, k$_3$={k[2]:.4f}")
plt.text(45, 160, f"k$_4$={k[3]:.4f}, k$_5$={k[4]:.4f}, k$_6$={k[5]:.4f}")
plt.text(45, 175, f"k$_7$={k[6]:.4f}, k$_8$={k[7]:.4f}")
plt.xlabel("$t$，时间 (min)", fontsize=12)
plt.ylabel("$C$,浓度 (kmol/m$^3$)", fontsize=12, labelpad=8)
plt.grid(which="both", axis="both", color="black", linestyle=":", linewidth=1)
plt.legend()
plt.xlim(-10, 108)  # 设置x轴范围
plt.ylim(-30, 190)

fig2 = plt.figure()  ##文献参数计算图像及数据
um, ks, kx, alpha, beta, yx, yp, ms = (
    0.06,
    1.14,
    0.0184,
    0.31,
    0.028,
    0.543,
    0.943,
    0.002,
)
t = np.linspace(0, 96, 97)
y_data = odeint(dy, y0, t, args=(um, ks, kx, alpha, beta, yx, yp, ms))
# JJ_wx = sum(sum((odeint(dy, y0, t, args=(um, ks, kx, alpha, beta, yx, yp, ms)) - C) ** 2) # 先求解微分方程组，再将求解结果和实际数据相减，
# 将所有差的平方和进行和列的相加，得到一个数值


n = len(C1)
JJ_wx = 0
for i in range(n):
    JJ_wx = (
        JJ_wx
        + (C1[i] - y_data[i * 12, 0]) ** 2
        + (C2[i] - y_data[i * 12, 1]) ** 2
        + (C3[i] - y_data[i * 12, 2]) ** 2
    )
print("JJ_wx=", JJ_wx)

plt.text(45, 130, f"abseer={JJ_wx:.4f}")

plt.scatter(tspan, C1, s=68, color="red", label="实验数据C$_A$", clip_on=False)
plt.scatter(tspan, C2, s=68, color="b", label="实验数据C$_B$", clip_on=False)
plt.scatter(tspan, C3, s=68, color="purple", label="实验数据C$_B$", clip_on=False)

plt.plot(t, y_data[:, 0], color="red", lw=2, label="文献拟合数据C$_A$")
plt.plot(t, y_data[:, 1], color="b", lw=2, label="文献拟合数据C$_B$")
plt.plot(t, y_data[:, 2], color="purple", lw=2, label="文献拟合数据C$_C$")


plt.legend()
# plt.grid(False)
plt.show()
