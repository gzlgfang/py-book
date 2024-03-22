# PSO_para_id


from tkinter import font
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_bvp
import scipy.interpolate as spi
from scipy import optimize as op

# 设置刻度线朝内
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 16  # 设置字体大小
# mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
font1 = {"family": "Times New Roman"}


def PSO(fitness, N, c1, c2, w, M, D):
    """
    c1 学习因子1
    c2 学习因子2
    w 惯性权重
    M 最大迭代次数
    D 搜索空间维数
    N 初始化群体个体数目
    """
    # 初始化种群的个体
    x = np.random.rand(N, D)  # 本题初始k值
    v = np.random.rand(N, D)  # 初始速度
    # x[0]=[0.1 ,0.1, 0.1]
    # pi 代表个体极值
    pbest = np.copy(x)  # 个体初始最优位置
    p = np.zeros(N)  # 个体初始最优值
    for i, val in enumerate(x):
        p[i] = fitness(val)  # 计算适应度，即目标函数，计算N个粒子的函数值
    # gbest 全局最优位置
    gbest = x[N - 1]
    for i in range(N - 1):  # 寻找n个粒子函数值最小的粒子位置gbest
        if fitness(x[i]) < fitness(gbest):
            gbest = x[i]
    # 主要循环
    pbest_fit = np.zeros(M)  # 每一次迭代的最优函数值
    for t in range(M):  # 进行M轮迭代
        for i in range(N):
            # momentum + cognition + social
            v[i] = (
                w * v[i]
                + c1 * np.random.random() * (pbest[i] - x[i])
                + c2 * np.random.random() * (gbest - x[i])
            )
            x[i] = x[i] + v[i]
            for j in range(D):
                if x[i, j] < 0:  # 保证变量为非负，需要根据具体求解问题设置
                    x[i, j] = 0
                if x[i, j] > 1:  # 保证变量为非负，需要根据具体求解问题设置
                    x[i, j] = 1
            if fitness(x[i]) < p[i]:  # 更新个体极值
                p[i] = fitness(x[i])
                pbest[i] = x[i]  # pbest[i]为个体最优解
            if p[i] < fitness(gbest):  # 更新全局极值
                gbest = pbest[i]
        pbest_fit[t] = fitness(gbest)
    # 结束迭代，得到最优解gbest,
    print(f"目标函数取最小值时的自变量 {gbest}")
    print(f"目标函数的最小值为 {fitness(gbest)}")
    plt.figure(num="目标函数与迭代次数关系图")
    for i in range(M - 1):
        plt.plot([i, i + 1], [pbest_fit[i], pbest_fit[i + 1]], lw=2, c="b")
        plt.grid()
    plt.xlabel("迭代次数")
    plt.ylabel("目标函数值")
    # 根据求得的最优参数，求解微分方程，得到浓度分布
    tspan = np.linspace(0, 5, 11)  # 确定自变量范围
    C_tspan = np.zeros((4, tspan.size))  # 确定4个应变量初值
    # 定义微分方程,注意和程序08-bc_ode中的不同，自变量t放在前面
    def dC(t, C):  # 注意和ode定义方程dy(y,t)的不同
        k1 = gbest[0]
        k2 = gbest[1]
        k3 = gbest[2]
        CA, CB, CC, CD = C[0], C[1], C[2], C[3]
        dC1 = -k1 * CA
        dC2 = k1 * CA - k2 * CB + k3 * CC**2 * CD
        dC3 = 2 * k2 * CB - 2 * k3 * CC**2 * CD
        dC4 = k2 * CB - k3 * CC**2 * CD
        return np.vstack((dC1, dC2, dC3, dC4))

    # 定义边界条件
    def BC(ya, yb):
        return np.array([ya[0] - 10, ya[1] - 0, ya[2] - 0, ya[3] - 0])

    sol = solve_bvp(dC, BC, tspan, C_tspan)
    CA_C = sol.sol(tspan)[0]
    CB_C = sol.sol(tspan)[1]
    CC_C = sol.sol(tspan)[2]
    CD_C = sol.sol(tspan)[3]
    C = sol.sol(tspan)
    # 辨识拟合曲线
    plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    plt.plot(tspan, C[0, :], label=r"$C_A$", color="red", linewidth=2, linestyle="-")
    plt.plot(
        tspan, C[1, :], label=r"$C_B$", color="green", linewidth=2.0, linestyle="--"
    )
    # plt.plot(tspan, C[2,:], label=r"$λ_1$",color="b", linewidth=2, linestyle="-")
    # plt.plot(tspan, C[3,:], label=r"$λ_2$",color="k", linewidth=2, linestyle="-")
    plt.plot(tspan, C[2, :], label=r"$C_C$", color="b", linewidth=2, linestyle="-.")
    plt.plot(tspan, C[3, :], label=r"$C_D$", color="k", linewidth=2, linestyle="-.")
    # 实验数据点
    plt.scatter(tspan, CA_E, s=70, c="r", marker="*", alpha=0.6)
    plt.scatter(tspan, CB_E, s=70, c="g", marker="h", alpha=0.6)
    plt.scatter(tspan, CC_E, s=70, c="b", marker="<", alpha=0.6)
    plt.scatter(tspan, CD_E, s=70, c="k", marker=">", alpha=0.6)
    k11 = int(gbest[0] * 1000 + 0.5) / 1000
    k22 = int(gbest[1] * 1000 + 0.5) / 1000
    k33 = int(gbest[2] * 1000 + 0.5) / 1000
    plt.text(3, 9, r"$\mathrm{k_{1}=}$" + str(k11), color="blue", fontsize=24)
    plt.text(3, 8, r"$\mathrm{k_{2}=}$" + str(k22), color="blue", fontsize=24)
    plt.text(3, 7, r"$\mathrm{k_{3}=}$" + str(k33), color="blue", fontsize=24)

    plt.xticks(np.linspace(0, 5, 11, endpoint=True))  # 设置横轴刻度
    plt.xlim(0, 5)  # 设置x轴的上下限
    plt.xlabel(r"$\mathrm{time,min}$", color="blue", size=28)  # 设置x轴描述信息
    plt.ylabel(r"$\mathrm{C_{A},C_{B},C_{C},C_{D}}$", color="red")  #
    plt.yticks(np.linspace(0, 10, 11, endpoint=True))  # 设置纵轴刻度
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.ylim(0, 10)
    plt.legend()
    plt.grid(True)
    plt.title("浓度随反应时间关系图")


