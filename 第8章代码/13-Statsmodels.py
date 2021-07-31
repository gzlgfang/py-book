#statsmodels 
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import patsy as py

#绘图设置
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 16#设置字体大小


x1=np.random.randn(50)
x2=np.random.randn(50)
y=6+3*x1+5*x2+8*x1*x2+0.3*np.random.randn(50)
data=pd.DataFrame({'x1':x1,'x2':x2,'y':y})
#print(data)
#用statsmodels.api求解sm：
M=np.vstack((np.ones_like(x1),x1,x2,x1*x2)).T
res_sm=sm.OLS(y, M).fit()  
print("statsmodels.api求解：\n",res_sm.summary())   
#用statsmodels.formula.api求解smf：
model=smf.ols('y~x1+x2+x1:x2',data)
res_smf=model.fit()
print("statsmodels.formula.api求解：\n",res_smf.summary())
print("res_smf.rsquared=",res_smf.rsquared)
print("res_smf.params=\n",res_smf.params)
print("res_smf.resid=\n",res_smf.resid)
print("res_smf.fittedvalues=\n",res_smf.fittedvalues)
print(type(res_smf.fittedvalues))





#绘制实际数据图和拟合数据图
x=np.linspace(-2,2,100)
X1,X2=np.meshgrid(x,x)
y_true=6+3*X1+5*X2+8*X1*X2
#print(y_true)
new_data=pd.DataFrame({"x1":X1.ravel(),'x2':X2.ravel()})
#print(X1.ravel()[200:300])
#print("new_data:\n",new_data)
y_pre=res_smf.predict(new_data)#一维数据
print(type(y_pre))
y_pre=y_pre.values.reshape(100,100)

def title_and_lab(ax, title):#常规坐标轴特性设置，可通用
    ax.set_title(title)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
fig,ax=plt.subplots(1,2,figsize=(18,9))
fig1=ax[0].contourf(X1,X2,y_true,cmap=mpl.cm.copper)
cb1=fig.colorbar(fig1, ax=ax[0], shrink=0.8)
title_and_lab(ax[0], "y_true_contour")
cb1.set_label(r"$y$")
fig2=ax[1].contourf(X1,X2,y_pre,cmap=mpl.cm.copper)
cb2=fig.colorbar(fig2, ax=ax[1], shrink=0.8)
title_and_lab(ax[1], "y_pre_contour")
cb2.set_label(r"$y$")

#用底层np.linalg.lstsq求解
#M=np.vstack((np.ones_like(x1),x1,x2,x1*x2)).T
res_ls=np.linalg.lstsq(M, y,rcond=-1)[0]#打印拟合参数a0,a1,a2,a3
print("Numpy库底层np.linalg.lstsq求解：\n",res_ls)


#广义线性模型：实际是非线性模型拟合，y=a0+a1*x1**2+a2*x2+a3*x1*ln(x2)

x1=np.random.randn(50)
x2=np.abs(np.random.randn(50))
y=2+6*x1**2+3*x2+9*x1*np.log(x2)+0.5*np.random.randn(50)
data=pd.DataFrame({'x1':x1,'x2':x2,'y':y})
#print(data)
#用statsmodels.api求解sm：
M=np.vstack((np.ones_like(x1),x1*x1,x2,x1*np.log(x2))).T
res_sm=sm.OLS(y, M).fit()  
print("statsmodels.api求解：\n",res_sm.summary())   
#用statsmodels.formula.api求解smf：
model=smf.ols('y~I(x1**2)+x2+I(x1*np.log(x2))',data)
res_smf=model.fit()
print("statsmodels.formula.api求解：\n",res_smf.summary())

#用statsmodels.formula.api求解smf无常数项无交互项
model=smf.ols('y~-1+I(x1**2)+x2+I(x1*np.log(x2))',data)
res_smf=model.fit()
print("statsmodels.formula.api求解无常数项：\n",res_smf.summary())

#用statsmodels.formula.api求解smf无交互项
model=smf.ols('y~I(x1**2)+x2',data)
res_smf=model.fit()
print("statsmodels.formula.api求解无交互项：\n",res_smf.summary())




#用底层np.linalg.lstsq求解
#M=np.vstack((np.ones_like(x1),x1,x2,x1*x2)).T
res_ls=np.linalg.lstsq(M, y,rcond=-1)#打印拟合参数a0,a1,a2,a3
print("Numpy库底层np.linalg.lstsq求解：\n",res_ls)
plt.show()