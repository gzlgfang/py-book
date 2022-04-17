import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as op
from scipy.integrate import odeint
from fipy.tools import numerix
import fipy as fp
from fipy import (
        CellVariable,
        Grid2D,
        Viewer,
        TransientTerm,
        DiffusionTerm,
        ImplicitSourceTerm,
        PowerLawConvectionTerm,
)
from fipy.tools import numerix
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 12  # 设置字体大小
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
mpl.rcParams["ytick.direction"] = "in"
font1 = {"family": "Times New Roman"}
st.sidebar.write("常微分及偏微分方程求解导航栏")
add_selectbox = st.sidebar.radio(
    "", ("一次微分方程1", "一次微分方程2", "高阶微分方程", "两应变量微分方程组", "四应变量微分方程组", "偏微分方程1", "偏微分方程2")
)
if add_selectbox == "一次微分方程1":
    st.latex("微分方程:f(x)=a_0+ a_1*cos(b_0x)+a_2*sin(b_1x)+a_3x^{b_2}")
    st.write("参数设置:")
    col1, col2, col3 = st.columns(3)
    with col1:
        a0 = st.number_input("a0", value=1.0, step=0.001, format="%f")
    with col2:
        a1 = st.number_input("a1", value=1.0, step=0.001, format="%f")
    with col3:
        a2 = st.number_input("a2", value=1.0, step=0.001, format="%f")
    col1, col2, col3 = st.columns(3)
    with col1:
        a3 = st.number_input("a3", value=0.0, step=0.001, format="%f")
    with col2:
        b0 = st.number_input("b0", value=1.0, step=0.001, format="%f")
    with col3:
        b1 = st.number_input("b1", value=1.0, step=0.001, format="%f")
    b2 = st.number_input("b2", value=1.0, step=0.001, format="%f")
    st.write("初始条件:")
    col1, col2 = st.columns(2)
    with col1:
        x_s = st.number_input("起点x_s", value=0.0, step=0.01, format="%f")
    with col2:
        y0 = st.number_input("初值y0", value=0.0, step=0.01, format="%f")
    col1, col2 = st.columns(2)
    with col1:
        x_e = st.number_input("终点x_e", value=10.0, step=0.01, format="%f")
    with col2:
        n = st.number_input("计算点数n+1", value=100, step=1, format="%i")

    # 定义微分方程
    def dy(y, x):  # 注意是参数y在前面
        ddy = a0 + a1 * np.cos(b0 * x) + a2 * np.sin(b1 * x) + a3 * x**b2
        return ddy

    # 微分方程求解
    x = np.linspace(x_s, x_e, n + 1)  # 确定自变量范围
    # x = np.arange(0, 10.55, 0.01)  # 确定自变量范围
    sol = odeint(dy, y0, x)
    ddy = dy(sol, x)
    fig = plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    plt.plot(x, sol[:], label="y", color="red", linewidth=2, linestyle="-")
    plt.plot(x, ddy[:], label="dy/dx", color="green", linewidth=2.0, linestyle="--")
    plt.xticks()
    ymin = [min(sol[:]), min(ddy[:])]
    ymax = [max(sol[:]), max(ddy[:])]
    plt.ylim(min(ymin) - 1, max(ymax) + 1)  # 设置纵轴的上下限
    plt.xlabel("x", color="blue")  # 设置x轴描述信息
    plt.ylabel("y,dy", color="red")  # 设置y轴描述信息
    plt.yticks()  # 设置纵轴刻度
    plt.legend()
    plt.grid(True)
    st.pyplot(fig)


