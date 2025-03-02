#!/usr/bin/env python3
import numpy as np
from scipy import optimize
from numpy.lib import copy
import random as rnd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
# 绘图设置
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细

# 模拟退火基础参数：
global T0, q, Tend, T
T0 = 2800  # 初始温度
Tend = 0.01  # 最终温度
L = 480  # 链长，每次稳定温度下优化次数
q = 0.93  # 温度下降速率
def fun(x):
    return T0 * q ** x[0] - Tend
T_num = int(optimize.fsolve(fun, [30]) + 2)  # 计算退火次数
# 产生w×h个点的坐标，其中两点作为开始点和结束点
# w=6
# h=6

#
st.header("有关方阵点最短距离连点问题人工智能求解")
st.text("本软件由方利国、方曦共同开发")
st.text("发现错误之处请联系lgfang@scut.edu.cn,不胜感谢。")
#streamlit run "g:/st-app/st_move.py"

city_zb1 = np.zeros((25, 2))  # 设置坐标数组
city_zb1 = np.zeros((25, 2))  # 设置坐标数组
for i in range(5):
        for j in range(5) :
            p_num=i*5+j
            city_zb1[p_num, 0] = j
            city_zb1[p_num, 1] = i
    # start_num=2
    # end_num=8
 #示意图绘制
fig10 = plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(
                city_zb1[:, 0], city_zb1[:, 1], marker="o", color="b", s=100
            ) 
plt.text(city_zb1[2, 0] + 0.2, city_zb1[3, 1] + 0.1, "Start")
plt.text(city_zb1[8, 0] + 0.2, city_zb1[6, 1] + 0.1, "End")
for i in range(25):
                # plt.text(city_zb[LJ[i],0]-0.3,city_zb[LJ[i],1]+0.5,str(i+1),color="r")
                plt.text(city_zb1[i, 0]+ 0.1, city_zb1[i, 1] + 0.1, str(i+1), color="r")
plt.ylim(-1, 5)
plt.xlim(-1, 5)
plt.xticks(np.arange(-1,5,step=1))
plt.yticks(np.arange(-1,5,step=1))
plt.grid()
st.pyplot(fig10)
#自定义各种函数
#距离计算
def Distance(city_zb,n):
            D = np.zeros((n, n))  #  产生两城市之间距离数据的空矩阵即零阵
            for i in range(n):
                for j in range(i + 1, n):
                    D[i, j] = (
                        (city_zb[i, 0] - city_zb[j, 0]) ** 2
                        + (city_zb[i, 1] - city_zb[j, 1]) ** 2
                    ) ** 0.5
                    if D[i, j]>1:
                        D[i, j]=10000
                    D[j, i] = D[i, j]
            return D
# 产生初始轨迹LJ0
def path(n,start_num,end_num):
            li = np.arange(0, n)
            li=list(li)
            li.remove(start_num)
            li.remove(end_num)
            LJ = np.zeros(n-2)
            rnd.shuffle(li)
            LJ[:] = li
            return LJ.astype(int)  # 需要强制转变成整数
#路径绘制
def drawpath(LJ, city_zb, num):
                fig=plt.figure(num=num)
                n = len(LJ)
                plt.scatter(
                    city_zb[:, 0], city_zb[:, 1], marker="o", color="b", s=100
                )  # 所有城市位置上画上o
                # plt.text(city_zb[LJ[0], 0] + 0.1, city_zb[LJ[0], 1] + 0.1, "起点")
                # plt.text(city_zb[LJ[n - 1], 0] + 0.1, city_zb[LJ[n - 1], 1] + 0.1, "终点")
                plt.text(city_zb[start_num, 0] + 0.2, city_zb[start_num, 1] + 0.1, "Start")
                plt.text(city_zb[end_num, 0] + 0.2, city_zb[end_num, 1] + 0.1, "End")

                for i in range(n+2):
                    # plt.text(city_zb[LJ[i],0]-0.3,city_zb[LJ[i],1]+0.5,str(i+1),color="r")
                    plt.text(city_zb[i, 0] + 0.1, city_zb[i, 1] + 0.1, str(i+1), color="r")
                # 绘线
                xy = (city_zb[start_num, 0], city_zb[start_num, 1])#确定起点到0序号点
                xytext = (city_zb[LJ[0], 0], city_zb[LJ[0], 1])
                plt.annotate(
                    "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="g", lw=2)
                )
                for i in range(0, n-1):
                    # x=[city_zb[LJ[i],0],city_zb[LJ[i+1],0]]
                    # y=[city_zb[LJ[i],1],city_zb[LJ[i+1],1]]
                    # plt.plot(x,y,lw=2,c="r")
                    xy = [city_zb[LJ[i], 0], city_zb[LJ[i], 1]]
                    xytext = [city_zb[LJ[i + 1], 0], city_zb[LJ[i + 1], 1]]
                    plt.annotate(
                        "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="r", lw=3)
                    )

                xy = (city_zb[LJ[n - 1], 0], city_zb[LJ[n - 1], 1])#序号n-1到结束点
                xytext = (city_zb[end_num, 0], city_zb[end_num, 1])
                plt.annotate(
                    "", xy=xy, xytext=xytext, arrowprops=dict(arrowstyle="<-", color="r", lw=3)
                )
                plt.ylim(-1, h)
                plt.xlim(-1, w)
                plt.xticks(np.arange(-1,w,step=1))
                plt.yticks(np.arange(-1,h,step=1))
                plt.grid()
                #plt.xlabel("横坐标")
                #plt.ylabel("纵坐标")
                plt.title("Trajectory Map")
                st.pyplot(fig)
