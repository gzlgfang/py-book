import matplotlib.pyplot as plt
import numpy as np
import cv2
plt.style.use('ggplot')#引入plt绘制风格
from sklearn.datasets import make_blobs
import matplotlib as mpl
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 16#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细

#①数据准备
X,kind=make_blobs(n_samples=500,centers=5,n_features=2,cluster_std=1.0,random_state=10)#每簇数据标准差为1
#print(kind)#类别
plt.scatter(X[:,0],X[:,1],s=120, c=kind,cmap=mpl.cm.RdYlBu)

#②算法测试
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,18,0.8)#收敛准则，迭代18次，误差小于1
flags=cv2.KMEANS_RANDOM_CENTERS#随机产生初始中心

compactness,labels,centers=cv2.kmeans(X.astype(np.float32),5,None,criteria,8,flags)

print("compactness=",compactness)
print("centers=",centers)
print("labels=\n",labels.ravel())
print(type(centers))
plt.figure()
plt.scatter(X[:,0],X[:,1],s=80, c=labels,cmap=mpl.cm.seismic)
plt.scatter(centers[:,0],centers[:,1],s=280, c="k",alpha=1)#s为标记大小，c为标记颜色
#③算法应用
plt.figure()
plt.scatter(X[:,0],X[:,1],s=80, c=labels,cmap=mpl.cm.seismic)
plt.scatter(centers[:,0],centers[:,1],s=280, c="k",alpha=1)#s为标记大小，c为标记颜色
#  
#new_data=eval(input("请利用[*,*]形式输入需要归类的数据new_data="))
#随机产生5个点
new_data=np.random.randint(-10, 10, size=(10, 2))
num=len(centers)
distance=np.zeros(num)
for j in range(10):
    for i,center in enumerate(centers):
         distance[i] =(new_data[j,0]-center[0])**2+(new_data[j,1]-center[1])**2
    print("distance=",distance)
    #print(type(distance))
    distance=list(distance)
    id_min_dist=distance.index(min(distance))

    print("id_min_dist=",id_min_dist)
    print("找到归类的簇心数据=",centers[id_min_dist])


    plt.scatter(new_data[j,0],new_data[j,1],s=400, c="red",alpha=1)#s为标记大小，c为标记颜色
    xy=(centers[id_min_dist,0],centers[id_min_dist,1])
    xytext=(new_data[j,0],new_data[j,1])
    plt.annotate('',xy=xy,xytext=xytext ,bbox=dict( facecolor=None,alpha=0.5,edgecolor=None,lw=0),
               arrowprops=dict(arrowstyle='<->',color="g",lw=2))


plt.show()