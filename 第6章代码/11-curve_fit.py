#10-curve_fit.py
#curve_fit(f, xdata, ydata, p0=None, sigma=None, absolute_sigma=False, check_finite=True, bounds=(-inf, inf), method=None, jac=None, **kwargs)
#Use non-linear least squares to fit a function, f, to data.
# Assumes ``ydata = f(xdata, *params) + eps``.
from scipy import optimize as op
import scipy as scp 
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
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
xdata=np.linspace(1,10,10)#自变量
#y_real=3+2.0*xdata+1.0*xdata**2+np.random.random(10)#应变量
#设置拟合方程
def func(x, a0,  a1, a2):
        return  a0+a1*x+a2*x**2
y_real=func(xdata,3,2.0,1.0)+np.random.random(10)
fit_cc,fit_cv=op.curve_fit(func,xdata,y_real)#拟合曲线curvefit方法
print(fit_cc)

#另一种方法拟合polynomial
poly_cc=np.polynomial.Polynomial.fit(xdata,y_real,2,window=[1,10])#2次拟合，可以选择其他次数
print(poly_cc)
print(poly_cc.coef)

#最小二乘拟合
def J(alfai):
    return y_real-func(xdata,*alfai)
alf0=[1,1,1]
alf_opt,alf_cov=op.leastsq(J,alf0)
print('alf=',alf_opt)

plt.figure(num="拟合曲线绘制",figsize=(8,8))
plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
plt.xlabel("x",fontname="serif")
plt.ylabel("y",labelpad=5,fontname="serif")

#ydata=func(xdata,fit_cc[0],fit_cc[1],fit_cc[2])
ydata=func(xdata,*fit_cc)
plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.xlim(0,11)#设置x轴范围
plt.legend()
plt.show()