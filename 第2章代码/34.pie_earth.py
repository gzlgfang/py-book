#33.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=16
#explode=(0.1,0.1,0.1,0.1)#间隔距离，半径的比例
#plt.pie(students,explode=explode,labels=labels,startangle=45,shadow=True,
        #colors=colors,autopct="%3.1f%%")
# 氧（46.6%）、（27.7%）、（8.1%）、（5.0%）、（3.6%）、（2.8%）、（2.6%）、（2.1%），其他.
cy_col= ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']
plt.figure()
x=[0.466,0.277,0.081,0.050,0.036,0.028,0.026,0.021,0.015]
labels=['氧','硅','铝','铁','钙','钠','钾','镁','其他'       ] 
wedges,texts,autotexts=plt.pie(x,startangle=45,shadow=False,
        colors=cy_col,autopct="%3.1f%%",textprops=dict(color="w"))
plt.text(-0.20,-1.15,"地壳元素含量表",)
#添加表格：
title="地壳元素含量"
xValue=np.zeros(9)
for i in range(9):
    xValue[i]=int(x[i]*100*10)/10
xValue=[xValue]

plt.table(loc='bottom',   # 表格在图表区的位置
          colLabels=labels,    # 表格每列的列名称
          colColours=None,    # 表格每列列名称所在单元格的填充颜色
          colLoc='center',    # 表格中每列列名称的对齐位置
          colWidths=[0.15]*9,    # 表格每列的宽度,对字体大小有影响        
          cellText=xValue,    # 表格中的数值, 每行数据的列表的列表
          cellLoc='center',    # 表格中数据的对齐位置
          rowLabels=["含量,%"] , #表格行名称
          fontsize=16 )
plt.legend(wedges, labels,loc='center left',title="元素名称",bbox_to_anchor=(0.9,0,0.3,1))
#plt.setp(texts,size=18)
plt.show()