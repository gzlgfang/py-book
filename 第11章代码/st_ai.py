import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as op
import pandas as pd
import random as rnd
from scipy import optimize
import copy
from numpy.core.fromnumeric import cumsum

# streamlit run g:\st-app\st_ai.py
# https://share.streamlit.io/gzlgfang/st-apps/main/st_ai.py
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 8  # 设置字体大小
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
mpl.rcParams["ytick.direction"] = "in"
font1 = {"family": "Times New Roman"}
st.set_option("deprecation.showPyplotGlobalUse", False)
st.sidebar.write("智能算法实际应用导航栏")
add_selectbox = st.sidebar.radio(
    "", ("遗传算法求解TSP问题", "遗传算法求解背包问题", "模拟退火算法求解最优邮路", "粒子算法求解三变量实数方程组", "蚁群算法求解TSP问题")
)
if add_selectbox == "遗传算法求解TSP问题":
    # st.latex("\sum_{i=1}^{n}")
    st.latex("min J=\sum_{i=1}^{n}d_{i,i+1}+d_{n,1},i=1,2,...n-1")
    st.write("设置基本遗传数据:")
    col1, col2, col3 = st.columns(3)
    with col1:
        ZQS = st.number_input("种群大小", value=200, step=1, format="%d")
    with col2:
        Maxgen = st.number_input("最大遗传代数", value=200, step=1, format="%d")
    with col3:
        Pc = st.number_input("交叉概率", value=0.6, step=0.1, format="%f")
    col1, col2, col3 = st.columns(3)
    with col1:
        Pm = st.number_input("变异概率", value=0.2, step=0.1, format="%f")
    with col2:
        Sel_ra = st.number_input("选择率", value=0.7, step=0.1, format="%f")
    with col3:
        B = st.number_input("是否回起点,是1,否0", value=1, step=1, format="%d")

    # 产生随机城市坐标city_zb
    def city_zb(width, hight, city_num):
        """
        width:城市配置平面图宽度
        hight:城市配置平面图高度
        city_num:配置城市数目
        """
        city_zb = np.zeros((city_num, 2))
        for i in range(city_num):
            city_zb[i, 0] = int(np.random.random() * width * 100) / 100
            city_zb[i, 1] = int(np.random.random() * hight * 100) / 100
        return city_zb

    city_num = st.number_input("输入随机城市数目，随机计算时使用", value=15, step=1, format="%d")
    st.write("加载具体路径的数据文件csv,三列结构，第一列城市名称，第二列为x坐标，第三列为y坐标；如不加载则利用随机数据进行计算", value="")
    # 读入城市坐标
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        array_d = np.array(dataframe)
        # 共有31个城市坐标
        city_x = array_d[:, 1]  # 数据分配
        city_y = array_d[:, 2]
        n = len(city_x)  # 计算城市的数目
        city_zb = np.zeros((n, 2))  # 设置坐标数组
        city_zb[:, 0] = city_x / 100
        city_zb[:, 1] = city_y / 100
    else:
        city_zb = city_zb(50, 50, city_num)
        n = city_num

    # 计算坐标起始范围：
    x_min = min(city_zb[:, 0])
    x_max = max(city_zb[:, 0])
    y_min = min(city_zb[:, 1])
    y_max = max(city_zb[:, 1])

    # 计算城市i和城市j之间的距离
    # 输入 city_zb 各城市的坐标,用city_zb[i,0:1])
    # 输出 D 城市i和城市j之间的距离,用D[i,j]表示
    def Distance(city_zb):
        n = len(city_zb)
        D = np.zeros((n, n))  #  产生两城市之间距离数据的空矩阵即零阵
        for i in range(n):
            for j in range(i + 1, n):
                # D[i,j]=city_zb[i,0]
                D[i, j] = (
                    (city_zb[i, 0] - city_zb[j, 0]) ** 2
                    + (city_zb[i, 1] - city_zb[j, 1]) ** 2
                ) ** 0.5
                D[j, i] = D[i, j]
        # D[0, 14] = D[14, 0] = 10000000  # 0-14之间有障碍物
        # D[29, 30] = D[30, 29] = 1000000
        return D

    D = Distance(city_zb)  # 计算一次即可
    # 设置基本遗传数据
    ZQS = ZQS  # 种群大小
    Maxgen = Maxgen  # 最大遗传代数
    Pc = Pc  # 交叉概率
    Pm = Pm  # 变异概率
    Sel_ra = Sel_ra  # 选择率

    # 产生随机路径path，一般调用一次即可
    # 输入种群数ZQS及城市数目N
    def path(ZQS, N):
        li = np.arange(0, N)
        LJ = np.zeros((ZQS, N))
        for i in range(ZQS):
            rnd.shuffle(li)
            # li=np.random.randint(N,size=N)
            LJ[i, :] = li
        return LJ.astype(int)  # 需要强制转变成整数

    LJ = path(ZQS, n)

    def drawpath(LJ, city_zb, num):
        fig, ax = plt.subplots(num=num)
        # fig=plt.figure(num=num)
        n = len(LJ)
        ax.scatter(
            city_zb[:, 0], city_zb[:, 1], marker="o", color="b", s=100
        )  # 所有城市位置上画上o
        ax.text(city_zb[LJ[0], 0] + 0.5, city_zb[LJ[0], 1] + 0.5, "start")
        ax.text(city_zb[LJ[n - 1], 0] + 0.5, city_zb[LJ[n - 1], 1] + 0.5, "end")
        for i in range(n):
            # plt.text(city_zb[LJ[i],0]-0.3,city_zb[LJ[i],1]+0.5,str(i+1),color="r")
            ax.text(city_zb[i, 0] - 0.3, city_zb[i, 1] + 0.5, str(i + 1), color="r")
        # 绘线
        xy = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
        xytext = (city_zb[LJ[1], 0], city_zb[LJ[1], 1])
        ax.annotate(
            "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="g", lw=2)
        )
        for i in range(1, n - 1):
            xy = [city_zb[LJ[i], 0], city_zb[LJ[i], 1]]
            xytext = [city_zb[LJ[i + 1], 0], city_zb[LJ[i + 1], 1]]
            ax.annotate(
                "",
                xy=xy,
                xytext=xytext,
                arrowprops=dict(arrowstyle="<-", color="g", lw=2),
            )
        # 无需回起点时，下面3行代码不要程序
        if B == 1:
            xy = (city_zb[LJ[n - 1], 0], city_zb[LJ[n - 1], 1])
            xytext = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
            ax.annotate(
                "",
                xy=xy,
                xytext=xytext,
                arrowprops=dict(arrowstyle="<-", color="g", lw=1),
            )

        plt.ylim(y_min - 2, y_max + 2)
        plt.xlim(x_min - 2, x_max + 2)
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Trajectory Map")

    # 计算路径总距离
    def pathlength(D, LJ):
        N = D.shape[1]
        ZQS = LJ.shape[0]
        p_len = np.zeros(ZQS)
        for i in range(ZQS):
            for j in range(N - 1):
                p_len[i] = p_len[i] + D[LJ[i, j], LJ[i, j + 1]]
            # 无需回起点时，下面1行代码不要
            if B == 1:
                p_len[i] = p_len[i] + D[LJ[i, N - 1], LJ[i, 0]]
        return p_len

    p_len = pathlength(D, LJ)
    # 计算适应度值fitness 归一化处理
    def fit(p_len):
        ZQS = len(p_len)
        fitnv = np.ones(ZQS)
        fitnv[:] = 1 / p_len[:]
        max = np.max(fitnv)
        min = np.min(fitnv)
        fitnv[:] = (fitnv[:] - min) / (max - min)
        return fitnv

    # 绘制初始优化图
    index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号
    # print(index)
    num = "Draw the initial optimization graph"
    draw_path = drawpath(LJ[index, :], city_zb, num)
    yt = 0.8 * (y_max - y_min - 1) + y_min
    xt1 = 0.65 * (x_max - x_min - 1) + x_min
    xt2 = 0.9 * (x_max - x_min - 1) + x_min
    plt.text(xt1, yt, "Total Length=")
    plt.text(xt2, yt, str(int(1000 * p_len[index]) / 1000))
    st.write("初始优化图")
    st.pyplot(draw_path)
    pre_obj = p_len[index]
    print("初始最优解=", pre_obj)
    # 初始种群优化图
    fitnv = fit(p_len)
    # 选择操作
    def select(LJ, Sel_ra, fitnv):
        ZQS = len(LJ)
        sel_num = int(ZQS * Sel_ra)
        n = 0
        index = []
        flags = True
        while flags:
            for i in range(ZQS):
                pick = rnd.random()
                if pick < 0.8 * fitnv[i]:
                    index.append(i)
                    n = n + 1
                    if n == sel_num:
                        break
            if n == sel_num:
                flags = False
        Sel_LJ = LJ[index]
        return Sel_LJ

    Sel_LJ = select(LJ, Sel_ra, fitnv)
    # 交叉
    def cross(a, b):
        # a和b为两个待交叉的个体
        # 输出：
        # a和b为交叉后得到的两个个体
        n = len(a)  # 城市数目
        flags = True
        while flags:
            r1 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
            r2 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
            if r1 != r2:
                flags = False
        # 保证找到两个不同是整数，可以进行交叉操作
        a0 = np.zeros(n)
        b0 = np.zeros(n)
        a1 = np.zeros(n)
        b1 = np.zeros(n)
        a0[:] = a[:]
        b0[:] = b[:]
        a1[:] = a[:]  # 先保护原数据到a1,b1
        b1[:] = b[:]
        if r1 > r2:
            s, e = r2, r1
        else:
            s, e = r1, r2
        for i in range(s, e + 1):
            a[i] = b0[i]
            b[i] = a0[i]
            # a1,b1=a,b#先保护原数据到a1,b1
            x = [id for id in range(n) if a[id] == a[i]]  # 找到交换后a中重复元素的序号
            y = [id for id in range(n) if b[id] == b[i]]
            # print("i=",x,y)
            id1 = [s1 for k, s1 in enumerate(x) if x[k] != i]  # 找到序号不为i的其他序号
            id2 = [s2 for k, s2 in enumerate(y) if y[k] != i]

            if id1 != []:
                i1 = id1[0]
                a[i1] = a1[i]
                a1[i1] = a[i1]
            if id2 != []:
                i2 = id2[0]
                b[i2] = b1[i]
                b1[i2] = b[i2]
        return [a, b]

    # 交叉重组
    def Re_com(Sel_LJ, Pc):
        n = len(Sel_LJ)
        for i in range(0, n - 1, 2):
            # print(i)
            if Pc >= rnd.random():  #%交叉概率Pc
                [Sel_LJ[i, :], Sel_LJ[i + 1, :]] = cross(Sel_LJ[i, :], Sel_LJ[i + 1, :])
        return Sel_LJ

    Sel_LJ = Re_com(Sel_LJ, Pc)
    # print("NEW=",Sel_LJ)
    # 交叉重组后的最优解
    p_len = pathlength(D, Sel_LJ)
    # fitnv=fit(p_len)
    index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号
    # 变异操作
    # Pm为变异概率
    # Sel_LJ为变异操作前后路径
    def Mutate(Sel_LJ, Pm):
        ZQS, n = Sel_LJ.shape
        Sel_LJ1 = np.copy(Sel_LJ)
        for i in range(ZQS):
            if Pm >= rnd.random():
                r = np.random.randint(n, size=2)
                r.sort()  # 产生2个不相等的0到n-1的整数
                r_min = r[0]
                r_max = r[1]
                Sel_LJ[i, r_min] = Sel_LJ1[i, r_max]
                Sel_LJ[i, r_max] = Sel_LJ1[i, r_min]
        return Sel_LJ

    # print(np.sort(Sel_LJ))
    Sel_LJ = Mutate(Sel_LJ, Pm)  # 变异后的路径
    # 变异后的最优解
    p_len = pathlength(D, Sel_LJ)
    # fitnv=fit(p_len)
    index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号
    # 逆转操作：
    # 全部被选中种子均参加逆转操作
    # 逆转后适应度大的将替换原选择种子
    # 输入种子Sel_LJ及D
    # 输出新的选择集Sel_LJ
    def Reverse(Sel_LJ, D):
        ZQS, n = Sel_LJ.shape
        Sel_LJ = np.array(Sel_LJ)
        p_len = pathlength(D, Sel_LJ)
        Sel_LJ1 = np.copy(Sel_LJ)
        for i in range(ZQS):
            # 换成下面代码，保证不重复
            flags = True
            while flags:
                r1 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
                r2 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
                if r1 != r2:
                    flags = False
            if r1 > r2:
                r_min, r_max = r2, r1
            else:
                r_min, r_max = r1, r2
            if r_min == 0:
                r_min = 1
            Sel_LJ1[i, r_min : r_max + 1] = Sel_LJ[i, r_max : r_min - 1 : -1]
        p_len1 = pathlength(D, Sel_LJ1)
        # %计算路径长度
        index = p_len1 < p_len
        Sel_LJ[index, :] = Sel_LJ1[index, :]
        return Sel_LJ

    Sel_LJ = Reverse(Sel_LJ, D)
    # 逆转后的最优解
    p_len = pathlength(D, Sel_LJ)
    # fitnv=fit(p_len)
    index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号

    # 重新产生新种群
    # 输入原种群LJ
    # 输入经过遗传操作后的优势种群Sel_LJ
    # 输出新的种群LJ1
    def newLJ(LJ, Sel_LJ, D):
        ZQS, n = LJ.shape
        sel_num = len(Sel_LJ)
        p_len = pathlength(D, LJ)
        tem_p = []
        for i, e in enumerate(p_len):
            tem_p.append((i, e))
        z = sorted(tem_p, key=lambda x: x[1])  # 按p_len大小排序
        index = [id[0] for id in z]  # 获得从小到大排序的原p_len数组的序号
        LJ1 = np.copy(LJ)
        LJ1[0 : ZQS - sel_num - 1, :] = LJ[index[0 : ZQS - sel_num - 1], :]
        LJ1[ZQS - sel_num : ZQS, :] = Sel_LJ
        return LJ1

    LJ = newLJ(LJ, Sel_LJ, D)
    # print(LJ)
    # print(np.sort(LJ))
    # 完成第一代遗传优化操作，进入循环操作
    gen = 0  # 遗传代数
    # pre_obj=p_len(index) 为上一轮最优
    # print(gen, pre_obj)
    fig1, ax = plt.subplots(
        num="Optimizing Path Distances and Genetic Algebraic Relationships"
    )
    while gen <= Maxgen:
        p_len = pathlength(D, LJ)  # 计算路径长度
        index = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径序号
        obj = p_len[index]
        ax.plot([gen, gen + 1], [pre_obj, obj], lw=2)
        pre_obj = obj
        # 选择操作
        fitnv = fit(p_len)
        Sel_LJ = select(LJ, Sel_ra, fitnv)  # LJ由上一代带入
        # 交叉重组操作
        Sel_LJ = Re_com(Sel_LJ, Pc)
        # 变异操作
        Sel_LJ = Mutate(Sel_LJ, Pm)
        # 逆转操作
        Sel_LJ = Reverse(Sel_LJ, D)
        # 新种子重组，保证上一轮最优解遗传给下一代
        LJ = newLJ(LJ, Sel_LJ, D)
        gen = gen + 1
    plt.xlabel("Genetic Algebra")
    plt.ylabel("Path Distances")
    plt.title("Optimizing Path Distances and Genetic Algebraic Relationships")
    plt.grid()
    st.pyplot(fig1)
    # 绘制最后最优解，并打印路线图
    # 绘制初始优化图
    num = "Draw the final optimization graph"
    fig2 = drawpath(LJ[index, :], city_zb, num)
    yt = 0.8 * (y_max - y_min - 1) + y_min
    xt1 = 0.65 * (x_max - x_min - 1) + x_min
    xt2 = 0.9 * (x_max - x_min - 1) + x_min
    plt.text(xt1, yt, "Total Length=")
    plt.text(xt2, yt, str(int(1000 * p_len[index]) / 1000))
    st.write("Draw the final optimization graph")
    st.pyplot(fig2)
    st.write("Print the final optimized path")
    # 打印最终优化路径
    print_LJ = str()
    for i in range(n):
        print_LJ = print_LJ + str(LJ[index, i] + 1) + "-->"
    if B == 1:
        print_LJ = print_LJ + str(LJ[index, 0] + 1)
    st.write(print_LJ)

