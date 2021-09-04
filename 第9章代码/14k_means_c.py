#14-k_means_c
import matplotlib.pyplot as plt
import numpy as np
import cv2
plt.style.use('ggplot')#引入plt绘制风格
from sklearn.datasets import make_blobs
import matplotlib as mpl

cv2.namedWindow("building",cv2.WINDOW_NORMAL)
img1=cv2.imread("building2.jpg")
cv2.imshow("building",img1)
print("img1.shape=",img1.shape)
height1,width1,n1=img1.shape
img1_data=img1/255.0
#print(img1_data[1,1][:])
img1_data=img1_data.reshape((-1,3))
print(img1_data.shape)

criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,18,0.5)#收敛准则，迭代18次，误差小于1
flags=cv2.KMEANS_RANDOM_CENTERS#随机产生初始中心
compactness,labels,centers=cv2.kmeans(img1_data.astype(np.float32),16,None,criteria,8,flags)
print(centers)
print((labels.shape))
new_clours=centers[labels].reshape((-1,3))#所有label数据替换成3元的颜色数据
print(new_clours)

new_img1=new_clours.reshape(img1.shape)#恢复到原图像数据结构

cv2.namedWindow("new-building",cv2.WINDOW_NORMAL)

cv2.imshow("new-building",new_img1)


cv2.waitKey(delay=-1)
