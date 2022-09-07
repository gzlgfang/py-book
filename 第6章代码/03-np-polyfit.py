#03-np-polyfit
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt

#设置刻度线朝内
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 16#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
#给定实验数据
x=np.array([-4,-3,-2,-1,0,1,2,3,4])#自变量
y=np.array([6.2,2.6,0.48,0.56,2.4,6.7,12.3,20.7,30.2])#应变量
coef1=np.polyfit(x,y,deg=3)
print("coef1=",coef1)
#ydata1=coef1(x)
#print(ydata1)
coef2=np.polynomial.Polynomial.fit(x, y, deg=2, window=[min(x),max(x)])
print("coef2=",coef2)
ydata=coef2(x)
print("y_real=",y)
print("y_cal=",ydata)
fig=plt.figure(num="拟合曲线绘制",figsize=(8,8))
plt.scatter(x,y,color="red",label='实验数据')#绘制数据点
plt.xlabel("x",fontname="serif")
plt.ylabel("y",labelpad=5,fontname="serif")
plt.plot(x,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
eer=sum((y-ydata)**2)
plt.text(-1,15,f'均方误差={eer:.5f}' )
plt.text(-1,18,coef2 )
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)

plt.legend()
plt.show()