#seaborn plot2
from matplotlib import colors
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import statsmodels.formula.api as smf
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小

DF=pd.read_excel('g:\income.xls','Sheet1', na_filter=False,index_col=0)
y = DF['income']
x1 = DF['age']
x2=DF['Education']
data=pd.DataFrame({"x1":x1,"y":y})
model=smf.ols('y~x1',data)
res_smf=model.fit()
print("statsmodels.formula.api求解：\n",res_smf.summary())
print("res_smf.rsquared=",res_smf.rsquared)
print("res_smf.params=\n",res_smf.params)
print("res_smf.resid=\n",res_smf.resid)
print("res_smf.fittedvalues=\n",res_smf.fittedvalues)
y_fit=res_smf.fittedvalues
plt.figure()
plt.scatter(x1,y,marker='o',color="b")
plt.plot(x1,y_fit,lw=2,color="r")
plt.xlabel("年龄，age")
plt.ylabel("收入，income",labelpad=5)
plt.grid()
plt.title("年龄-收入拟合数据图")
plt.ylim(60000,200000)
plt.xlim(20,60)
plt.show()

#按学历、年龄进行拟合
print("按学历、年龄进行拟合")
data=pd.DataFrame({"x1":x1,"x2":x2,"y":y})
model=smf.ols('y~x1+C(x2)',data)
res_smf=model.fit()
print("statsmodels.formula.api求解：\n",res_smf.summary())
print("res_smf.rsquared=",res_smf.rsquared)
print("res_smf.params=\n",res_smf.params)
print("res_smf.resid=\n",res_smf.resid)
print("res_smf.fittedvalues=\n",res_smf.fittedvalues)

#按学历、年龄、省份进行拟合
print("按学历、年龄、省份进行拟合:")

data=pd.DataFrame({"x1":x1,"x2":x2,"x3":DF['province'],"y":y})
model=smf.ols('y~x1+C(x2)+C(x3)',data)
res_smf=model.fit()
print("statsmodels.formula.api求解：\n",res_smf.summary())
print("res_smf.rsquared=",res_smf.rsquared)
print("res_smf.params=\n",res_smf.params)
print("res_smf.resid=\n",res_smf.resid)
print("res_smf.fittedvalues=\n",res_smf.fittedvalues)