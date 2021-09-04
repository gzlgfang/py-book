import cv2
import matplotlib.pyplot as plt
cv2.namedWindow("Image1",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image2",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image3",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image4",cv2.WINDOW_NORMAL)

#img1=cv2.imread("g:/jianghua.jpg")
##img2=cv2.imread("g:/starflower.jpg")
#img3=cv2.imread("g:/insect.png")

img1=cv2.imread("jianghua.jpg")
img2=cv2.imread("starflower.jpg")
img3=cv2.imread("insect.png")
img4=cv2.imread("insect.png",flags=0)


cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.imshow("Image3",img3)
cv2.imshow("Image4",img4)
cv2.waitKey(delay=-2)
#plt.show()