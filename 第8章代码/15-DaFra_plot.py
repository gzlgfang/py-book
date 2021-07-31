#DataFrame Plot
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as mticker
from numpy.lib.function_base import rot90
import pandas as pd
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小
DF=pd.read_excel('g:\city_gdp.xls','Sheet1', na_filter=False,index_col=0)
DF_city_top8=DF.province.value_counts().head(8)
fig, ax = plt.subplots(figsize=(9, 9))#绘制柱体图
DF_city_top8.plot(kind="bar",ax=ax,color="blue",align="center")
plt.ylabel("GDP50城市数目")
plt.xlabel("所在省",labelpad=5)
#plt.xticks.set_rotation=90
plt.legend()
plt.grid()
plt.show()
