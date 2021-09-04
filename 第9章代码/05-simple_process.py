#05-simple_process
#通过数组处理数据得到不同图形效果
import cv2
import numpy as np

cv2.namedWindow("Image1",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image2",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image3",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image4",cv2.WINDOW_NORMAL)

img1=cv2.imread("taoflower2.jpg")
img2=255-img1

print("img1.shape=",img1.shape)
height1,width1,n1=img1.shape
scale=10
h=int(height1/scale)
w=int(width1/scale)
img3=img1.copy()
for i in range(h):
    for j in range(w):
        for k in range(n1):
            img3[i,j,k]=img1[i*scale,j*scale,k]

img3=img3[0:h,0:w,:]
print("img3.shape=",img3.shape)
img4=img1.copy()
img4[2000:3000,2000:3000,:]=np.random.randint(0,256,size=(1000,1000,3))

cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.imshow("Image3",img3)
cv2.imshow("Image4",img4)

cv2.waitKey(delay=-1)
