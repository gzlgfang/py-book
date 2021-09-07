#08-ad_Threshold
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
img1=cv2.imread("insect.png",flags=0)
#img=cv2.cvtColor(cv2.imread("heflower.jpg"),cv2.COLOR_BGR2GRAY)
#img1=cv2.imread("treepolo.jpg",0)
ret,img2 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
img3 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3) 
img4 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2) 
images =[img1,img2,img3,img4]
titles = ['原灰度图gray','二值图THRESH_BINARY','.ADAPTIVE_THRESH_MEAN_C','ADAPTIVE_THRESH_GAUSSIAN_C']
fig,ax=plt.subplots(1,4,figsize=(20,5),num="自适应阀值绘制")
for i in range(4):   
       ax[i].imshow(images[i],'gray')
       ax[i].set_title(titles[i])
plt.show()

