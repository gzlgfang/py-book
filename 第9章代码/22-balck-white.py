#balck-white
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小
im=cv2.imread("insect.png")
plt.imshow(im)
plt.figure()
im2=cv2.imread("insect.png",0)
plt.imshow(im2)
plt.figure()
ret,imb_w=cv2.threshold(im2,127,255,cv2.THRESH_TRIANGLE)
plt.imshow(imb_w)
print(ret)

cv2.namedWindow("Image1",cv2.WINDOW_NORMAL)
cv2.imshow("Image1",imb_w)
plt.title("黑白图")


plt.show()
