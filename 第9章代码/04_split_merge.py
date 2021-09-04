import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cv2
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] =12#设置字体大小

img1=cv2.cvtColor(cv2.imread("jianghua.jpg"),cv2.COLOR_BGR2RGB)
R,G,B=cv2.split(img1)
print("R=\n",R)
D2_data1=R[0:8,0:8]
D2_data2=G[0:8,0:8]
D2_data3=B[0:8,0:8]

fig,ax=plt.subplots(1,3,figsize=(24,8))
sn.heatmap(D2_data1,vmin=0,vmax=256,linewidths = 0.05, annot=True, fmt='.1f', cmap='Reds_r', yticklabels=np.arange(1,9,1),xticklabels=np.arange(1,9,1),ax=ax[0])
sn.heatmap(D2_data2,vmin=0,vmax=256,linewidths = 0.05, annot=True, fmt='.1f', cmap='GnBu_r', yticklabels=np.arange(1,9,1),xticklabels=np.arange(1,9,1),ax=ax[1])
sn.heatmap(D2_data3,vmin=0,vmax=256,linewidths = 0.05, annot=True, fmt='.1f', cmap='Blues', yticklabels=np.arange(1,9,1),xticklabels=np.arange(1,9,1),ax=ax[2])

cv2.namedWindow("Image_R",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image_G",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image_B",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image_RGB",cv2.WINDOW_NORMAL)

img1,img2,img3=R,G,B
img4=cv2.merge([B,G,R])
cv2.imshow("Image_R",img1)
cv2.imshow("Image_G",img2)
cv2.imshow("Image_B",img3)
cv2.imshow("Image_RGB",img4)
plt.show()
cv2.waitKey(delay=-1)
#cmap='rainbow'
