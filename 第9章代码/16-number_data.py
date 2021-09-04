import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.size"] = 6#设置字体大小
img=cv2.imread("g:/11.PNG",0)
ret,img1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
#scale1=(64,64)
#img2=cv2.resize(img1,scale1,interpolation=cv2.INTER_AREA)#缩小 

h,w=img1.shape
print(h,w)
plt.imshow(img1, cmap="gray",vmin=0, vmax=255)
plt.figure()
img_data=np.zeros((100,102,104))

#img_data=np.zeros((100,96,102))

#img_data=np.zeros((50,140,167))
img_tar=np.zeros(100)

for i in range(10):
    for j in range(10):
        img_tar[10*i+j]=j
        #img_data[10*i+j]=img1[1+96*i:1+96*(i+1),3+102*j:3+102*(j+1)]
        img_data[10*i+j]=img1[0:102,104*j:104*(j+1)]
        #img_data[10*i+j]=img1[1+96*i:1+96*(i+1),3+102*j:3+102*(j+1)]
        #img_data[10*i+j]=img1[140*i:140*(i+1),4+167*j:4+167*(j+1)]
plt.imshow(img_data[23], cmap="gray",vmin=0, vmax=255)

plt.figure()
for i in range(100):   
    plt.subplot(10,10,i+1)
    plt.imshow(img_data[i],cmap='gray', vmin=0, vmax=255) 
    plt.title(img_tar[i])
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
print(img_tar)
img_data=1-img_data/255
print(img_data[0].shape)


criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,56,0.01)#收敛准则，迭代18次，误差小于0.5
flags=cv2.KMEANS_RANDOM_CENTERS#随机产生初始中心

compactness,labels,centers=cv2.kmeans(img_data.astype(np.float32),10,None,criteria,18,flags)#18为指定使用不同的初始标签执行算法的次数
print(compactness,centers)
#print(labels)
fig,ax=plt.subplots(2,5,figsize=(20,8))
#centers=centers.reshape(10,102,104)
centers=centers.reshape(10,102,104)
for ax1,center in zip(ax.flat,centers):
    ax1.imshow(center,cmap=plt.cm.binary)
#print(labels.shape)#数据为(1797,64)
#print(labels.ravel().shape)

from scipy.stats import mode
print("di_tar=",img_tar)

y_tre=img_tar

from sklearn import metrics
y_pre1=np.zeros_like(labels.ravel())
for i in range(10):
   mask=(labels.ravel()==i)##如果labels.ravel()中的元素等于i,则mask中的元素为true,否则为false
   print(mask)#[False False  True ...  True False  True]共100
   # 
   # 个元素
   #print(mask.shape)#(1791,)
   y_pre1[mask]=mode(img_tar[mask])[0]
   print(y_pre1[mask])
acc1=metrics.accuracy_score(y_pre1,y_tre)
print("acc1=",acc1)
print("y_pre1=",y_pre1)

cf_mat=metrics.confusion_matrix(y_tre,y_pre1)
print(cf_mat)





plt.show()


