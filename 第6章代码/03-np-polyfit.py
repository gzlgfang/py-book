#03-np-polyfit
import numpy as np
#给定实验数据
x=np.array([-4,-3,-2,-1,0,1,2,3,4])#自变量
y=np.array([6.2,2.6,0.48,0.56,2.4,6.7,12.3,20.7,30.2])#应变量
coef1=np.polyfit(x,y,deg=3)
print("coef1=",coef1)

coef2=np.polynomial.Polynomial.fit(x, y, deg=2, window=[min(x),max(x)])
print("coef2=",coef2)
ydata=coef2(x)
print("ydata=",ydata)