elif add_selectbox == "一次微分方程2":

    st.latex("微分方程:f(x)=a_0*e^{a_1*(y-a_2)}*(y-a_3)^{a_4}")
    st.write("参数设置:")
    col1, col2, col3 = st.columns(3)
    with col1:
        a0 = st.number_input("a0", value=-0.03, step=0.001, format="%f")
    with col2:
        a1 = st.number_input("a1", value=0.0015, step=0.001, format="%f")
    with col3:
        a2 = st.number_input("a2", value=300.0, step=0.001, format="%f")

    col1, col2 = st.columns(2)
    with col1:
        a3 = st.number_input("a3", value=300.0, step=0.001, format="%f")
    with col2:
        a4 = st.number_input("a4", value=0.85, step=0.001, format="%f")

    st.write("初始条件:")
    col1, col2 = st.columns(2)
    with col1:
        x_s = st.number_input("起点x_s", value=0.0, step=0.01, format="%f")
    with col2:
        y0 = st.number_input("初值y0", value=2000.0, step=0.01, format="%f")
    col1, col2 = st.columns(2)
    with col1:
        x_e = st.number_input("终点x_e", value=400.0, step=0.01, format="%f")
    with col2:
        n = st.number_input("计算点数n+1", value=1000, step=1, format="%i")

    # 定义微分方程
    def dy(y, x):  # 注意是参数y在前面
        ddy = a0 * np.exp(a1 * (y - a2)) * (y - a3) ** a4
        return ddy

    # 微分方程求解
    x = np.linspace(x_s, x_e, n + 1)  # 确定自变量范围
    sol = odeint(dy, y0, x)
    ddy = dy(sol, x)
    fig = plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    plt.plot(x, sol[:], label="y", color="red", linewidth=2, linestyle="-")
    plt.plot(x, ddy[:], label="dy/dx", color="green", linewidth=2.0, linestyle="--")
    plt.xticks()
    ymin = [min(sol[:]), min(ddy[:])]
    ymax = [max(sol[:]), max(ddy[:])]
    plt.ylim(min(ymin) - 1, max(ymax) + 1)  # 设置纵轴的上下限
    plt.xlabel("x", color="blue")  # 设置x轴描述信息
    plt.ylabel("y,dy", color="red")  # 设置y轴描述信息
    plt.yticks()  # 设置纵轴刻度
    plt.legend()
    plt.grid(True)
    st.pyplot(fig)

elif add_selectbox == "高阶微分方程":
    st.latex("微分方程: d^{2}y/dx^{2}=a_0+ a_1*sin(b_0x)+a_2*x^{b_1}")
    st.latex("+a_3*y^{b_2}+c_0*e^{c_1y}+c_2*dy/dx+d_0*e^{d_1x}")
    st.write("参数设置:")
    col1, col2, col3 = st.columns(3)
    with col1:
        a0 = st.number_input("a0", value=0.0, step=0.001, format="%f")
    with col2:
        a1 = st.number_input("a1", value=2.0, step=0.001, format="%f")
    with col3:
        a2 = st.number_input("a2", value=0.0, step=0.001, format="%f")

    col1, col2, col3 = st.columns(3)
    with col1:
        a3 = st.number_input("a3", value=0.0, step=0.001, format="%f")
    with col2:
        b0 = st.number_input("b0", value=1.0, step=0.001, format="%f")
    with col3:
        b1 = st.number_input("b1", value=1.0, step=0.001, format="%f")

    col1, col2, col3 = st.columns(3)
    with col1:
        b2 = st.number_input("b2", value=1.0, step=0.001, format="%f")
    with col2:
        c0 = st.number_input("c0", value=0.0, step=0.001, format="%f")
    with col3:
        c1 = st.number_input("c1", value=-1.0, step=0.001, format="%f")
    col1, col2, col3 = st.columns(3)
    with col1:
        c2 = st.number_input("c2", value=0.0, step=0.001, format="%f")
    with col2:
        d0 = st.number_input("d0", value=0.0, step=0.0001, format="%f")
    with col3:
        d1 = st.number_input("d1", value=-1.0, step=0.001, format="%f")
    st.write("初始条件:")
    col1, col2, col3 = st.columns(3)
    with col1:
        x_s = st.number_input("起点x_s", value=0.0, step=0.01, format="%f")
    with col2:
        ys0 = st.number_input("初值ys0", value=0.0, step=0.01, format="%f")
    with col3:
        ys1 = st.number_input("dy/dx初值ys1", value=1.0, step=0.01, format="%f")
    col1, col2 = st.columns(2)
    with col1:
        x_e = st.number_input("终点x_e", value=10.0, step=0.01, format="%f")
    with col2:
        n = st.number_input("计算点数n+1", value=100, step=1, format="%d")

    def dy(y, x):
        y1, y2 = y[0], y[1]
        dy1 = y2
        # dy2 = 5 * np.sin(t) - 2 * np.cos(t) * t * np.exp(0.001 * y1)
        dy2 = (
            a0
            + a1 * np.sin(b0 * x)
            + a2 * x**b1
            + a3 * y1**b2
            + c0 * np.exp(c1 * y1)
            + c2 * y2
            + d0 * np.exp(d1 * x)
        )
        return [dy1, dy2]

    y0 = [ys0, ys1]  # 确定初始状态
    tspan = np.linspace(x_s, x_e, n + 1)  # 确定自变量范围
    sol = odeint(dy, y0, tspan)
    x = tspan
    y1 = sol[:, 0]
    y2 = sol[:, 1]
    ddy = (
        a0
        + a1 * np.sin(b0 * x)
        + a2 * x**b1
        + a3 * y1**b2
        + c0 * np.exp(c1 * y1)
        + c2 * y2
        + d0 * np.exp(d1 * x)
    )
    # print(ddy)
    fig = plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    # 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
    plt.plot(tspan, sol[:, 0], label="y", color="red", linewidth=2, linestyle="-")
    # 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
    plt.plot(tspan, sol[:, 1], label="dy", color="green", linewidth=2.0, linestyle="--")
    plt.plot(tspan, ddy, label="ddy", color="blue", linewidth=2.0, linestyle="-.")
    plt.xticks()
    plt.xlabel("x", font1, color="blue")  # 设置x轴描述信息
    plt.ylabel("y,dy,ddy", color="red")  # 设置y轴描述信息
    plt.yticks()  # 设置纵轴刻度
    plt.legend()
    plt.grid(True)
    st.pyplot(fig)
