#03-image_shape
import cv2
import matplotlib.pyplot as plt
import numpy as np

img1=cv2.imread("jianghua.jpg")
img2=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
height1,width1,n1=img1.shape
height2,width2,n2=img2.shape
print(img1.shape,img2.shape)
print(type(img1))
print(img1.dtype)
print(img1[100,200])
print(img2[100,200])
print(img1[100,200][0])
print(img2[100,200][0])
print(img1[:,:])
print(img1.flatten())
print(len(img1.flatten()))

plt.imshow(img1)
plt.figure()
plt.imshow(img2)
img3=img1.copy()
for i in range(height1):
    for j in range(width1):
        for k in range(n1):
            img3[i,j][k]=255-img1[i,j][k]
plt.figure()
plt.imshow(img3)


plt.show()




