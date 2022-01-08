import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
import cv2
from scipy.stats import mode
iris=datasets.load_iris()#从datasets输入数据
print(iris)

mpl.rcParams["font.size"] = 28#设置字体大小
#设置刻度线朝内
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
mpl.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 16#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True

#plt.style.use('ggplot')#引入plt绘制风格
X=np.array(iris.data[0:100,0:3:1])#将第1列、第2列、第3列数据转换成数组，以便进行聚类处理
y_tre=iris.target[0:100]

#算法测试
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,50,0.4)#收敛准则，迭代50次，误差小于0.4
flags=cv2.KMEANS_RANDOM_CENTERS#随机产生初始中心
compactness,labels,centers=cv2.kmeans(X.astype(np.float32),2,None,criteria,8,flags)
print("compactness=",compactness)
print("centers=",centers)
print("labels=\n",labels.ravel())#降维处理由原来的[[],[],[],...]变为[*,*,...]
print(type(centers))

y_pre=labels.ravel()#仅仅是分类，但不知定义的类别和实际数据标签的类别分类是否一致，需要通过mode函数
from sklearn import metrics
acc=metrics.accuracy_score(y_pre,y_tre)
print(y_pre,y_tre)
print("acc=",acc) #预测准确率,其实可能是不正确率

y_pre1=np.zeros_like(labels.ravel())
for i in range(2):
   mask=(labels.ravel()==i)##如果labels.ravel()中的元素等于i,则mask中的元素为true,否则为false
   #print(mask)#[False False  True ...  True False  True]共100个元素
   #print(mask.shape)#(100,)
   y_pre1[mask]=mode(y_tre[mask])[0]
   print(y_pre1[mask])
acc1=metrics.accuracy_score(y_pre1,y_tre)
print("acc1=",acc1)
print("y_pre1=",y_pre1)#预测准确率(实际的）


fig=plt.figure()
ax=fig.add_subplot(projection='3d')

#fig.colorbar(p, ax=ax,shrink=0.8)
p=ax.scatter(X[:50,0],X[:50,1],X[:50,2],s=200, c=labels[:50],cmap=mpl.cm.seismic,marker="*",label='setosa',zdir="z")
p=ax.scatter(X[50:100,0],X[50:100,1],X[50:100,2],s=200, c=labels[50:100],cmap=mpl.cm.seismic,marker="+",label='versicolor',zdir="z")
p=ax.scatter(centers[:,0],centers[:,1],centers[:,2],s=280, c="r",alpha=1)#s为标记大小，c为标记颜色
ax.set_xlabel('萼片长度(cm)',fontsize=24,labelpad=10)
ax.set_ylabel('萼片宽度(cm)',fontsize=24,labelpad=10)
ax.set_zlabel('花瓣长度(cm)',fontsize=24,labelpad=10) 
plt.grid()                 
plt.legend(loc='upper left',fontsize=24)
plt.xlim(4,7.5)
plt.ylim(0.5,5.5)
plt.show()
     