elif add_selectbox == "遗传算法求解背包问题":
    st.write("目标函数:")
    st.latex("max J=\sum_{i=1}^{n}v_i*x_i,i=1,2,...n,x_i=1  if put  m_i  else x_i=0")
    st.write("设置基本遗传数据:")
    col1, col2, col3 = st.columns(3)
    with col1:
        ZQS = st.number_input("种群大小", value=200, step=1, format="%d")
    with col2:
        Maxgen = st.number_input("最大遗传代数", value=300, step=1, format="%d")
    with col3:
        Pc = st.number_input("交叉概率", value=0.8, step=0.1, format="%f")
    col1, col2, col3 = st.columns(3)
    with col1:
        Pm = st.number_input("变异概率", value=0.3, step=0.1, format="%f")
    with col2:
        Sel_ra = st.number_input("选择率", value=0.8, step=0.1, format="%f")
    with col3:
        M = st.number_input("包中可以放入的总重量", value=1000.0, step=1.0, format="%f")
    ZQS = ZQS  # 种群大小
    Maxgen = Maxgen  # 最大遗传代数
    Pc = Pc  # 交叉概率
    Pm = Pm  # 变异概率
    Sel_ra = Sel_ra  # 选择率
    M = M  # 背包中可以放入的总重量
    num = st.number_input("包中可能放入物品的总件数", value=30, step=1, format="%d")

    def mass_value(num):
        """
        num:物体数目
        """
        m_v = np.zeros((2, num))
        for i in range(num):
            m_v[0, i] = int(np.random.random() * 50) + 1  # 产生0-100的随机整数
            m_v[1, i] = int(np.random.random() * 100) + 1
        return m_v

    put_files = st.text_input("输入具体物品的重量及价值的数据文件,如为空则利用随机数据进行计算", value="")
    if put_files == "":
        m_v = mass_value(num)  # 确定物体数目、重量和及价值
        n = num
        m = m_v[0, :]
        v = m_v[1, :]
        # st.write(m,v)
    else:
        # 读入物品重量及价值数据
        DF = pd.read_excel(put_files, "Sheet1", na_filter=False, index_col=0)  # 共有n个物品
        m = np.array(DF["m"])  # 数据分配
        v = np.array(DF["v"])
        n = len(m)  # 计算物品的数目
    # 定义背包是否放入物品0-1数组，0代表不放入，1代表放入
    def put_array(n):
        x = np.zeros(n)
        for i in range(n):
            if np.random.random() >= 0.5:
                x[i] = 1
        return x

    x = put_array(n)
    # 计算背包中放入的总重量
    def total_mass(x, m):
        T_mass = sum(x * m)
        return T_mass

    # 计算背包中放入的总价值
    def total_value(x, m):
        T_value = sum(x * v)
        return T_value

    def array(ZQS, n):
        T_x = np.zeros((ZQS, n))
        for i in range(ZQS):
            T_x[i, :] = put_array(n)
        return T_x

    T_x = array(ZQS, n)
    # 计算种群全部个体的放入背包的总重量GM
    def gene_mass(T_x, m):
        ZQS = T_x.shape[0]
        GM = np.zeros(ZQS)
        for i in range(ZQS):
            GM[i] = total_mass(T_x[i, :], m)
        return GM

    # 计算种群全部个体的放入背包的总价值GV
    def gene_value(T_x, v):
        ZQS = T_x.shape[0]
        GV = np.zeros(ZQS)
        for i in range(ZQS):
            GV[i] = total_mass(T_x[i, :], v)
        return GV

    # 计算适应度值fitness 归一化处理
    def fit(GM, GV, M):
        ZQS = len(GM)
        fitnv = np.ones(ZQS)
        for i in range(ZQS):
            if GM[i] > M:
                GV[i] = -i
        fitnv[:] = GV[:]
        max = np.max(fitnv)
        min = np.min(fitnv)
        fitnv[:] = (fitnv[:] - min) / (max - min)
        return fitnv

    def draw_T_x(T_x, GM, GV, index, num):
        plt.figure(num=num)
        n = T_x.shape[1]
        x = np.arange(1, n + 1)
        y = T_x[index]
        plt.scatter(
            x, y, s=100, c="red", cmap=mpl.cm.RdYlBu, clip_on=False
        )  # clip_on=False表示坐标轴上的Mark也要整体显示
        plt.plot(x, y, lw=2)
        plt.xticks(np.arange(0, n + 1, 1))
        plt.yticks([0, 1])
        # plt.xticks(np.arange(0,n+1,1),position='top')
        plt.tick_params(top="on", right="on", which="both", direction="in")
        plt.xlabel("Object Number,n")
        plt.ylabel("Put logical numbers in the package")
        plt.text(
            n / 2,
            0.6,
            f"The total weight of the loaded items GM(index)={GM[index]:.1f}",
            c="b",
        )
        plt.text(
            n / 2,
            0.5,
            f"The total value of the item put in GV(index)={GV[index]:.1f}",
            c="b",
        )
        plt.title("Logical data graph")
        plt.xlim(0, n)
        plt.grid(c="green", ls="-.")

    # 打印初始优化结果图
    GM = gene_mass(T_x, m)
    GV = gene_value(T_x, v)
    fitnv = fit(GM, GV, M)
    index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
    pre_obj = GV[index]
    num = "Initial optimization result graph"
    # draw_T_x(T_x, GM, GV, index, num)
    # 开始遗传算法核心代码
    # 选择操作
    LJ = T_x

    def select(LJ, Sel_ra, fitnv):
        ZQS = len(LJ)
        sel_num = int(ZQS * Sel_ra)
        n = 0
        index = []
        flags = True
        while flags:
            for i in range(ZQS):
                pick = rnd.random()
                if pick < fitnv[i]:
                    index.append(i)
                    n = n + 1
                    if n == sel_num:
                        break
            if n == sel_num:
                flags = False
        Sel_LJ = LJ[index]
        return Sel_LJ

    Sel_LJ = select(LJ, Sel_ra, fitnv)
    # 选择操作后的最优解
    GM = gene_mass(Sel_LJ, m)
    GV = gene_value(Sel_LJ, v)
    fitnv = fit(GM, GV, M)
    index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
    num = "选择操作的最优解图"
    # 交叉
    def cross(a, b):
        # a和b为两个待交叉的个体
        # 输出：
        # a和b为交叉后得到的两个个体
        n = len(a)  # 城市数目
        flags = True
        while flags:
            r1 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
            r2 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
            if r1 != r2:
                flags = False
        # 保证找到两个不同整数，可以进行交叉操作
        a0 = np.zeros(n)
        b0 = np.zeros(n)
        a0[:] = a[:]
        b0[:] = b[:]
        if r1 > r2:
            s, e = r2, r1
        else:
            s, e = r1, r2
        for i in range(s, e + 1):
            a[i] = b0[i]
            b[i] = a0[i]

        return [a, b]

    # 交叉重组
    def Re_com(Sel_LJ, Pc):
        n = len(Sel_LJ)
        for i in range(0, n - 1, 2):
            # print(i)
            if Pc >= rnd.random():  #%交叉概率Pc
                [Sel_LJ[i, :], Sel_LJ[i + 1, :]] = cross(Sel_LJ[i, :], Sel_LJ[i + 1, :])
        return Sel_LJ

    Sel_LJ = Re_com(Sel_LJ, Pc)
    # 交叉重组后的最优解
    GM = gene_mass(Sel_LJ, m)
    GV = gene_value(Sel_LJ, v)
    fitnv = fit(GM, GV, M)
    index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
    num = "交叉重组后的最优解图"
    # Pm为变异概率
    # Sel_LJ为变异操作前后路径,原来0的变成1，原来1的变成0
    def Mutate(Sel_LJ, Pm):
        ZQS, n = Sel_LJ.shape
        for i in range(ZQS):
            if Pm >= rnd.random():
                r = np.random.randint(n, size=4)
                r.sort()  # 产生4个不相等的0到n-1的整数
                r_min = r[0]
                r_mid = r[1]
                r_max = r[2]

                if abs(Sel_LJ[i, r_min] - 1) <= 0.1:
                    Sel_LJ[i, r_min] = 0
                else:
                    Sel_LJ[i, r_min] = 1
                if abs(Sel_LJ[i, r_mid] - 1) <= 0.1:
                    Sel_LJ[i, r_mid] = 0
                else:
                    Sel_LJ[i, r_mid] = 1
                if abs(Sel_LJ[i, r_max] - 1) <= 0.1:
                    Sel_LJ[i, r_max] = 0
                else:
                    Sel_LJ[i, r_max] = 1
                if abs(Sel_LJ[i, r[3]] - 1) <= 0.1:
                    Sel_LJ[i, r[3]] = 0
                else:
                    Sel_LJ[i, r[3]] = 1

        return Sel_LJ

    Sel_LJ = Mutate(Sel_LJ, Pm)  # 变异后的路径
    # 变异后的最优解
    GM = gene_mass(Sel_LJ, m)
    GV = gene_value(Sel_LJ, v)
    fitnv = fit(GM, GV, M)
    index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号

    num = "变异后的最优解"
    # draw_T_x(Sel_LJ, GM, GV, index, num)
    # 逆转操作
    def Reverse(Sel_LJ, m, v, M):
        ZQS, n = Sel_LJ.shape
        Sel_LJ = np.array(Sel_LJ)
        GM = gene_mass(Sel_LJ, m)
        GV = gene_value(Sel_LJ, v)
        fitnv = fit(GM, GV, M)
        Sel_LJ1 = np.copy(Sel_LJ)
        for i in range(ZQS):
            flags = True
            while flags:
                r1 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
                r2 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
                if r1 != r2:
                    flags = False
            if r1 > r2:
                r_min, r_max = r2, r1
            else:
                r_min, r_max = r1, r2
            if r_min == 0:
                r_min = 1
            # print(r_min,r_max)
            Sel_LJ1[i, r_min : r_max + 1] = Sel_LJ[i, r_max : r_min - 1 : -1]
        GM = gene_mass(Sel_LJ1, m)
        GV = gene_value(Sel_LJ1, v)
        fitnv1 = fit(GM, GV, M)
        # p_len1=pathlength(D,Sel_LJ1); # %计算路径长度
        index = fitnv1 > fitnv
        Sel_LJ[index, :] = Sel_LJ1[index, :]
        return Sel_LJ

    Sel_LJ = Reverse(Sel_LJ, m, v, M)
    # 逆转后的最优解
    GM = gene_mass(Sel_LJ, m)
    GV = gene_value(Sel_LJ, v)
    fitnv = fit(GM, GV, M)
    index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
    num = "逆转后的最优解"
    # draw_T_x(Sel_LJ,GM,GV,index,num)
    # 重新产生新种群
    # 输入原种群LJ
    # 输入经过遗传操作后的优势种群Sel_LJ
    # 输出新的种群LJ1
    def newLJ(LJ, Sel_LJ, m, v, M):
        ZQS, n = LJ.shape
        sel_num = len(Sel_LJ)
        GM = gene_mass(LJ, m)
        GV = gene_value(LJ, v)
        fitnv = fit(GM, GV, M)
        tem_p = []
        for i, e in enumerate(fitnv):
            tem_p.append((i, e))
        z = sorted(tem_p, key=lambda x: x[1], reverse=True)  # 按fitnv从大到小排序
        index = [id[0] for id in z]  # 获得从大到小排序的原fitnv数组的序号
        LJ1 = np.copy(LJ)
        LJ1[0 : ZQS - sel_num - 1, :] = LJ[index[0 : ZQS - sel_num - 1], :]
        LJ1[ZQS - sel_num : ZQS, :] = Sel_LJ
        return LJ1

    LJ = newLJ(LJ, Sel_LJ, m, v, M)
    gen = 0  # 遗传代数
    # pre_obj=p_len(index) 为上一轮最优
    # print(gen, pre_obj)
    fig = plt.figure(num="Optimizing Total Value and Genetic Algebraic Relationships")
    while gen <= Maxgen:
        GM = gene_mass(LJ, m)
        GV = gene_value(LJ, v)
        fitnv = fit(GM, GV, M)
        index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
        obj = GV[index]  # 初次遗传操作后的最优解
        plt.plot([gen, gen + 1], [pre_obj, obj], lw=2)
        pre_obj = obj
        # 选择操作
        fitnv = fit(GM, GV, M)
        Sel_LJ = select(LJ, Sel_ra, fitnv)  # LJ由上一代带入
        # 交叉重组操作
        # Sel_LJ=Re_com(Sel_LJ,Pc)
        # 变异操作
        Sel_LJ = Mutate(Sel_LJ, Pm)
        # 逆转操作
        Sel_LJ = Reverse(Sel_LJ, m, v, M)
        # 新种子重组，保证上一轮最优解遗传给下一代
        LJ = newLJ(LJ, Sel_LJ, m, v, M)
        gen = gen + 1
    plt.xlabel("Genetic Algebra")
    plt.ylabel("The total value of the item put in")
    plt.title("Optimizing Total Value and Genetic Algebraic Relationships")
    plt.grid()

    st.pyplot(fig)
    # 绘制最后最优解
    num = "Draw the final optimization graph"
    GM = gene_mass(LJ, m)
    GV = gene_value(LJ, v)
    fitnv = fit(GM, GV, M)
    index = list(fitnv[:]).index(max(fitnv[:]))  # 找到满足约束条件放入背包中价值最大的物体系列序号
    # print(index, GM[index], GV[index])
    # print(LJ[index, :])
    fig2 = draw_T_x(LJ, GM, GV, index, num)
    st.pyplot(fig2)
    st.write("放入背包中的总重量及总价值=", GM[index], GV[index])