# 定义自适应度函数
def fitness(kx):
    tspan = np.linspace(0, 5, 11)  # 确定自变量范围
    C_tspan = np.zeros((4, tspan.size))  # 确定4个应变量初值
    # 定义微分方程,注意和程序08-bc_ode中的不同，自变量t放在前面
    def dC(t, C):  #
        k1 = kx[0]
        k2 = kx[1]
        k3 = kx[2]
        CA, CB, CC, CD = C[0], C[1], C[2], C[3]
        dC1 = -k1 * CA
        dC2 = k1 * CA - k2 * CB + k3 * CC**2 * CD
        dC3 = 2 * k2 * CB - 2 * k3 * CC**2 * CD
        dC4 = k2 * CB - k3 * CC**2 * CD
        return np.vstack((dC1, dC2, dC3, dC4))

    # 定义边界条件
    def BC(ya, yb):
        return np.array([ya[0] - 10, ya[1] - 0, ya[2] - 0, ya[3] - 0])

    sol = solve_bvp(dC, BC, tspan, C_tspan)
    CA_C = sol.sol(tspan)[0]
    CB_C = sol.sol(tspan)[1]
    CC_C = sol.sol(tspan)[2]
    CD_C = sol.sol(tspan)[3]
    fit = 0
    for i in range(len(CA_E)):
        fit = (
            fit
            + (CA_C[i] - CA_E[i]) ** 2
            + (CB_C[i] - CB_E[i]) ** 2
            + (CC_C[i] - CC_E[i]) ** 2
            + (CD_C[i] - CD_E[i]) ** 2
        )
    fit1 = (
        sum((CA_C - CA_E) ** 2)
        + sum((CB_C - CB_E) ** 2)
        + sum((CC_C - CC_E) ** 2)
        + sum((CD_C - CD_E) ** 2)
    )
    ##两种计算自适应度的方法均可以
    return fit1


# 已知数据
CA_E = np.array(
    [10, 9.048, 8.187, 7.408, 6.703, 6.065, 5.488, 4.965, 4.493, 4.065, 3.678]
)
CB_E = np.array(
    [0, 0.882, 1.559, 2.076, 2.497, 2.892, 3.298, 3.708, 4.104, 4.475, 4.816]
)
CC_E = np.array([0, 0.138, 0.506, 1.03, 1.598, 2.084, 2.426, 2.65, 2.802, 2.916, 3.008])
CD_E = np.array(
    [0, 0.069, 0.253, 0.515, 0.799, 1.042, 1.213, 1.325, 1.401, 1.458, 1.504]
)

PSO(fitness, 50, 1.5, 2.5, 0.5, 30, 3)  # 调用总程序
plt.show()
