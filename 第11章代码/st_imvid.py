#st_imvid.py
import streamlit as st
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 设置刻度线朝内
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细

col1, col2, col3 = st.columns(3)
with col1:
    image1 = Image.open("g:/建筑2.jpg")
    st.header("励悟楼图片")
    st.image(image1)
with col2:
    video_file = open("g:/chapter1-1.mp4", "rb")
    video_bytes = video_file.read()
    st.header("慕课视频")
    st.video(video_bytes)
with col3:
    fig=plt.figure(figsize=(8, 6), dpi=80)  # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    x = np.linspace(0, 10, 101, endpoint=True)
    # 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
    plt.plot(x, np.sin(x), label="y", color="red", linewidth=2, linestyle="-")
    plt.xlim(0, 10)  # 设置横轴的上下限
    plt.xticks(np.arange(0, 10, 1))  # 设置横轴刻度
    plt.xlabel("x", color="blue")  # 设置x轴描述信息
    plt.ylabel("y",color="red")  # 设置y轴描述信息
    plt.yticks()  # 设置纵轴刻度
    plt.legend()
    plt.grid(True)
    st.header("Matplotlib图形")
    #st.pyplot(fig)
    st.write(fig)

