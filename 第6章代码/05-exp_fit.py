# y=ae^bx  fit 指数拟合
#05-exp_fit.py
from scipy import optimize as op
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
xdata=np.array([1,2,3,4,5,6,7,8])
y_real=np.array([15.3,20.5,27.4,36.6,49.1,65.6,87.8,117.6])
#拟合函数
def func(x, a,  b):
        return  a*np.exp(b*x)
alf_opt,alf_cov=op.curve_fit(func,xdata,y_real)
print('alf=',alf_opt)
plt.figure(num="拟合曲线绘制",figsize=(8,8))
plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
plt.xlabel("x",fontname="serif")
plt.ylabel("y",labelpad=5,fontname="serif")
ydata=func(xdata,*alf_opt)
eer=sum((y_real-ydata)**2)/len(y_real)
print('eer=',eer)
plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.text(0.2,90,f'均方误差={eer:.5f}' )

plt.text(0.2,80,f'拟合方程：y={alf_opt[0]:.5f}e$^{{0.29141}}$')#{}
plt.xlim(0,9)#设置x轴范围
plt.ylim(10,120)
plt.legend()
plt.show()



