00

import cv2
import matplotlib.pyplot as plt
import numpy as np

img1=cv2.imread("xtx_gra.jpg",cv2.IMREAD_UNCHANGED)
cv2.namedWindow("Original image ",cv2.WINDOW_NORMAL)
cv2.imshow("Original image ",img1)
#核，正方形
#kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
#kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
#kernel3 = cv2.getStr2ucturingElement(cv2.MORPH_ELLIPSE,(10,20))
kernel4 = np.ones((10,10), np.float32) 
kernel=kernel4


#腐蚀
erosion = cv2.erode(img1, kernel ,iterations = 1)
cv2.namedWindow("erosion",cv2.WINDOW_NORMAL)
cv2.imshow("erosion",erosion)


#膨胀
dilation = cv2.dilate(img1, kernel, iterations = 1)
cv2.namedWindow("dilation",cv2.WINDOW_NORMAL)
cv2.imshow("dilation",dilation)


#开运算=先腐蚀后膨胀dilate(erode())
open = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel, iterations=9)
cv2.namedWindow("open",cv2.WINDOW_NORMAL)
cv2.imshow("open",open)
#闭运算=先膨胀后腐蚀erode(dilate())
close = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel,iterations=9)
cv2.namedWindow("close",cv2.WINDOW_NORMAL)
cv2.imshow("close",close)

#形态学梯度：膨胀图减去腐蚀图得到物体的轮廓：dilation - erosion，
cv2.namedWindow("dilation - erosion",cv2.WINDOW_NORMAL)
img2=dilation - erosion
cv2.imshow("dilation - erosion",img2)

img3= cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)#轮廓图
cv2.namedWindow("cv2.MORPH_GRADIENT",cv2.WINDOW_NORMAL)
cv2.imshow("cv2.MORPH_GRADIENT",img3)


# 顶帽：原图减去开运算后的图：tophat=img1 - open
img4=cv2.morphologyEx(img1, cv2.MORPH_TOPHAT, kernel)
cv2.namedWindow("cv2.MORPH_TOPHAT",cv2.WINDOW_NORMAL)
cv2.imshow("cv2.MORPH_TOPHAT",img4)
#黑帽：闭运算后的图减去原图：blackhat = close - img1
img5=cv2.morphologyEx(img1, cv2.MORPH_BLACKHAT, kernel)
cv2.namedWindow("MORPH_BLACKHAT",cv2.WINDOW_NORMAL)
cv2.imshow("MORPH_BLACKHAT",img5)
cv2.waitKey(delay=-1)
