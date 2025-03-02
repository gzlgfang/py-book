# 04-Mar_ equation
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, bisect, newton, brentq, brenth

global a2, a3, a4, a5, b2, b3, b5, bv, c2, c3, c5, tc
a2 = -4391473.1
a3 = 233734790.0
a4 = -8196792900.0
a5 = 113229830000.0
b2 = 4501.7239
b3 = -102972.05
b5 = 74758927.0
bv = 20.101853
c2 = -60767617.0
c3 = 5081973600.0
c5 = -3229376000000.0
tc = 304.2


def f(x):
    return p - (
        82.06 * t / (x - bv)
        + (a2 + b2 * t + c2 * math.exp(-5 * t / tc)) / (x - bv) ** 2
        + (a3 + b3 * t + c3 * math.exp(-5 * t / tc)) / (x - bv) ** 3
        + a4 / (x - bv) ** 4
        + (a5 + b5 * t + c5 * math.exp(-5 * t / tc)) / (x - bv) ** 5
    )


p = 1
t = 423.15
print(f"V(p=1,t=423.15)={brentq(f,22,100000):.3f}")


v = np.zeros((6, 41))
for i in range(6):
    t = 333.15 + i * 40
    for j in range(41):
        p = 10 + 5 * j
        v[i, j] = brentq(f, 22, 100000)
        print(t, p, v[i, j])
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False
mpl.rcParams["font.size"] = 16  # 设置字体大小
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
mpl.rcParams["ytick.direction"] = "in"
font1 = {"family": "Times New Roman"}
p = np.linspace(10, 210, 41)
for i in range(6):
    tt = str(333.15 + i * 40) + "°C"
    y = v[i, :]
    plt.plot(p, y, lw=2, label=tt)
plt.xlim(10, 210)
plt.ylim(0, 4500)
plt.xticks(np.arange(10, 210, 10))
plt.xlabel("p,atm", font1)
plt.ylabel(r"$V,1×10^{-6}m^{3}.mol^{-1}$", font1)
plt.legend()
plt.grid()
plt.show()
