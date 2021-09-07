#ndimage basic application
import numpy as np
from numpy.core.numeric import ones_like
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

from sklearn import  neighbors as nbs
#plt.style.use('style/elegant.mplstyle')
figure,ax=plt.subplots(1,3,figsize=(18,6))
R_image1=np.random.randint(0,256,size=(801,801))
ax[0].imshow(R_image1)
ax[0].set_title("0-255随机整数图")

R_image2=np.random.rand(801,801)
ax[1].imshow(R_image2)
ax[1].set_title("0-1随机数图")




R_image3=np.ones((801, 801))
ax[2].imshow(R_image3)
ax[2].set_title("1数图")



plt.figure()
from skimage import io 

#img1=("g:/flg.png")

img1=("g:/butterfly.JPG")
asimg1=io.imread(img1)
print(type(asimg1),asimg1.shape,asimg1.dtype)
plt.imshow(asimg1)

#scikit_image-0.17.2-cp37-cp37m-win_amd64.whl
#print(asimg1[5000,300:400,:])

plt.figure()
butt=io.imread("butterfly.JPG")
plt.imshow(butt)

plt.figure()
insc=io.imread("insect.png")
print(insc)

plt.imshow(insc)



plt.show()