elif add_selectbox == "两应变量微分方程组":
    st.latex("微分方程u: dy_1/dx=a_0*y_1(1-y_1/a_1)-a_2*y_1y_2")
    st.latex("微分方程v: dy_2/dx=b_0*y_2(1-y_2/b_1)-b_2*y_1y_2")
    st.write("参数设置:")
    col1, col2, col3 = st.columns(3)
    with col1:
        a0 = st.number_input("a0", value=0.1, step=0.01, format="%f")
    with col2:
        a1 = st.number_input("a1", value=20.0, step=0.01, format="%f")
    with col3:
        a2 = st.number_input("a2", value=0.35, step=0.01, format="%f")

    col1, col2, col3 = st.columns(3)
    with col1:
        b0 = st.number_input("b0", value=0.05, step=0.001, format="%f")
    with col2:
        b1 = st.number_input("b1", value=15.0, step=0.001, format="%f")
    with col3:
        b2 = st.number_input("b2", value=0.15, step=0.001, format="%f")

    st.write("初始条件:")
    col1, col2, col3 = st.columns(3)
    with col1:
        x_s = st.number_input("起点x_s", value=0.0, step=0.01, format="%f")
    with col2:
        y10 = st.number_input("初值y10", value=1.6, step=0.01, format="%f")
    with col3:
        y20 = st.number_input("初值y20", value=1.2, step=0.01, format="%f")
    col1, col2 = st.columns(2)
    with col1:
        x_e = st.number_input("终点x_e", value=300.0, step=0.01, format="%f")
    with col2:
        n = st.number_input("计算点数n+1", value=300, step=1, format="%d")

    def dy(y, t):
        y1, y2 = y[0], y[1]
        dy1 = a0 * y1 * (1 - y1 / a1) - a2 * y1 * y2
        dy2 = b0 * y2 * (1 - y2 / b1) - b2 * y1 * y2
        return [dy1, dy2]

    y0 = [y10, y20]  # 确定初始状态
    tspan = np.linspace(x_s, x_e, n + 1)  # 确定自变量范围
    sol = odeint(dy, y0, tspan)
    fig = plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    # 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
    plt.plot(tspan, sol[:, 0], label="u", color="red", linewidth=2, linestyle="-")
    # 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
    plt.plot(tspan, sol[:, 1], label="v", color="green", linewidth=2.0, linestyle="--")
    plt.xticks()  # 设置横轴刻度
    plt.xlim(x_s, x_e)  # 设置x轴的上下限
    # plt.ylim(0,1.6)
    plt.xlabel("时间", color="blue")  # 设置x轴描述信息
    plt.ylabel("物种数量，(u，v)", color="red")  # 设置y轴描述信息
    plt.yticks()  # 设置纵轴刻度
    plt.legend()
    plt.grid(True)
    st.pyplot(fig)


