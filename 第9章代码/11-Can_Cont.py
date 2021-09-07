
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import data

import matplotlib as mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小


cat = data.chelsea()
img0=cat
img0=cv2.imread("shufa1.jpg")#",cv2.IMREAD_UNCHANGED)
img0=cv2.cvtColor(img0,cv2.COLOR_BGR2RGB)
img1=cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
edges1=cv2.Canny(img1, 70, 180) 
cv2.namedWindow("edges1",0)#0表示cv2.WINDOW_NORMAL
cv2.imshow("edges1",edges1)

#contours=edges1
#img_cont=cv2.drawContours(img1,contours,contourIdx=-1,color=(0,0,255),thickness=2)
#plt.imshow(img_cont)
#plt.title("img_cont")#color="b"

#cv2.imread("g:/yingwu.jpg")

ret, thresh = cv2.threshold(img1, 0, 200, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img2=cv2.drawContours(img0,contours,-1,(0,0,255),2)  # img为三通道才能显示轮廓
cv2.namedWindow("Con_img2",0)#0表示cv2.WINDOW_NORMAL
cv2.imshow('Con_img2',img2)

kernel = np.ones((8,8), np.float32) 
img3= cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)#轮廓图

cv2.namedWindow("Grad_img3",0)#0表示cv2.WINDOW_NORMAL
cv2.imshow('Grad_img3',img3)


imgs=[edges1,img2,img3]
titles=["Canny检测轮廓","drawContours轮廓","形态学MORPH_GRADIENT轮廓"]
plt.figure(figsize=(24,8))
axes_num=[131,132,133]#布局图号列表
for i,axn in enumerate(axes_num):
    ax=plt.subplot(axn)#将布局图号为axn的子图赋给ax,以便后续用ax调用
    #ax.imshow(imgs[i])
    ax.imshow(imgs[i],cmap='gray', vmin=0, vmax=255)
    ax.set_title(titles[i])
plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.tight_layout()#和上面adjust语句功能相同
plt.show()



cv2.waitKey(delay=-1)
