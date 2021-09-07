import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
import matplotlib as mpl
mpl.rcParams["font.size"] = 16#设置字体大小
#plt.style.use('ggplot')#引入plt绘制风格

X_train = np.array([[-1, -1], [-2, -1], [-3, -2], [-1, 0.5], [-2, 1], [-3, 1],
        [4, 4], [3, 4], [2, 3], [4, 5.5], [3, 6], [2, 6],
        [9, -1], [8, -1], [7, -2], [9, 0.5], [8, 1], [7, 1]])

y_train = ["A","A","A","A","A","A","B","B","B","B","B","B","C","C","C","C","C","C"]
lb=MultiLabelBinarizer()
y_train_mulb=lb.fit_transform(y_train)#标签由字母转换成数字
print(y_train_mulb)
plt.scatter(X_train[:,0],X_train[:,1],s=300, c=y_train_mulb,cmap=mpl.cm.seismic)
X_test=np.array([[-0.5, -1.5], [3.1, 1.7], [-1.3, -2.4],[7,0]])
plt.scatter(X_test[:,0],X_test[:,1],s=500, marker="*",c="purple")

# 创建kNN_classifier实例
KNN_CF = KNeighborsClassifier(n_neighbors=5)
# kNN_CF做一遍fit(拟合)的过程，没有返回值，
# 模型就存储在kNN_CF实例中
K_model=KNN_CF.fit(X_train, y_train_mulb)
print(K_model)
# KNN进行预测predict，需要传入一个矩阵，而不能是一个数组。reshape()成一个二维数组，第一个参数是1表示只有一个数据，第二个参数-1，numpy自动决定第二维度有多少
y_predict = K_model.predict(X_test)
print(y_predict)
y_predict =np.array(lb.inverse_transform(y_predict)).reshape(-1)#标签反向逆转
print(y_predict)
for i ,X in enumerate(X_test):
    plt.text(X[0]+0.3,X[1]-0.2,y_predict[i] )
plt.grid()
plt.show()#,bbox=dict( facecolor="w",alpha=1,edgecolor=None,lw=0)

