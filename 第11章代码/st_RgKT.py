# 01-Rg_Kt1.py
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
# 设置刻度线朝内
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细
# 初始化参数设置
st.latex("微分方程:f(x)= cos(ax)+0.8*sin(bx)")
st.latex("初始条件:y(0)= c")
col1,col2,col3=st.columns(3)
with col1:
    a= st.number_input("a", value=1.0, step=0.1, format="%f")
with col2:
    b = st.number_input("b", value=1.0, step=0.1, format="%f")
with col3:
    c= st.number_input("c", value=2.0, step=0.1, format="%f")

h = 0.01
x00 = 0
y0 = c
xt = 10.0
n = int((xt - x00) / h)

def dy(x, y):
    # ddy = y**2 *np.cos(x)
    ddy = np.cos(a * x) + 0.8 * np.sin(b * x)
    return ddy

def rgkt(y0, x0):  # 四阶龙格—库塔法
    k1 = dy(x0, y0)
    k2 = dy((x0 + 0.5 * h), (y0 + 0.5 * h * k1))
    k3 = dy((x0 + 0.5 * h), (y0 + 0.5 * h * k2))
    k4 = dy((x0 + h), (y0 + h * k3))
    y = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y

ddy = []
result = []
for i in range(n):
    x0 = h * i + x00
    y = rgkt(y0, x0)
    k1 = dy(x0, y0)
    ddy.append(k1)
    y0 = y
    result.append(y0)
for i in range(int(n / 2)):
    print(f"x={2*(i+1)*h:.2f},y={result[2*(i+1)-1]:.5f}")
fig=plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
X = np.linspace(0, xt, n, endpoint=True)
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(X, result, label="y", color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(X, ddy, label="dy/dx", color="green", linewidth=2.0, linestyle="--")
plt.xlim(0, xt)  # 设置横轴的上下限
plt.xticks(np.arange(0, xt, 1))  # 设置横轴刻度
ymin = [min(result[:]), min(ddy[:])]
ymax = [max(result[:]), max(ddy[:])]
plt.ylim(min(ymin) - 1, max(ymax) + 1)  # 设置纵轴的上下限
# plt.ylim(min(result[:]),max(result[:]))# 设置纵轴的上下限
plt.xlabel("x", color="blue")  # 设置x轴描述信息
plt.ylabel("y,dy", color="red")  # 设置y轴描述信息
plt.yticks()  # 设置纵轴刻度
plt.legend()
plt.grid(True)

st.pyplot(fig)