elif add_selectbox == "模拟退火算法求解最优邮路":
    st.latex("min J=\sum_{i=1}^{n}w_i*d_{i,i+1}+d_{n,1}")
    st.write("设置基本退火数据:")
    global T00, q, Tend, T0, L, test_num
    col1, col2, col3 = st.columns(3)
    with col1:
        T00 = st.number_input("初始温度T00", value=3800.0, step=1.0, format="%f")
    with col2:
        Tend = st.number_input("最终温度Tend", value=0.001, step=0.0001, format="%f")
    with col3:
        L = st.number_input("链长L", value=300, step=1, format="%d")
    col1, col2, col3 = st.columns(3)
    with col1:
        q = st.number_input("温度下降速率", value=0.93, step=0.01, format="%f")
    with col2:
        test_num = st.number_input("实验次数test_num", value=5, step=1, format="%d")
    with col3:
        post_files = st.text_input("邮局及投递点x,y,w数据,空为随机数", value="")  # g:/Postal.xlsx

    T00 = T00  # 初始温度
    T0 = T00
    Tend = Tend  # 最终温度
    L = L  # 链长，每次稳定温度下优化次数
    q = q  # 温度下降速率
    test_num = test_num

    def fun(x):
        return T0 * q ** x[0] - Tend

    T_num = int(optimize.fsolve(fun, [30]) + 2)  # 计算退火次数
    # 读入城市坐标
    if post_files == "":
        n = 20  # 确定投递点为20个
        city_x = np.zeros(n + 1)
        city_y = np.zeros(n + 1)
        w1 = np.zeros(n + 1)
        for i in range(n + 1):
            city_x[i] = int(np.random.random() * 50) + 1  # 产生0-50的随机整数
            city_y[i] = int(np.random.random() * 50) + 1
            w1[i] = int(np.random.random() * 30) + 1
    else:
        DF = pd.read_excel(post_files, "Sheet1", na_filter=False)  # , index_col=0
        city_x = np.array(DF["x"])  # 数据分配
        city_y = np.array(DF["y"])
        w1 = np.array(DF["w"])
    n = len(city_x) - 1  # 计算投递点的数目
    w = w1[1:]  # 读入每个投递点的投递重量,w1[0]为邮局，无投递重量
    TG = sum(w)
    # print("总邮件重量=",TG)
    city_zb = np.zeros((n + 1, 2))  # 设置坐标空数组
    city_zb[:, 0] = city_x  # city_zb[0, :]为邮局位置坐标
    city_zb[:, 1] = city_y

    opt_JJ = np.zeros(test_num)
    opt_way = np.zeros((test_num, n))
    # 计算两地距离
    def Distance(city_zb):
        n = len(city_x)  # 其实是n+1
        D = np.zeros((n, n))  #  产生两城市之间距离数据的空矩阵即零阵
        for i in range(n):
            for j in range(i + 1, n):
                D[i, j] = (
                    (city_zb[i, 0] - city_zb[j, 0]) ** 2
                    + (city_zb[i, 1] - city_zb[j, 1]) ** 2
                ) ** 0.5
                D[j, i] = D[i, j]
        return D

    D = Distance(city_zb)  # 计算一次即可

    # 定义绘制函数
    def drawpath(LJ, city_zb, num):
        fig, ax = plt.subplots(num=num)
        n = len(LJ)
        print("n=", n)
        ax.scatter(
            city_zb[:, 0], city_zb[:, 1], marker="o", color="b", s=100
        )  # 所有城市位置上画上o
        ax.text(city_zb[0, 0] + 0.5, city_zb[0, 1] + 0.5, "Post")
        ax.text(city_zb[LJ[0], 0] + 0.5, city_zb[LJ[0], 1] + 0.5, "Start")
        ax.text(city_zb[LJ[n - 1], 0] + 0.5, city_zb[LJ[n - 1], 1] + 0.5, "End")

        ax.text(city_zb[0, 0] - 0.3, city_zb[0, 1] + 0.5, str(0), color="r")  # 邮局放置0号
        for i in range(n):  # 0-n-1
            # plt.text(city_zb[LJ[i],0]-0.3,city_zb[LJ[i],1]+0.5,str(i+1),color="r")
            ax.text(
                city_zb[i + 1, 0] - 0.3, city_zb[i + 1, 1] + 0.5, str(i + 1), color="r"
            )
        # 绘线
        xy = (city_zb[0, 0], city_zb[0, 1])
        xytext = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
        ax.annotate(
            "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="r", lw=3)
        )  # 邮局到起点

        for i in range(n - 1):
            # x=[city_zb[LJ[i],0],city_zb[LJ[i+1],0]]
            # y=[city_zb[LJ[i],1],city_zb[LJ[i+1],1]]
            # plt.plot(x,y,lw=2,c="r")
            xy = [city_zb[LJ[i], 0], city_zb[LJ[i], 1]]
            xytext = [city_zb[LJ[i + 1], 0], city_zb[LJ[i + 1], 1]]
            ax.annotate(
                "",
                xy=xy,
                xytext=xytext,
                arrowprops=dict(arrowstyle="<-", color="g", lw=2),
            )

        xy = (city_zb[LJ[n - 1], 0], city_zb[LJ[n - 1], 1])
        xytext = (city_zb[0, 0], city_zb[0, 1])
        ax.annotate(
            "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="r", lw=3)
        )
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(" Trajectory Map")

    # 定义计算目标函数
    def pathlength(D, LJ):
        n = D.shape[1] - 1  # 多了一个邮局
        ZQS = 1
        p_len = np.zeros(ZQS)
        for i in range(ZQS):
            p_len[i] = D[0, LJ[0]] * TG  # 邮局到第一个投递点的距离与总总量之和
            TW = TG
            for j in range(n - 1):
                TW = TW - w[j]
                # TW=1
                p_len[i] = p_len[i] + D[LJ[j], LJ[j + 1]] * TW
            p_len[i] = p_len[i] + D[LJ[n - 1], 0]  # 最后一个投递点返回邮局,无重量
        return p_len

    # p_len = pathlength(D, LJ0)
    # 定义打印路径
    def print_way(LJ):
        print_LJ = str()
        n = len(LJ)
        print_LJ = "邮局Post-->"
        for i in range(n):
            print_LJ = print_LJ + str(LJ[i]) + "-->"
        print_LJ = print_LJ + "邮局Post"
        print(print_LJ)
        return print_LJ

    # 进入模拟退火算法
    def Newpath(LJ):
        # 有原来的旅行轨迹LJ1计算产生新的旅行轨迹LJ2(部分逆转）
        # 输入 LJ1 原来的旅行轨迹，是0到N-1城市的数字排列
        # 输出 LJ2 新的旅行轨迹,逆转扰动
        N = len(LJ)  # 计算城市的数目
        LJ2 = copy.deepcopy(LJ)  # 先将原轨迹全部复制到新轨迹
        flags = True
        while flags:
            r1 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
            r2 = rnd.randint(0, n - 1)  # 随机产生一个0：n-1的整数
            if r1 != r2:
                flags = False
            if r1 > r2:
                r_min, r_max = r2, r1
            else:
                r_min, r_max = r1, r2
            if r_min == 0:
                r_min = 1
            # 轨迹逆转
            LJ2[r_min : r_max + 1] = LJ[r_max : r_min - 1 : -1]
            # 互换位置
            # LJ2[r_min] = LJ[r_max]
            # LJ2[r_max] = LJ[r_min]
        return LJ2

    # 判断新路径是否被采用
    def Metropolis(LJ0, LJ2, D, T):
        Len1 = pathlength(D, LJ0)  # 计算轨迹LJ0路径长度
        Len2 = pathlength(D, LJ2)  # 计算轨迹LJ2路径长度
        dc = Len2 - Len1
        if dc < 0:
            LJ = LJ2
            Len = Len2
        else:
            if np.exp(-dc / T) >= rnd.random():
                LJ = LJ2
                Len = Len2
            else:
                LJ = LJ0
                Len = Len1
        return [LJ, Len]

    for test in range(test_num):
        T0 = T00  # 初始温度,每次实验保证初始温度不变T00

        def path(n):
            li = np.arange(1, n + 1)  # 产生1-n的整数
            LJ = np.zeros(n)
            rnd.shuffle(li)
            LJ[:] = li
            return LJ.astype(int)  # 需要强制转变成整数

        LJ0 = path(n)
        p_len = pathlength(D, LJ0)

        LJ2 = Newpath(LJ0)
        p_len = pathlength(D, LJ2)

        [LJ0, Len] = Metropolis(LJ0, LJ2, D, T0)
        count = 0
        LJ0 = LJ0.astype(int)
        # 初始化设置及函数定义工作完成，进入主程序迭代

        count = 0
        obj = np.zeros(T_num)  # 初始化路径总距离
        obj1 = np.zeros(T_num)
        track = np.zeros((T_num, n))  # 初始化轨迹
        # 迭代
        while T0 > Tend:
            count = count + 1
            tem_LJ = np.zeros((L, n))
            tem_len = np.zeros(L)
            # 进行一次退火需要进行L次新轨迹计算
            for i in range(L):
                LJ2 = Newpath(LJ0)
                # Metropolis 法则判断新解
                [LJ0, Len] = Metropolis(LJ0, LJ2, D, T0)
                tem_LJ[i, :] = LJ0[:].astype(int)  # 临时记录下一路径及路程，在每次退火过程中数据会更新
                tem_len[i] = Len[0]
            # looking for the most short way
            index = list(tem_len[:]).index(min(tem_len[:]))  # 找到最短距离路径序号
            opt_sd = tem_len[index]
            opt_LJ = tem_LJ[index, :]
            obj[count] = opt_sd  # 将计算本次退火操作中最小的路程SD赋值给 obj(count)
            # obj1[count] = opt_sd
            track[count, :] = opt_LJ[:]  # 记录当前温度的最优路径
            LJ0 = opt_LJ.astype(int)
            T0 = q * T0
            if count > 1 and opt_sd > obj[count - 1]:
                LJ0 = track[count - 1, :].astype(
                    int
                )  # 如果本次退火操作最小路程大于上次退火的最小路程, 用上次退火最优轨迹代替本次退火最优轨迹进行新的退火操作
                obj[count] = obj[count - 1]
                track[count, :] = track[count - 1, :]
        # 进行新的退火操作时只需保留到目前为止最优的轨迹
        # 绘制最优路径1
        # print("第" ,(test+1), "次实验最优路径")
        # print_way(LJ0)
        p_len = pathlength(D, LJ0)
        # print("最优目标函数=",p_len[0])

        st.write("第", (test + 1), "次实验最优路径")
        st.write(print_way(LJ0))
        st.write("最优目标函数=", p_len[0])

        opt_JJ[test] = p_len[0]
        opt_way[test, :] = LJ0

    opt_way = opt_way.astype(int)
    # print(opt_way)
    # 寻找全部实验中是最优解：
    # find opt_JJ elements minizmation
    # fmin=min(opt_JJ[:])#确定最小值
    index = list(opt_JJ[:]).index(min(opt_JJ[:]))  # 确定最小值所在的位置
    # print(index)
    # print("全部实验中是最优解")
    # print(opt_JJ[index])
    opt_way = opt_way.astype(int)
    # 最优路径
    # print_way(opt_way[index])
    st.write("全部实验中是最优解")
    st.write(print_way(opt_way[index]))
    st.write("最优目标函数=", opt_JJ[index])

    fig1, ax = plt.subplots(num="实验序号和最优目标函数关系图")
    x = np.arange(1, test_num + 1)
    y = opt_JJ
    ax.scatter(x, y, color="b", marker="o", s=100)
    ax.plot(
        x, y, color="b", label="Objective function value", linewidth=2.0, linestyle="--"
    )
    # plt.xticks(np.linspace(0,test_num,test_num+1,endpoint=True))# 设置横轴刻度
    plt.xlim(1, test_num)  # 设置x轴的上下限
    plt.xlabel("Experiment number", color="blue")  # 设置x轴描述信息
    plt.ylabel("Objective function", color="red")  # 设置y轴描述信息,利用r'$x_1$设置下标1
    plt.legend()
    plt.grid(True)
    st.pyplot(fig1)
    LJ = opt_way[index]
    num = "The optimal path in the sequence experiment"
    fig2 = drawpath(LJ, city_zb, num)
    plt.text(25, 25, "Total Length=")
    plt.text(35, 25, str(int(1000 * opt_JJ[index]) / 1000))
    st.pyplot(fig2)
    st.write("列次计算目标函数平均值=", np.mean(opt_JJ))

