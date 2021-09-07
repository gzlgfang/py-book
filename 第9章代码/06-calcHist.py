#06-calcHist.py
#像素颜色强度值直方图
from matplotlib import colors
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小


img1=cv2.cvtColor(cv2.imread("heflower.jpg"),cv2.COLOR_BGR2RGB)#读入图像及翻转
R,G,B=cv2.split(img1)#三通道数据分离
hist_R=cv2.calcHist([R],[0],None,[256],[0,255])
hist_G=cv2.calcHist([G],[0],None,[256],[0,255])
hist_B=cv2.calcHist([B],[0],None,[256],[0,255])

plt.plot(hist_R,color="r",lw=2,label="红色")
plt.plot(hist_G,color="g",lw=2,ls=":",label="绿色")
plt.plot(hist_B,color="b",lw=2,ls="-.",label="蓝色")
plt.legend()
plt.grid()
#plt.xlim=(0,256)
#plt.ylim=(0,2000)
plt.xlabel("Bins")
plt.ylabel("某Bins范围内像素个数统计值")
plt.title("三色像素统计直方图")
plt.show()