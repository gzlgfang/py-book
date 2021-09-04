#不同第三库读入图片文件 01-SOP_readshow
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小

import skimage  as ski
from skimage import io 
import cv2
from PIL import Image

figure,ax=plt.subplots(1,4,figsize=(16,4))
R_image1=np.random.randint(0,256,size=(1101,901))
#R_image12=np.random.randint(0,256,size=(1101,901))
#R_image13=np.random.randint(0,256,size=(1101,901))
#R_image1= np.array([R_image11,R_image12,R_image13]).T

ax[0].imshow(R_image1)
ax[0].set_title("0-255随机整数图")

R_image2=io.imread("redleaf2.jpg")
ax[1].imshow(R_image2)
ax[1].set_title("scikit_image读入图")
print("skimage_type=",type(R_image2))


R_image3=cv2.imread("maofengshan.jpg")
print("cv2_type=",type(R_image3))
R_image3=cv2.cvtColor(R_image3,cv2.COLOR_BGRA2RGB)
ax[2].imshow(R_image3)
ax[2].set_title("OpenCV读入BGR2RGB图")

R_image4=Image.open("g:/butterfly.JPG")
print("PIL_type=",type(R_image4))
R_image4=R_image4.rotate(90, expand=True)
print(R_image4.size)
R_image4=np.array(R_image4)
R_image4=R_image4[500:2800,0:2000][:]
ax[3].imshow(R_image4)
ax[3].set_title("PIL读入图")
plt.figure()
plt.imshow(R_image3)
plt.figure()
plt.imshow(R_image1)

plt.show()



