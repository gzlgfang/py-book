# Temperature-pressure  fit 
#04-tem_pre-fit.py
from scipy import optimize as op
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt
import pandas as pd
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
xdata=np.array([283,293,303,313,323,333,343])
y_real=np.array([35,120,210,380,520,680,790])
# 读入拟合数据
DF1 = pd.read_csv("data1.csv")   #, "Sheet1",na_filter=False, index_col=0# 共有31个城市坐标
data_x = np.array(DF1["x"])  # 数据分配
data_y = np.array(DF1["y"])
xdata=data_x
y_real=data_y
print(data_x,data_y)
#拟合函数
def func(x, a,  b, c):
        return  np.exp(a+b/(x+c))
#最小二乘拟合
def J(alfai):
    return y_real-func(xdata,*alfai)
alf0=[5,-1,1]#初值对拟合结果有较大影响
alf_opt,alf_cov=op.leastsq(J,alf0,maxfev=10000)
print('alf=',alf_opt)
plt.figure(num="拟合曲线绘制",figsize=(8,8))
plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
plt.xlabel("x",fontname="serif")
plt.ylabel("y",labelpad=5,fontname="serif")
ydata=func(xdata,*alf_opt)
plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
eer=sum((y_real-ydata)**2)
print(ydata)
plt.text(min(xdata),0.8*max(y_real),f'均方误差={eer:.5f}' )
plt.text(min(xdata),0.6*max(y_real),f'拟合方程：lnp={alf_opt[0]:.5f}{alf_opt[1]:.5f}/(x+{alf_opt[2]:.5f})' )
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.xlim(min(xdata)-2,max(xdata)+2)#设置x轴范围
plt.ylim(min(y_real)-50,max(y_real)+50)#设置
plt.legend()
plt.show()

