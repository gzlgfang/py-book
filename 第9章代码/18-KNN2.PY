#17-KNN2.py
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib as mpl
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] =28#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
#①数据准备
from sklearn import datasets
digits=datasets.load_digits()
print(digits.images.shape)

X_train=digits.images[0:500].reshape(500,-1)
#KNN需要传入一个矩阵，而不能是一个数组。reshape()成一个二维数组，第一个参数是500表示500个数据，第二个参数-1，numpy自动决定第二维度有多少
print(X_train.shape)

y_train=digits.target[0:500]
#print(y_train)
print(len(y_train))

#②算法测试
from sklearn import metrics
n_neighbors=10

#print("n_neighbors=",n_neighbors)
acc=np.zeros(100)
y_tre =digits.target[500:1000] 
for i in range(100):
    n_neighbors=i+1
# 创建kNN_classifier实例
    KNN_CF = KNeighborsClassifier(n_neighbors=n_neighbors)
# kNN_CF做一遍fit(拟合)的过程，没有返回值，
# 模型就存储在kNN_CF实例中
    K_model=KNN_CF.fit(X_train, y_train)
#print(K_model)

    X_test=digits.images[500:1000].reshape(500,-1)
    
#print(y_tre)
    y_pre = K_model.predict(X_test)
   
    acc[i]=metrics.accuracy_score(y_pre,y_tre)
   #print("acc=",acc)
#图形绘制
plt.figure()
x_n=np.arange(100)+1
plt.plot(x_n,acc,lw=2,marker="o",color='#1f77b4')#
plt.grid()
plt.xlim(0,100)
plt.ylim(0.7,1)
plt.xlabel("邻居数目,n_neighbors")
plt.ylabel("算法准确率,acc")
plt.title("算法邻居数目和测试集准确度关系")
plt.show()





