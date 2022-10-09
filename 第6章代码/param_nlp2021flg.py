# nlp2021flg
from scipy import optimize as op
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as scp
from scipy.integrate import odeint

# k0 = [0.01  0.01 ];         % 参数初值
lb = [0, 0]  # 参数下限
ub = [100, 100]  # 参数上限

CC1 = np.array(
    [
        [0, 7.311, 1.884, 0, 0],
        [1, 6.965, 1.386, 0.346, 0.497],
        [2, 6.719, 1.029, 0.592, 0.855],
        [3, 6.542, 0.769, 0.769, 1.115],
        [4, 6.412, 0.577, 0.899, 1.307],
        [5, 6.317, 0.434, 0.994, 1.449],
        [6, 6.245, 0.328, 1.066, 1.556],
        [7, 6.192, 0.248, 1.119, 1.636],
        [8, 6.152, 0.187, 1.159, 1.696],
    ]
)
C1 = CC1[:, 1:5]
CO1 = CC1[0, 1:5]
CC2 = np.array(
    [
        [0, 6.982, 2.273, 0, 0],
        [1, 6.582, 1.691, 0.399, 0.582],
        [2, 6.299, 1.27, 0.682, 1.002],
        [3, 6.093, 0.961, 0.888, 1.311],
        [4, 5.942, 0.731, 1.04, 1.541],
        [5, 5.829, 0.558, 1.153, 1.714],
        [6, 5.744, 0.428, 1.238, 1.845],
        [7, 5.679, 0.328, 1.302, 1.944],
        [8, 5.63, 0.252, 1.351, 2.02],
    ]
)
C2 = CC2[:, 1:5]
CO2 = CC2[0, 1:5]
CC3 = np.array(
    [
        [0, 6.593, 2.642, 0, 0],
        [1, 6.154, 1.989, 0.438, 0.652],
        [2, 5.842, 1.514, 0.751, 1.127],
        [3, 5.614, 1.162, 0.979, 1.479],
        [4, 5.444, 0.897, 1.148, 1.744],
        [5, 5.316, 0.696, 1.276, 1.946],
        [6, 5.219, 0.541, 1.373, 2.1],
        [7, 5.145, 0.422, 1.448, 2.219],
        [8, 5.087, 0.33, 1.505, 2.311],
    ]
)
C3 = CC3[:, 1:5]
CO3 = CC3[0, 1:5]
tspan = CC1[:, 0]
# 定义反应微分方程组：
def dy(y, t, k1, k2):
    CA, CB, CC, CD = y[0], y[1], y[2], y[3]
    dCA = -k2 * CA * CB
    dCB = -k1 * CB - k2 * CA * CB
    dCD = k1 * CB + k2 * CA * CB
    dCC = k2 * CA * CB
    dC = [dCA, dCB, dCC, dCD]
    return dC


# 定义数据偏差平方和,可以直接和目标函数合并
def J(k1, k2):
    y0 = CO1
    JJ1 = sum(sum((odeint(dy, y0, tspan, args=(k1, k2)) - C1) ** 2))
    y0 = CO2
    JJ2 = sum(sum((odeint(dy, y0, tspan, args=(k1, k2)) - C2) ** 2))
    y0 = CO3
    JJ3 = sum(sum((odeint(dy, y0, tspan, args=(k1, k2)) - C3) ** 2))
    JJ = JJ1 + JJ2 + JJ3
    return JJ


# 定义优化函数
def fun(x):
    k1, k2 = x[0], x[1]
    y0 = CO1
    JJ1 = sum(sum((odeint(dy, y0, tspan, args=(k1, k2)) - C1) ** 2))
    y0 = CO2
    JJ2 = sum(sum((odeint(dy, y0, tspan, args=(k1, k2)) - C2) ** 2))
    y0 = CO3
    JJ3 = sum(sum((odeint(dy, y0, tspan, args=(k1, k2)) - C3) ** 2))
    JJ = JJ1 + JJ2 + JJ3
    # sum = J(k1, k2)  ##目标函数和偏差平方和单独定义时用
    return JJ


k0 = np.array([0.01, 0.01])
res = op.minimize(fun, k0, method="L-BFGS-B", bounds=[(0.01, 10), (0.01, 10)])
k = res.x
j = res.fun

print(f'优化目标=",{j:.5f}')
print(f"辨识参数:k_1={k[0]:.5f}, k_2={k[1]:.5f}")
# tspan1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# tspan1 = tspan
k1, k2 = k[0], k[1]

# 打印辨识参数计算的微分方程解
y0 = CO1
ca_C1 = odeint(dy, y0, tspan, args=(k1, k2))
print(ca_C1)
y0 = CO2
ca_C2 = odeint(dy, y0, tspan, args=(k1, k2))
print(ca_C2)
y0 = CO3
ca_C3 = odeint(dy, y0, tspan, args=(k1, k2))
print(ca_C3)

