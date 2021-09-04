from sklearn.neighbors import NearestCentroid
import numpy as np




X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])
clf = NearestCentroid()
clf.fit(X, y)
print(clf.predict([[-0.8, -1]]))





from sklearn.neighbors import DistanceMetric
dist = DistanceMetric.get_metric('euclidean')
X = [[0, 1, 2,6], [0, 1, 2,6]]

pd=dist.pairwise(X)
print("pd:\n",pd)

X1 = [[0], [3],[4]]
pd=dist.pairwise(X1)
print("pd1:\n",pd)


X = [[0, 1, 2,6], [0, 7, 3,2]]
Y=[[5, 4, 3,6], [1, 8, 2,6]]
pd=dist.pairwise(X,Y)
print("pd2:\n",pd)

X = [[0, 1, 2,6], [0, 7, 3,2]]
Y=X
pd=dist.pairwise(X,Y)
print("pd2:\n",pd)



