#!/usr/bin/env python3
# 01-BP_basica
import time
import numpy as np
import random as rnd

# 绘图设置
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 28  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细

n = eval(input("输入输入层神经元数目="))  # 相当于输入变量有n个分量
p = eval(input("输入中间层神经元数目="))
q = eval(input("输入输出层神经元数目="))  # 相当于输出变量有q个分量

num = 0
m = eval(input("训练模式数量="))
a = np.zeros((m, n))
y = np.zeros((m, q))
#'输入已知模式对的输入输出数据，若有绝对值大于1的数据，需对数据作归一化处理，'该程序中认为所有数据绝对值小于等于1，未作归一化处理，读者在应用时请注意
for i in range(m):
    for j in range(n):
        print("输入第", i + 1, "模式第", j + 1, "输入变量a[i, j]")
        a[i, j] = eval(input("a[i, j]="))
    for j in range(q):
        print("输入第", i + 1, "模式第", j + 1, "输出变量y[i, j]")
        y[i, j] = eval(input("y[i, j]="))

#'生成初始连接权数及阀值
start_time = time.perf_counter()
print("start_time:", start_time)

w = np.zeros((n, p))
thta = np.zeros(p)
for j in range(p):
    for i in range(n):
        w[i, j] = 2 * rnd.random() - 1  # '保证产生（-1，1）之间的随机数
    thta[j] = 2 * rnd.random() - 1  #   ' 随机函数
    #'Print thta(j)
# w=2*np.random.random((n,p))-1
v = np.zeros((p, q))
r = np.zeros(q)
for t in range(q):
    for j in range(p):
        v[j, t] = 2 * rnd.random() - 1
        #'Print v(j, t)
    r[t] = 2 * rnd.random() - 1
    #'Print r(t)
#'神经元函数
def fnf(x):
    fnf = 1 / (1 + np.exp(-x))
    return fnf


ee = 1
train_num = 0
tol = []
b = np.zeros(p)
c = np.zeros((m, q))
d = np.zeros(q)
while ee > 0.005:
    eer = np.zeros(m)
    # c=np.zeros((m,q))
    e = np.zeros((m, p))
    for k in range(m):
        # eer(k) = 0
        #'模式顺传播
        s = np.zeros(p)
        # b=np.zeros(p)
        for j in range(p):
            # s(j) = 0
            for i in range(n):
                s[j] = s[j] + w[i, j] * a[k, i]
            s[j] = s[j] - thta[j]
            b[j] = fnf(s[j])
        L = np.zeros(q)
        # d=np.zeros(q)
        for t in range(q):
            # L(t) = 0
            for j in range(p):
                L[t] = L[t] + v[j, t] * b[j]
            L[t] = L[t] - r[t]
            #'Print l(t)
            c[k, t] = fnf(L[t])
            #'误差逆传播
            d[t] = (y[k, t] - c[k, t]) * c[k, t] * (1 - c[k, t])

        for j in range(p):
            # e(k, j) = 0
            for t in range(q):
                e[k, j] = e[k, j] + d[t] * v[j, t]
            e[k, j] = e[k, j] * b[j] * (1 - b[j])

        #'调整连接权及罚值，网络的学习系数均取0.5
        for t in range(q):
            for j in range(p):
                v[j, t] = v[j, t] + 0.5 * d[t] * b[j]
            r[t] = r[t] - 0.5 * d[t]  # 0.5学习效率，下同
        for j in range(p):
            for i in range(n):
                w[i, j] = w[i, j] + 0.5 * e[k, j] * a[k, i]
            thta[j] = thta[j] - 0.5 * e[k, j]
    train_num = train_num + 1

    #'计算全局误差
    ee = 0
    for k in range(m):
        # eer(k) = 0
        for t in range(q):
            eer[k] = eer[k] + (y[k, t] - c[k, t]) ** 2
        ee = ee + eer[k]
    ee = np.sqrt(ee)
    #'全局误差判断

    if train_num / 10000 == int(train_num / 10000):
        print("ee=", ee)
        tol.append(ee)
    if train_num < 10000000:
        continue  #'网络尚未收敛，继续计算
    else:
        break
    #'网络收敛，打印权值及阀值并进入回响
    # GoTo 200
# 绘制误差图
# print(tol)
train_num1 = []
print(len(tol))
for i in range(len(tol)):
    train_num1.append((i + 1) * 10000)
plt.figure()
plt.plot(train_num1, tol, lw=2, marker="o", color="#1f77b4")  #
plt.grid()
plt.xlabel("训练数目")
plt.ylabel("全局误差")
plt.title("训练数目和全局误差关系图")
#
#'打印权值及阀值
for j in range(p):
    for i in range(n):
        print("w(", i, ",", j, ")=", w[i, j])
    print("thta(", j, ")=", thta[j])
for t in range(q):
    for j in range(p):
        print("v(", j, ",", t, ")=", v[j, t])
    print("r(", t, ")=", r[t])
print("全局误差=", ee, "\n" "总训练次数=", train_num)
end_time = time.perf_counter()
print("perf_counter程序运行计时=", end_time - start_time, "秒")
# '网络回响
flags = True
while flags:
    x = np.zeros(n)
    for i in range(n):
        print("输入第", i + 1, "输入变量")
        x[i] = eval(input("x[i]="))
        # print(x[i])
    s = np.zeros(p)
    for j in range(p):
        for i in range(n):
            s[j] = s[j] + w[i, j] * x[i]
        s[j] = s[j] - thta[j]
        b[j] = fnf(s[j])
    L = np.zeros(q)
    for t in range(q):
        for j in range(p):
            L[t] = L[t] + v[j, t] * b[j]
        L[t] = L[t] - r[t]
        # print(L[t])
        yy = fnf(L[t])
        print("回响值=", yy)
    tt = input("是否继续需要网络回响，是输入y，否输入n ")
    if tt == "y":
        flags = True
    else:
        flags = False

plt.show()

#'神经元函数
# fnf = 1 / (1 + Exp(-x))