# 图形绘制
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
plt.scatter(tspan, C1[:, 0], s=58, color="red", label="实验数据C$_A$", clip_on=False)
plt.scatter(tspan, C1[:, 1], s=58, color="b", label="实验数据C$_B$", clip_on=False)
plt.scatter(tspan, C1[:, 2], s=58, color="purple", label="实验数据C$_C$", clip_on=False)
plt.scatter(tspan, C1[:, 3], s=58, color="pink", label="实验数据C$_D$", clip_on=False)

plt.plot(tspan, ca_C1[:, 0], color="red", lw=2, label="拟合数据C$_A$")
plt.plot(tspan, ca_C1[:, 1], color="b", lw=2, label="拟合数据C$_B$")
plt.plot(tspan, ca_C1[:, 2], color="purple", lw=2, label="拟合数据C$_C$")
plt.plot(tspan, ca_C1[:, 3], color="pink", lw=2, label="拟合数据C$_D$")
y0 = CO1
JJ1 = sum(sum((odeint(dy, y0, tspan, args=(k1, k2)) - C1) ** 2))
plt.text(2, 5, f"abseer={JJ1*100:.5f}%")
plt.text(2, 3, f"k$_1$={k[0]:.5f}, k$_2$={k[1]:.5f}")
plt.xlabel("$t$，时间 (h)", fontsize=16)
plt.ylabel("$C$,浓度 (kmol/m$^3$)", fontsize=16, labelpad=8)
plt.grid(which="both", axis="both", color="r", linestyle=":", linewidth=1)
plt.title("第一组实验数据点和拟合计算曲线")
plt.xlim(0, 8)  # 设置x轴范围
plt.ylim(0, 10)
plt.legend()


fig = plt.figure()
plt.scatter(tspan, C2[:, 0], s=58, color="red", label="实验数据C$_A$", clip_on=False)
plt.scatter(tspan, C2[:, 1], s=58, color="b", label="实验数据C$_B$", clip_on=False)
plt.scatter(tspan, C2[:, 2], s=58, color="purple", label="实验数据C$_C$", clip_on=False)
plt.scatter(tspan, C2[:, 3], s=58, color="pink", label="实验数据C$_D$", clip_on=False)

plt.plot(tspan, ca_C2[:, 0], color="red", lw=2, label="拟合数据C$_A$")
plt.plot(tspan, ca_C2[:, 1], color="b", lw=2, label="拟合数据C$_B$")
plt.plot(tspan, ca_C2[:, 2], color="purple", lw=2, label="拟合数据C$_C$")
plt.plot(tspan, ca_C2[:, 3], color="pink", lw=2, label="拟合数据C$_D$")

y0 = CO2
JJ2 = sum(sum((odeint(dy, y0, tspan, args=(k1, k2)) - C2) ** 2))
plt.text(2, 5, f"abseer={JJ2*100:.5f}%")
plt.text(2, 3, f"k$_1$={k[0]:.5f}, k$_2$={k[1]:.5f}")
plt.xlabel("$t$，时间 (h)", fontsize=16)
plt.ylabel("$C$,浓度 (kmol/m$^3$)", fontsize=16, labelpad=8)
plt.grid(which="both", axis="both", color="r", linestyle=":", linewidth=1)
plt.title("第二组实验数据点和拟合计算曲线")
plt.xlim(0, 8)  # 设置x轴范围
plt.ylim(0, 10)
plt.legend()

fig = plt.figure()
plt.scatter(tspan, C3[:, 0], s=58, color="red", label="实验数据C$_A$", clip_on=False)
plt.scatter(tspan, C3[:, 1], s=58, color="b", label="实验数据C$_B$", clip_on=False)
plt.scatter(tspan, C3[:, 2], s=58, color="purple", label="实验数据C$_C$", clip_on=False)
plt.scatter(tspan, C3[:, 3], s=58, color="pink", label="实验数据C$_D$", clip_on=False)

plt.plot(tspan, ca_C3[:, 0], color="red", lw=2, label="拟合数据C$_A$")
plt.plot(tspan, ca_C3[:, 1], color="b", lw=2, label="拟合数据C$_B$")
plt.plot(tspan, ca_C3[:, 2], color="purple", lw=2, label="拟合数据C$_C$")
plt.plot(tspan, ca_C3[:, 3], color="pink", lw=2, label="拟合数据C$_D$")

y0 = CO3
JJ2 = sum(sum((odeint(dy, y0, tspan, args=(k1, k2)) - C3) ** 2))
plt.text(2, 5, f"abseer={JJ2*100:.5f}%")
plt.text(2, 3, f"k$_1$={k[0]:.5f}, k$_2$={k[1]:.5f}")
plt.xlabel("$t$，时间 (h)", fontsize=16)
plt.ylabel("$C$,浓度 (kmol/m$^3$)", fontsize=16, labelpad=8)
plt.grid(which="both", axis="both", color="r", linestyle=":", linewidth=1)
plt.title("第三组实验数据点和拟合计算曲线")
plt.xlim(0, 8)  # 设置x轴范围
plt.ylim(0, 10)
plt.legend()


plt.show()