elif add_selectbox == "四应变量微分方程组":
    st.latex("微分方程1: dy_1/dx=-(k_1+k_2)*y_1")
    st.latex("微分方程2: dy_2/dx=k_1*y_1-k_3y_2")
    st.latex("微分方程3: dy_3/dx=k_2*y_1-k_4y_3")
    st.latex("微分方程4: dy_4/dx=k_3*y_2+k_4y_3")

    R = 8.31434  # 气体常数 kJ/kmol.K
    st.write("输入4个阿累乌尼斯常数， 1/s")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        k1 = st.number_input("k1", value=1.2e10, step=0.1e10, format="%e")
    with col2:
        k2 = st.number_input("k2", value=2.8e10, step=0.1e8, format="%e")
    with col3:
        k3 = st.number_input("k3", value=1.8e5, step=0.1e5, format="%e")
    with col4:
        k4 = st.number_input("k4", value=3.2e7, step=0.1e7, format="%e")
    st.write("输入4个活化能数据，kJ/kmo")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        E1 = st.number_input("E1", value=1.3e5, step=0.1e5, format="%e")
    with col2:
        E2 = st.number_input("E2", value=1.6e5, step=0.1e5, format="%e")
    with col3:
        E3 = st.number_input("E3", value=8.0e4, step=0.1e4, format="%e")
    with col4:
        E4 = st.number_input("E4", value=1.2e5, step=0.1e5, format="%e")
    st.write("输入4个物质初值浓度", r"$c,kmol/m^{3}$")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        C_A = st.number_input("C_A", value=2.0, step=0.01, format="%f")
    with col2:
        C_B = st.number_input("C_B", value=0.0, step=0.01, format="%f")
    with col3:
        C_C = st.number_input("C_C", value=0.0, step=0.01, format="%f")
    with col4:
        C_D = st.number_input("C_D", value=0.0, step=0.01, format="%f")
    k0 = np.array([k1, k2, k3, k4])  #% 阿累乌尼斯常数, 1/s
    E = np.array([E1, E2, E3, E4])  # ;% 活化能, kJ/kmol
    # 反应速率常数, 1/s
    T = 230 + 273.15
    # global k
    k = k0 * np.exp(-E / (R * T))  # ;

    def dy(y, t):
        y1, y2, y3, y4 = y[0], y[1], y[2], y[3]
        dy1 = -(k[0] + k[1]) * y1
        dy2 = k[0] * y1 - k[2] * y2
        dy3 = k[1] * y1 - k[3] * y3
        dy4 = k[2] * y2 + k[3] * y3
        return [dy1, dy2, dy3, dy4]

    y0 = [C_A, C_B, C_C, C_D]  # 确定初始状态
    tspan = np.linspace(0, 30000, 30001)  # 确定自变量范围
    cbmax = []
    timemax = []
    temper = []
    for i in range(50):
        T = 181 + i + 273.15
        k = k0 * np.exp(-E / (R * T))  # ;
        sol = odeint(dy, y0, tspan)
        MAX_C_B = max(sol[:, 1])  # 确定最大值
        time1 = list(sol[:, 1]).index(MAX_C_B)  # 确定最大值所在的位置
        # time1=(sol[:,1]).index(MAX_C_B)#sol[:,1]为numpy.ndarray
        cbmax.append(MAX_C_B)
        timemax.append(time1)
        temper.append(T)
    fig1 = plt.figure(figsize=(8, 6), dpi=80)
    plt.plot(
        temper, cbmax, label="$maxc_{B}$", color="green", linewidth=3.0, linestyle="-"
    )
    plt.legend()
    plt.grid(True)
    plt.xlabel("反应温度，T(K)")
    plt.ylabel("物质B浓度，" + "$c_{B}$")
    plt.xticks()
    plt.yticks()
    st.pyplot(fig1)

    fig2 = plt.figure(figsize=(8, 6), dpi=80)
    plt.plot(
        temper, timemax, label="opt—time", color="green", linewidth=3.0, linestyle="-"
    )
    plt.legend()
    plt.grid(True)
    plt.xlabel("反应温度,T(K)")
    plt.ylabel("物质B浓度最大时反应时间,s")
    plt.xticks()
    plt.yticks()
    st.pyplot(fig2)

    fig3 = plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    plt.plot(
        tspan, sol[:, 0], label=r"$c_{A}$", color="red", linewidth=3, linestyle="-"
    )
    plt.plot(
        tspan, sol[:, 1], label="$c_{B}$", color="green", linewidth=3.0, linestyle="-."
    )
    plt.plot(
        tspan, sol[:, 2], label="$c_{C}$", color="b", linewidth=3.0, linestyle="--"
    )
    plt.plot(tspan, sol[:, 3], label="$c_{D}$", color="k", linewidth=3.0, linestyle=":")

    plt.annotate(
        f"最高点{MAX_C_B:.5f}",
        xy=(time1, MAX_C_B),
        xytext=(time1 + 1400, MAX_C_B + 0.2),
        arrowprops=dict(arrowstyle="->", color="r", lw=2.5),
    )
    plt.xlim(0, 30000)
    plt.xticks()  # 设置横轴刻度
    plt.xlabel("时间t,s", color="blue")  # 设置x轴描述信息
    plt.ylabel("浓度" + r"$c,kmol/m^{3}$", color="red")  # 设置y轴描述信息
    plt.yticks()  # 设置纵轴刻度
    plt.legend()
    plt.grid(True)
    st.pyplot(fig3)