elif add_selectbox == "粒子算法求解三变量实数方程组":
    st.write("设置三变量方程:")
    st.latex("a_1x^{a_2}+a_3y^{a_4}+a_5z^{a_6}=1+No/1")
    st.latex("b_1x^{b_2}+b_3y^{b_4}+b_5z^{b_6}=1+No/1")
    st.latex("c_1x^{c_2}+c_3y^{c_4}+c_5z^{c_6}=1+No/1")
    col1, col2, col3 = st.columns(3)
    with col1:
        a1 = st.number_input("a1", value=1.0, step=0.01, format="%f")
    with col2:
        a2 = st.number_input("a2", value=0.5, step=0.01, format="%f")
    with col3:
        a3 = st.number_input("a3", value=1.0, step=0.01, format="%f")
    col1, col2, col3 = st.columns(3)
    with col1:
        a4 = st.number_input("a4", value=1.0, step=0.01, format="%f")
    with col2:
        a5 = st.number_input("a5", value=0.5, step=0.01, format="%f")
    with col3:
        a6 = st.number_input("a6", value=0.9, step=0.01, format="%f")

    col1, col2, col3 = st.columns(3)
    with col1:
        b1 = st.number_input("b1", value=1.0, step=0.01, format="%f")
    with col2:
        b2 = st.number_input("b2", value=0.9, step=0.01, format="%f")
    with col3:
        b3 = st.number_input("b3", value=1.2, step=0.01, format="%f")
    col1, col2, col3 = st.columns(3)
    with col1:
        b4 = st.number_input("b4", value=0.8, step=0.01, format="%f")
    with col2:
        b5 = st.number_input("b5", value=1.0, step=0.01, format="%f")
    with col3:
        b6 = st.number_input("b6", value=1.6, step=0.01, format="%f")

    col1, col2, col3 = st.columns(3)
    with col1:
        c1 = st.number_input("c1", value=0.9, step=0.01, format="%f")
    with col2:
        c2 = st.number_input("c2", value=0.8, step=0.01, format="%f")
    with col3:
        c3 = st.number_input("c3", value=1.0, step=0.01, format="%f")
    col1, col2, col3 = st.columns(3)
    with col1:
        c4 = st.number_input("c4", value=0.8, step=0.01, format="%f")
    with col2:
        c5 = st.number_input("c5", value=0.7, step=0.01, format="%f")
    with col3:
        c6 = st.number_input("c6", value=1.5, step=0.01, format="%f")

    st.write("设置粒子算法基本数据:")
    col1, col2, col3 = st.columns(3)
    with col1:
        c1 = st.number_input("学习因子c1", value=1.5, step=0.1, format="%f")
    with col2:
        c2 = st.number_input("学习因子c2", value=2.5, step=0.1, format="%f")
    with col3:
        w = st.number_input("惯性权重w", value=0.5, step=0.1, format="%f")
    col1, col2, col3 = st.columns(3)
    with col1:
        N = st.number_input("初始化群体个体数目N", value=100, step=1, format="%d")
    with col2:
        M = st.number_input("最大迭代次数M", value=200, step=1, format="%d")
    with col3:
        No = st.number_input("方程右边校正数据", value=0, step=1, format="%d")
    # fun1=st.text_input("输入第一个方程：",value="x**2 - 2 * x + y + 1000 * (min(4 - 4 * x**2 - y**2, 0)) ** 2")
    # st.write(fun1)
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
        x = np.random.rand(N, D)  # 初始位置
        v = np.random.rand(N, D)  # 初始速度
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
                if fitness(x[i]) < p[i]:  # 更新个体极值
                    p[i] = fitness(x[i])
                    pbest[i] = x[i]  # pbest[i]为个体最优解
                if p[i] < fitness(gbest):  # 更新全局极值
                    gbest = pbest[i]
            pbest_fit[t] = fitness(gbest)
        # print(f"目标函数取最小值时的自变量 {gbest}")
        # print(f"目标函数的最小值为 {fitness(gbest)}")
        st.write("目标函数取最小值时的自变量:")
        st.write("x=", gbest[0], "  y=", gbest[1], "  z=", gbest[2])
        st.write("目标函数的最小值为", fitness(gbest))
        fig, ax = plt.subplots(
            num="The relationship between the objective function and the number of iterations"
        )
        for i in range(M - 1):
            ax.plot([i, i + 1], [pbest_fit[i], pbest_fit[i + 1]], lw=2, c="b")
            ax.grid()
        plt.xlabel("Number of iterations")
        plt.ylabel("Objective Function Value")
        st.pyplot(fig)

    def func(x):
        x, y, z = x[0], x[1], x[2]
        f = (
            lambda x: (a1 * x**a2 + a3 * y**a4 + a5 * z**a6 - 1 - No / 100) ** 2
            + (b1 * x**b2 + b3 * y**b4 + b5 * z**b6 - 1 - No / 100) ** 2
            + (c1 * x**c2 + c3 * y**c4 + c5 * z**c6 - 1 - No / 100) ** 2
        )
        return f(x)  # 求最大变成求最小，前面加负号

    # if __name__ == '__main__':
    # PSO(func, 50, 1.5, 2.5, 0.5, 100,3)
    PSO(func, N, c1, c2, w, M, 3)

