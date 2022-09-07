#08-five_var_fit.py

from scipy import optimize as op
import numpy as np
# DF1 = pd.read_csv("data1.csv")   #, "Sheet1",na_filter=False, index_col=0# 共有31个城市坐标
# data_x = np.array(DF1["x"])  # 数据分配
# data_y = np.array(DF1["y"])

#输入统计数据
x0=np.linspace(45,100,12)
x1=np.linspace(5,38,12)
x2=np.linspace(1.5,18,12)
x3=np.linspace(12.5,40,12)
x4=np.linspace(0.8,9.6,12)
y_real=np.array([34.13,47.67,64.89,85.56,109.56,136.78,167.17,200.68,237.27,276.92,319.58,365.25])
x=np.array([x0,x1,x2,x3,x4])
def func(x,a0,a1,a2,a3,a4,a5):
    return a0+a1*x[0]**0.5+a2*x[1]**1.2+a3*x[2]**1.5+a4*x[3]+a5*x[4]**2
#a=[2,1.5,0.6,0.9,1.2,2]
#print(func(x,*a))
fit_cc,fit_cv=op.curve_fit(func,x,y_real,p0=[2,1.5,0.6,0.9,1.2,2])#拟合曲线curvefit方法
print(f'a_0={fit_cc[0]:.5f},a_1={fit_cc[1]:.5f}, a_2={fit_cc[2]:.5f},a_3={fit_cc[3]:.5f},a_4={fit_cc[4]:.5f}, a_5={fit_cc[5]:.5f}')
ydata=func(x,*fit_cc)
print('ydata=:\n',ydata)
#计算绝对百分误差平均值
abseer=np.mean(abs(y_real-ydata)/ydata)*100
print("abseer=",f'{abseer:.5f}',"%")