#07-threshold.py
#二值图绘制
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
mpl.rcParams["font.size"] = 16#设置字体大小
#img=cv2.imread("insect.png",flags=0)
#img=cv2.cvtColor(cv2.imread("heflower.jpg"),cv2.COLOR_BGR2GRAY)
#img=cv2.imread("heflower.jpg",0)
img=cv2.imread("g:\qm2.png",0)
hist=cv2.calcHist([img],[0],None,[256],[0,255])
plt.plot(hist,color="b",lw=2)
TR=170
plt.figure()
ret1,img1 = cv2.threshold(img,TR,255,cv2.THRESH_BINARY)
ret2,img2 = cv2.threshold(img,TR,255,cv2.THRESH_BINARY_INV)
ret3,img3 = cv2.threshold(img,TR,255,cv2.THRESH_TRUNC)
ret4,img4 = cv2.threshold(img,TR,255,cv2.THRESH_TOZERO)
ret5,img5 = cv2.threshold(img,TR,255,cv2.THRESH_TOZERO_INV)
print("ret1,ret2,ret3,ret4,ret5=",ret1,ret2,ret3,ret4,ret5)


titles = ['原图','大于阀值取255其它取零','大于阀值取零其它取255','大于阀值取阀值其它取原值','大于阀值取原值其它取零','大于阀值取零其它取原值']
imgs = [img,img1,img2,img3,img4,img5]
for i in range(6):   
    plt.subplot(2,3,i+1)
    plt.imshow(imgs[i],cmap='gray', vmin=0, vmax=255) 
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()