#路径长度计算：
def pathlength(D, LJ):
                N = len(LJ)#扣除2点
                ZQS = 1
                p_len = np.zeros(ZQS)
                for i in range(ZQS):
                    for j in range(N - 1):
                        p_len[i] = p_len[i] + D[LJ[j], LJ[j + 1]]
                    p_len[i]=p_len[i] + D[start_num,LJ[0]]#起点到0点
                    p_len[i] = p_len[i] + D[LJ[N - 1], end_num]#n-1点到终点

                return p_len
# 打印优化路径
def print_way(LJ):
                print_LJ = str()
                n = len(LJ)
                for i in range(n):
                    print_LJ = print_LJ + str(LJ[i] + 1) + "-->"
                print_LJ = str(start_num+ 1)+"-->"+print_LJ + str(end_num + 1)
                # print(print_LJ)
def Newpath(LJ):
                # 有原来的旅行轨迹LJ1计算产生新的旅行轨迹LJ2(部分逆转）
                # 输入 LJ1 原来的旅行轨迹，是0到N-1城市的数字排列
                # 输出 LJ2 新的旅行轨迹,逆转扰动
                N = len(LJ)  # 计算城市的数目
                LJ2 = copy(LJ)  # 先将原轨迹全部复制到新轨迹
                
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
                        r_min = 1#轨迹逆转
                    LJ2[r_min : r_max + 1] = LJ[r_max : r_min - 1 : -1]
                return LJ2
def Metropolis(LJ0, LJ2, D, T):
                Len1 = pathlength(D, LJ0)  # 计算轨迹LJ0路径长度
                Len2 = pathlength(D, LJ2)  # 计算轨迹GJ2路径长度
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


with st.form("my_form"):
    w=st.number_input("选择方阵宽度", value=5,min_value=2, max_value=20, step=1, format="%i")
    h=st.number_input("选择方阵高度", value=5,min_value=2, max_value=20, step=1, format="%i")
    #max_value=w*h-1
    start_num=st.number_input("选择起点序号", value=3,min_value=1, max_value= 100, step=1, format="%i")
    end_num=st.number_input("选择终点序号", value=9,min_value=1, max_value= 100, step=1, format="%i")
    start_num=start_num-1
    end_num=end_num-1
    submitted = st.form_submit_button("点击提交寻找最优路径")
    #输入修改数据
    
    if submitted:
        n=w*h
        st.write("w,h,start_num,end_num=",w,h,start_num+1,end_num+1)
        city_zb = np.zeros((n, 2))  # 设置坐标数组
        city_zb = np.zeros((n, 2))  # 设置坐标数组
        for i in range(h):
            for j in range(w) :
                p_num=i*w+j
                city_zb[p_num, 0] = j
                city_zb[p_num, 1] = i
         #绘制输入数据示意图
        fig1 = plt.figure(figsize=(8, 6), dpi=80)
        plt.scatter(
                    city_zb[:, 0], city_zb[:, 1], marker="o", color="b", s=100
                ) 
        plt.text(city_zb[start_num, 0] + 0.2, city_zb[start_num, 1] + 0.1, "Start")
        plt.text(city_zb[end_num, 0] + 0.2, city_zb[end_num, 1] + 0.1, "End")
        for i in range(n):
                    # plt.text(city_zb[LJ[i],0]-0.3,city_zb[LJ[i],1]+0.5,str(i+1),color="r")
                    plt.text(city_zb[i, 0]+ 0.1, city_zb[i, 1] + 0.1, str(i+1), color="r")
        plt.ylim(-1, h)
        plt.xlim(-1, w)
        plt.xticks(np.arange(-1,w,step=1))
        plt.yticks(np.arange(-1,h,step=1))
        plt.grid()
        st.pyplot(fig1)
        st.write("正在计算中，请耐心等待！")
        D = Distance(city_zb,n)  # 计算一次即可
        
        for k in range(100):  #进行100轮退火智能方法计算，每次计算不一定成功，每次计算右需要T_num 退火，只有总距离符合要求的才算成功
            T0 = 2800#需要恢复初温
            n=w*h
            LJ0 = path(n,start_num,end_num)#产生一个随机路径
            n = len(LJ0)#实际路径上的点数，已扣除规定的起点和终点
            #p_len = pathlength(D, LJ0)

            # 绘制初始路径1
            #num = "绘制初始路径"
            LJ2 = Newpath(LJ0)
            p_len = pathlength(D, LJ2)
            num = "绘制初始退火路径"
            [LJ0, Len] = Metropolis(LJ0, LJ2, D, T0)
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
                obj1[count] = opt_sd
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
            #print_way(LJ0)
            p_len = pathlength(D, LJ0)
            # print("总长=",p_len)
            # print("k=",k)
            if p_len<w*h:
                # print(p_len)
                st.subheader("恭喜您，本次计算获得成功！")
                st.write("模拟退火智能方法运行次数：",k+1)
                num = "绘制最优路径"
                #fig=plt.figure()
                draw_path = drawpath(LJ0, city_zb, num)
                # plt.legend(str(p_len[0]))
                plt.text(w-1, h-1, "总长度=")
                plt.text(w-0.5, h-1, str(int(1000 * p_len) / 1000))
                #st.pyplot(fig)
                fig2=plt.figure(num="优化路径距离和退火次数关系图")
                for i in range(1, T_num - 1):
                    plt.plot([i, i + 1], [obj1[i], obj1[i + 1]])
                #plt.show()
                st.pyplot(fig2)
                # print("k=",k)
                st.subheader("恭喜您，本次计算获得成功！")
                
                break
            if k==99:
                # print("对不起，经过60次的人工智能计算，仍未找到最优解，可能原问题就没有最优解")
                st.write("对不起，经过100次的人工智能计算，仍未找到最优解，可能原问题就没有最优解")