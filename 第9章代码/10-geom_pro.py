#10-geometric process
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
img1=cat
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
#显示原图
cv2.namedWindow("orignal_img",0)#0表示cv2.WINDOW_NORMAL
cv2.imshow("orignal_img",img1)
h,w,n=img1.shape
#平移：
M = np.float32([[1,0,50],[0,1,-50]]) #x方向移50，y方向移动50
img2 = cv2.warpAffine(img1,M,(w,h))
cv2.namedWindow("flat_move",0)#0表示cv2.WINDOW_NORMAL
cv2.imshow("flat_move",img2)
#img1=cv2.imread("yingwu.jpg")#",cv2.IMREAD_UNCHANGED)
#缩小
scale1=(int(0.5*w),int(0.5*h))
img3=cv2.resize(img1,scale1,interpolation=cv2.INTER_AREA)#缩小 
cv2.namedWindow("scale_in",0)#0表示cv2.WINDOW_NORMAL
cv2.imshow("scale_in",img3)

#放大
scale2=(2*w,2*h)
img4=cv2.resize(img1,scale2,interpolation=cv2.INTER_AREA)#缩小 
cv2.namedWindow("scale_out",0)#0表示cv2.WINDOW_NORMAL
cv2.imshow("scale_out",img4)
#旋转
M=cv2.getRotationMatrix2D((w/2.0,h/2.0),45,1)
img5=cv2.warpAffine(img1,M,(w,h))#(w,h)
cv2.namedWindow("ro_img",0)#0表示cv2.WINDOW_NORMAL
cv2.imshow("ro_img",img5)
#翻转
hor_img = cv2.flip( img1, 0 )#水平翻转
ver_img = cv2.flip( img1, 1 )#垂直翻转
both_img = cv2.flip(img1, -1 )#两个方向

cv2.imshow( "Horizontal flip", hor_img )#水平
cv2.imshow( "Vertical flip", ver_img )#垂直
cv2.imshow( "Both flip", both_img )#水平和垂直

plt.figure(figsize=(24,12))
imgs=[img1,img2,img3,img4,img5,hor_img,ver_img,both_img]
titles=["原图","平移图","缩小图","放大图","旋转图","水平翻转","垂直翻转","水平垂直同时翻转"]
axes_num=[241,242,243,244,245,246,247,248]#布局图号列表
for i,axn in enumerate(axes_num):
    ax=plt.subplot(axn)#将布局图号为axn的子图赋给ax,以便后续用ax调用
    #ax.imshow(imgs[i])
    ax.imshow(cv2.cvtColor(imgs[i],cv2.COLOR_RGB2BGR))
    ax.set_title(titles[i])
plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.tight_layout()#和上面adjust语句功能相同
plt.show()



cv2.waitKey(delay=-1)