elif add_selectbox == "偏微分方程1":
    st.latex("偏微分方程:∂u/∂t=D(∂^{2}u/∂x^{2}+∂^{2}u/∂y^{2})+αu+C_1∂u/∂x+C_2∂u/∂y")
    st.write("输入偏微分方程4个参数")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        D = st.number_input("D", value=10.0, step=0.1, format="%f")
    with col2:
        alpha = st.number_input("α", value=8.0, step=0.1, format="%f")
    with col3:
        C1 = st.number_input("C1", value=10.0, step=0.1, format="%f")
    with col4:
        C2 = st.number_input("C2", value=1.0, step=0.1, format="%f")
    eq = TransientTerm() == DiffusionTerm(coeff=D) + ImplicitSourceTerm(
        alpha
    ) + PowerLawConvectionTerm((C1, C2))

    st.write("输入初始条件及边界约束")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        value = st.number_input("初值", value=0.0, step=0.1, format="%f")
    with col2:
        V_TL = st.number_input("左顶端边界值", value=30.0, step=0.1, format="%f")
    with col3:
        V_BR = st.number_input("一半右底端边界值", value=100.0, step=0.1, format="%f")
    with col4:
        steps = st.number_input("步长0.01时的计算步数", value=10, step=1, format="%d")

    nx = 200
    ny = nx
    dx = 0.01
    dy = dx
    L = dx * nx
    mesh = Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)
    phi = CellVariable(name="u值求解结果", mesh=mesh, value=value)

    valueTopLeft = V_TL
    valueBottomRight = V_BR
    X, Y = mesh.faceCenters
    facesTopLeft = (mesh.facesLeft & (Y >= 0)) | (mesh.facesTop & (X <= L))
    facesBottomRight = (mesh.facesRight & (Y <= L)) | (mesh.facesBottom & (X >= L / 2))
    phi.constrain(valueTopLeft, facesTopLeft)
    phi.constrain(valueBottomRight, facesBottomRight)

    timeStepDuration = 0.01
    # 10 * 0.9 * dx**2 / (2 * D)
    steps = steps
    num = "D=" + str(D) + ",alpha=" + str(alpha) + ",t=" + str(steps * timeStepDuration)
    # from builtins import range
    for step in range(steps):
        eq.solve(var=phi, dt=timeStepDuration)

    arr = np.zeros(len(phi))
    for i in range(len(phi)):
        arr[i] = phi[i]
    ar = arr.reshape(nx, nx)
    # print(ar)
    x = np.arange(nx) * dx  # 长度位置，归一处理，从0开始，共101个点
    y = np.arange(nx) * dy
    X, Y = np.meshgrid(x, y)

    norm = mpl.colors.Normalize(0, max(V_BR, V_TL))
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))  # 布局设置
    p = ax.pcolor(X, Y, ar, cmap=mpl.cm.jet, norm=norm, shading="auto")  # pcolor绘制
    cb = plt.colorbar(p, ax=ax)
    cb.set_label("应变量u值")
    ax.set_title(num + "时不同位置求解结果变化色图")
    font1 = {"family": "Times New Roman"}
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2])  # 设置纵轴刻度
    plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2])
    ax.set_xlabel("x", font1)
    ax.set_ylabel("y", font1)
    st.pyplot(fig)


