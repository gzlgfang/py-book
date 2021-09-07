#13-k_means_3d.py
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
import cv2
#plt.style.use('ggplot')#引入plt绘制风格
from sklearn.datasets import make_blobs
import matplotlib as mpl
X,kind=make_blobs(n_samples=500,centers=10,n_features=3,cluster_std=1.0,random_state=10)#每簇数据标准差为1
fig=plt.figure()
ax=fig.add_subplot(1,2,1,projection='3d')
x=X[:,0]
y=X[:,1]
z=X[:,2]
p=ax.scatter(x,y,z,s=10, c=kind,cmap=mpl.cm.seismic,marker="o",zdir="z")
fig.colorbar(p, ax=ax,shrink=0.8)

criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,18,0.8)#收敛准则，迭代18次，误差小于1
flags=cv2.KMEANS_RANDOM_CENTERS#随机产生初始中心
compactness,labels,centers=cv2.kmeans(X.astype(np.float32),10,None,criteria,8,flags)
print(compactness,centers)
ax=fig.add_subplot(1,2,2,projection='3d')

x=centers[:,0]
y=centers[:,1]
z=centers[:,2]
p=ax.scatter(x,y,z,s=200, c="r",alpha=0.8,zdir="z")
x=X[:,0]
y=X[:,1]
z=X[:,2]

p=ax.scatter(x,y,z,s=10, c=labels,cmap=mpl.cm.seismic,marker="o",alpha=0.8,zdir="z")
fig.colorbar(p, ax=ax,shrink=0.8)

plt.show()
cv2.waitKey(delay=-1)