elif add_selectbox == "蚁群算法求解TSP问题":
    # 参数初始化
    # """
    # n:城市数目
    # m: 蚂蚁个数
    # alpha :表征信息素重要程度的参数
    # beta :表征启发式因子重要程度的参数
    # rho :信息素蒸发系数
    # itera_max： 最大迭代次数
    # city_zb:城市坐标
    # Q： 信息素增加强度系数
    # LJ_best[itera_max,n]: 各代最佳路线
    # pen_best[itera_max]: 各代最佳路线的长度
    # eta:启发因子，取距离的倒数
    # LJ[m,n]:路径记录
    # tau[n,n]:信息素矩阵
    # ran_ant:不受信息素影响的随机蚂蚁数
    st.latex("min J=\sum_{i=1}^{n}d_{i,i+1}+d_{n,1},i=1,2,...n-1")
    st.write("设置基本遗传数据:")
    # alpha = 1.5
    # beta = 4
    # rho = 0.08
    # itera_max = 500
    # Q = 1
    # ran_ant = 0
    col1, col2, col3 = st.columns(3)
    with col1:
        alpha = st.number_input("表征信息素重要程度的参数", value=1.5, step=0.1, format="%f")
    with col2:
        beta = st.number_input("表征启发式因子重要程度的参数", value=4.0, step=0.1, format="%f")
    with col3:
        rho = st.number_input("信息素蒸发系数", value=0.25, step=0.01, format="%f")
    col1, col2, col3 = st.columns(3)
    with col1:
        itera_max = st.number_input("最大迭代次数", value=500, step=1, format="%d")
    with col2:
        Q = st.number_input("信息素增加强度系数", value=10.0, step=0.1, format="%f")
    with col3:
        ran_ant = st.number_input("不受信息素影响的随机蚂蚁数", value=0, step=1, format="%d")

    # 产生随机城市坐标city_zb
    def city_zb(width, hight, city_num):
        """
        width:城市配置平面图宽度
        hight:城市配置平面图高度
        city_num:配置城市数目
        """
        city_zb = np.zeros((city_num, 2))
        for i in range(city_num):
            city_zb[i, 0] = int(np.random.random() * width * 100) / 100
            city_zb[i, 1] = int(np.random.random() * hight * 100) / 100
        return city_zb

    col1, col2 = st.columns(2)
    with col1:
        city_num = st.number_input("输入随机城市数目，随机计算时使用", value=15, step=1, format="%d")
    with col2:
        B = st.number_input("是否回起点,是1,否0", value=1, step=1, format="%d")
    # city_num = 20
    # city_num = st.number_input("输入随机城市数目，随机计算时使用", value=30, step=1, format="%d")
    st.write("加载具体路径的数据文件csv,三列结构，第一列城市名称，第二列为x坐标，第三列为y坐标；如不加载则利用随机数据进行计算", value="")
    # 读入城市坐标
    uploaded_file2 = st.file_uploader("Choose a file")
    if uploaded_file2 is not None:
        dataframe = pd.read_csv(uploaded_file2)
        array_d = np.array(dataframe)
        # 共有31个城市坐标
        city_x = array_d[:, 1]  # 数据分配
        city_y = array_d[:, 2]
        n = len(city_x)  # 计算城市的数目
        city_zb = np.zeros((n, 2))  # 设置坐标数组
        city_zb[:, 0] = city_x / 100
        city_zb[:, 1] = city_y / 100
    else:
        city_zb = city_zb(50, 50, city_num)
        n = city_num

    # city_files = st.text_input("输入具体路径的数据文件,如为空则利用随机数据进行计算", value="")
    # if city_files == "":
    # city_zb = city_zb(50, 50, city_num)
    # n = city_num
    # else:
    # 读入城市坐标
    # DF = pd.read_excel(
    # city_files, "Sheet1", na_filter=False, index_col=0
    # )  # 共有31个城市坐标
    # city_x = np.array(DF["x"])  # 数据分配
    # city_y = np.array(DF["y"])
    # n = len(city_x)  # 计算城市的数目
    # city_zb = np.zeros((n, 2))  # 设置坐标数组
    # city_zb[:, 0] = city_x / 100
    # city_zb[:, 1] = city_y / 100

    # 计算坐标起始范围：
    x_min = min(city_zb[:, 0])
    x_max = max(city_zb[:, 0])
    y_min = min(city_zb[:, 1])
    y_max = max(city_zb[:, 1])
    # 定义绘制路径图函数
    # n = len(city_zb)

    def Distance(city_zb):
        D = np.zeros((n, n))  #  产生两城市之间距离数据的空矩阵即零阵
        for i in range(n):
            D[i, i] = 10e-4  # 计算信息素时要用到
            for j in range(i + 1, n):
                D[i, j] = (
                    (city_zb[i, 0] - city_zb[j, 0]) ** 2
                    + (city_zb[i, 1] - city_zb[j, 1]) ** 2
                ) ** 0.5
                D[j, i] = D[i, j]
        return D

    D = Distance(city_zb)  # 计算一次即可
    m = int(1.3 * n)  # 确定蚂蚁数
    alpha = alpha
    beta = beta
    rho = rho
    itera_max = itera_max
    Q = Q
    ran_ant = ran_ant
    LJ_best = np.zeros((itera_max, n))  # 各代最佳路线
    pen_best = np.zeros(itera_max)  # 各代最佳路线的长度
    eta = 3.0 / D  # 启发因子，取距离的倒数
    LJ = np.zeros((m, n))  # 路径记录
    tau = np.ones((n, n))  # 信息素矩阵
    # 产生初始蚂蚁轨迹LJ0用以验证绘制程序的正确性
    def path(n):
        li = np.arange(0, n)
        LJ = np.zeros(n)
        rnd.shuffle(li)
        LJ[:] = li
        return LJ.astype(int)  # 需要强制转变成整数

    LJ0 = path(n)
    # 绘制初始路径图
    # 画路径函数
    def drawpath(LJ, city_zb, num):
        """
        #画路径函数
        #输入
        LJ: 待画路径
        city_zb: 各城市坐标位置
        num: 图片左上角的图名
        """
        plt.figure(num=num)
        n = len(LJ)
        plt.scatter(
            city_zb[:, 0], city_zb[:, 1], marker="o", color="b", s=100
        )  # 所有城市位置上画上o
        plt.text(city_zb[LJ[0], 0] + 0.5, city_zb[LJ[0], 1] + 0.5, "Start")
        plt.text(city_zb[LJ[n - 1], 0] + 0.5, city_zb[LJ[n - 1], 1] + 0.5, "End")
        for i in range(n):
            plt.text(city_zb[i, 0] - 0.3, city_zb[i, 1] + 0.5, str(i + 1), color="r")
        # 绘线
        xy = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
        xytext = (city_zb[LJ[1], 0], city_zb[LJ[1], 1])
        plt.annotate(
            "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="g", lw=2)
        )
        for i in range(1, n - 1):
            xy = [city_zb[LJ[i], 0], city_zb[LJ[i], 1]]
            xytext = [city_zb[LJ[i + 1], 0], city_zb[LJ[i + 1], 1]]
            plt.annotate(
                "",
                xy=xy,
                xytext=xytext,
                arrowprops=dict(arrowstyle="<-", color="g", lw=2),
            )
        if B == 1:
            xy = (city_zb[LJ[n - 1], 0], city_zb[LJ[n - 1], 1])
            xytext = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
            plt.annotate(
                "",
                xy=xy,
                xytext=xytext,
                arrowprops=dict(arrowstyle="<-", color="g", lw=1),
            )
        # plt.ylim(0,40)
        # plt.xlim(10,50)
        plt.ylim(y_min - 2, y_max + 2)
        plt.xlim(x_min - 2, x_max + 2)
        # plt.ylim(-5, 55)
        # plt.xlim(-5, 55)
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(" Trajectory Map")

    # 路径长度计算
    def pathlength(D, LJ):
        N = D.shape[1]
        p_len = 0
        for j in range(N - 1):
            p_len = p_len + D[LJ[j], LJ[j + 1]]
        if B == 1:
            p_len = p_len + D[LJ[N - 1], LJ[0]]
        return p_len

    p_len = pathlength(D, LJ0)
    # print(p_len)
    # 绘制初始路径1
    num = "绘制初始路径"
    draw_path = drawpath(LJ0, city_zb, num)
    # plt.legend(str(p_len[0]))
    plt.text(22, 33, "总长度=" + str(int(1000 * p_len) / 1000))
    # 打印路径
    def print_way(LJ):
        print_LJ = str()
        n = len(LJ)
        for i in range(n):
            print_LJ = print_LJ + str(LJ[i] + 1) + "-->"
        if B == 1:
            print_LJ = print_LJ + str(LJ[0] + 1)
        return print_LJ

    # print(print_LJ)
    # print("初始路径")
    # print_way(LJ0)
    # 开始迭代计算
    itera_num = 0
    while itera_num < itera_max:
        # 随机产生每只蚂蚁的起点城市序号0~n-1
        start = np.zeros(m)
        # itera_num=itera_num+1
        for i in range(m):
            start[i] = rnd.randint(0, n - 1)
        start = start.astype(int)
        # print(start)
        LJ[:, 0] = start
        LJ = LJ.astype(int)
        city_id = np.arange(n)
        # print(city_id)
        p_len = np.zeros(m)  # 每只蚂蚁的总路径长度初始化
        for i in range(m):  # m只蚂蚁逐个城市选择路径
            for j in range(1, n):
                prohi_tab = LJ[i, 0:j]  # 禁止表 prohibit_table
                allow = list(set(city_id).difference(set(prohi_tab)))
                P = np.zeros(len(allow))  # []#建立初始空数据
                for k in range(len(allow)):
                    # print(prohi_tab[j-1],allow[k])
                    P[k] = (
                        tau[prohi_tab[j - 1], allow[k]] ** alpha
                        * eta[prohi_tab[j - 1], allow[k]] ** beta
                    )
                    # tem_P=tau[prohi_tab[j-1],allow[k]]**alpha+eta[prohi_tab[j-1],allow[k]]**beta
                    # P.append(tem_P)
                # print("k=",k)
                # print("allow[k]=",allow[k])
                # print("J=",j)
                # print("k=",k)
                P = P / sum(P)
                # print(P)
                Pc = cumsum(P)
                # print(Pc)
                # Pc=P
                tar_id = [i for i, tp in enumerate(Pc) if tp > np.random.random()]
                tar = allow[tar_id[0]]
                LJ[i, j] = tar
            # print("LJ=",LJ[i,:])
            if i >= m - ran_ant:  # ran_ant=3
                LJ[i, :] = path(n)
                # print("LJ(m-1)",LJ[m-1,:])#每轮循环放三只随机蚂蚁，不受信息素影响，以便跳出局部最优解

            p_len[i] = pathlength(D, LJ[i, :])
        id_ant = list(p_len[:]).index(min(p_len[:]))  # 找到最短距离路径的蚂蚁序号

        pen_best[itera_num] = p_len[id_ant]  # 各代最佳路线的长度
        LJ_best[itera_num, :] = LJ[id_ant, :]  # 各代最佳路线
        # print(LJ[i,:])
        # print(len(LJ[i,:]))
        detal_tau = np.zeros((n, n))
        for i in range(m):
            for j in range(n - 1):
                detal_tau[LJ[i, j], LJ[i, j + 1]] = (
                    detal_tau[LJ[i, j], LJ[i, j + 1]] + Q / p_len[i]
                )
                # detal_tau[LJ[i,j+1],LJ[i,j]]=detal_tau[LJ[i,j+1],LJ[i,j]]+Q/ p_len[i]
            detal_tau[LJ[i, n - 1], LJ[i, 0]] = (
                detal_tau[LJ[i, n - 1], LJ[i, 0]] + Q / p_len[i]
            )  # 最后一个点和起始点闭合
            # detal_tau[LJ[i,0],LJ[i,n-1]]=detal_tau[LJ[i,0],LJ[i,n-1]]+Q/ p_len[i]

        # 最优蚂蚁路线加强：
        for j in range(n - 1):
            detal_tau[LJ[id_ant, j], LJ[id_ant, j + 1]] = (
                detal_tau[LJ[id_ant, j], LJ[id_ant, j + 1]] + 9
            )
            # detal_tau[LJ[i,j+1],LJ[i,j]]=detal_tau[LJ[i,j+1],LJ[i,j]]+Q/ p_len[i]
        detal_tau[LJ[id_ant, n - 1], LJ[id_ant, 0]] = (
            detal_tau[LJ[id_ant, n - 1], LJ[id_ant, 0]] + 9
        )
        tau = (1 - rho) * tau + detal_tau  # 更新信息素
        # print("tau=",tau)
        itera_num = itera_num + 1
        LJ = np.zeros((m, n))  # 路径记录清空
    id_best = list(pen_best[:]).index(min(pen_best[:]))  # 找到最短距离路径的迭代序号
    print(LJ_best[id_best, :].astype(int))
    LJ_end = LJ_best[id_best, :].astype(int)
    # print("最优路径")
    # print_way(LJ_end)
    st.write("最优路径")
    st.write(print_way(LJ_end))
    num = "draw the optimal path"
    draw_path = drawpath(LJ_end, city_zb, num)
    yt = 0.8 * (y_max - y_min - 1) + y_min
    xt = 0.65 * (x_max - x_min - 1) + x_min
    plt.text(xt, yt, "Total length=" + str(int(1000 * pen_best[id_best]) / 1000))
    st.write("绘制最终优化图")
    st.pyplot(draw_path)

    st.write("最优路径总长度=", (int(1000 * pen_best[id_best]) / 1000))
    fig, ax = plt.subplots(num="Optimization path distance iteration number graph")
    for i in range(itera_max - 1):
        ax.plot([i, i + 1], [pen_best[i], pen_best[i + 1]])
    plt.xlabel("Number of iterations")
    plt.ylabel("Path length")
    plt.title(
        "The relationship between the distance of optimize path  and the number of iterations"
    )
    plt.grid()
    st.pyplot(fig)