elif add_selectbox == "偏微分方程2":
    # from fipy import (
    #     CellVariable,
    #     Grid2D,
    #     Viewer,
    #     TransientTerm,
    #     DiffusionTerm,
    #     ImplicitSourceTerm,
    #     PowerLawConvectionTerm,
    # )
    

    st.latex("偏微分方程:∂u/∂t=D(∂^{2}u/∂x^{2}+∂^{2}u/∂y^{2}+∂^{2}u/∂z^{2})+αu+C_1∂u/∂x+C_2∂u/∂y")
    st.write("输入偏微分方程4个参数")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        D = st.number_input("D", value=10.0, step=0.1, format="%f")
    with col2:
        alpha = st.number_input("α", value=8.0, step=0.1, format="%f")
    with col3:
        C1 = st.number_input("C1", value=10.0, step=0.1, format="%f")
    with col4:
        C2 = st.number_input("C2", value=1.0, step=0.1, format="%f")
    eq = TransientTerm() == DiffusionTerm(coeff=D) + ImplicitSourceTerm(
        alpha
    ) + PowerLawConvectionTerm((C1, C2))

    st.write("输入初始条件及边界约束")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        value = st.number_input("初值", value=0.0, step=0.1, format="%f")
    with col2:
        V_TL = st.number_input("左顶端边界值", value=30.0, step=0.1, format="%f")
    with col3:
        V_BR = st.number_input("一半右底端边界值", value=100.0, step=0.1, format="%f")
    with col4:
        steps = st.number_input("步长0.01时的计算步数", value=10, step=1, format="%d")

    nx = 10
    ny = nx
    nz = nx
    dx = 0.1
    dy = dx
    dz = dx
    L = dx * nx
    # mesh = Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)
    mesh = fp.Grid3D(dx=dx, dy=dy, dz=dz, nx=nx, ny=ny, nz=nz)

    u = fp.CellVariable(name="solution variable", mesh=mesh, value=value)
    D = D
    # eq =DiffusionTerm(coeff=D)==0
    # TransientTerm()
    alpha = alpha
    eq = fp.TransientTerm() == fp.DiffusionTerm(coeff=D) + fp.ImplicitSourceTerm(alpha)
    valueTopLeft = V_TL
    valueBottomRight = V_BR
    X, Y, Z = mesh.faceCenters
    facesTopLeft = (mesh.facesLeft & (Y > 0)) | (mesh.facesTop & (X < L))
    facesBottomRight = (mesh.facesRight & (Y <= L)) | (mesh.facesBottom & (X >= L / 2))
    u.constrain(valueTopLeft, facesTopLeft)
    u.constrain(valueBottomRight, facesBottomRight)
    timeStepDuration =0.001
    #  10 * 0.9 * dx**2 / (2 * D)
    steps = steps
    for step in range(steps):
        eq.solve(var=u, dt=timeStepDuration)
        # print(u)
        # print(type(phi),len(phi))
    arr = np.zeros(len(u))
    for i in range(len(u)):
        arr[i] = u[i]
    arr1 = list(arr)
    b = arr1.reverse()
    arr = np.array(arr1)
    ar = arr.reshape(nx, ny, nz)
    x = np.arange(nx) * dx  # 长度位置，归一处理，从0开始，共101个点
    y = np.arange(ny) * dy

    X, Y = np.meshgrid(x, y)
    #norm = mpl.colors.Normalize(30, 100)
    norm = mpl.colors.Normalize(0, max(V_BR, V_TL))
    for i in range(1, 9, 4):
        # for i in range(nz):
        c = ar[:, :, i]
        fig2 = plt.figure()
        ax = plt.subplot(111, projection="3d")
        p = ax.plot_surface(
            X,
            Y,
            c,
            rstride=1,
            cstride=1,
            linewidth=0,
            antialiased=False,
            norm=norm,
            cmap=mpl.cm.jet,
        )
        # ax.contour(X, Y, z, zdir='z', offset=0, norm=norm, cmap=mpl.cm.copper)
        ax.set_xlabel("x", font1)
        ax.set_ylabel("y", font1)
        fig2.colorbar(p, ax=ax, shrink=0.8)
        st.pyplot(fig2)

    z = np.arange(nz) * dz
    X1, Y1, Z1 = np.meshgrid(x, y, z)
    fig3 = plt.figure()
    ax = plt.subplot(111, projection="3d")
    # p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, norm=norm, cmap=mpl.cm.jet)
    p = ax.scatter(
        X1, Y1, Z1, s=250, c=ar, cmap=mpl.cm.jet, marker="o", zdir="z", norm=norm
    )
    ax.set_xlabel("x", font1)
    ax.set_ylabel("y", font1)
    ax.set_zlabel("z", font1)
    fig3.colorbar(p, ax=ax, shrink=0.8)
    st.pyplot(fig3)
