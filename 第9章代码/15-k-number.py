##14-k-n
import cv2
from sklearn import datasets
import matplotlib.pyplot as plt 
import numpy as np 
digits=datasets.load_digits()
print(digits.data.shape)
#print(digits.data)
print("dsd")
#print(digits.images)
img=digits.images/16
#print(img[6])
#plt.imshow(img[6],cmap="gray")

criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,18,0.5)#收敛准则，迭代18次，误差小于0.5
flags=cv2.KMEANS_RANDOM_CENTERS#随机产生初始中心

compactness,labels,centers=cv2.kmeans(digits.data.astype(np.float32),10,None,criteria,8,flags)#8为指定使用不同的初始标签执行算法的次数
#print(compactness,centers)
fig,ax=plt.subplots(2,5,figsize=(20,8))
centers=centers.reshape(10,8,8)
for ax1,center in zip(ax.flat,centers):
    ax1.imshow(center,cmap=plt.cm.binary)
print(labels[0:100])#数据为(1797,64)
#print(labels.ravel().shape)
print(labels.ravel()) #数据降维为(1797,)
y_pre=labels.ravel()
from scipy.stats import mode
print("di_tar=",digits.target)
print("di_tar=",digits.target[0])
y_tre=digits.target

from sklearn import metrics
acc=metrics.accuracy_score(y_pre,y_tre)
print("acc=",acc)
y_pre1=np.zeros_like(labels.ravel())
for i in range(10):
   mask=(labels.ravel()==i)##如果labels.ravel()中的元素等于i,则mask中的元素为true,否则为false
   #print(mask)#[False False  True ...  True False  True]共1797个元素
   #print(mask.shape)#(1791,)
   y_pre1[mask]=mode(digits.target[mask])[0]
   print(y_pre1[mask])
acc1=metrics.accuracy_score(y_pre1,y_tre)
print("acc1=",acc1)
print("y_pre1=",y_pre1)

cf_mat=metrics.confusion_matrix(y_tre,y_pre1)
print("cf_mat=\n",cf_mat)

plt.show()