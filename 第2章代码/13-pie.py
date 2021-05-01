#13-pie.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=28
plt.figure()
labels=["数学","化学","物理","哲学"]
students=[0.35,0.25,0.10,0.30]#选课学生比例
colors=["red","lightblue","green","pink"]#颜色
explode=(0.1,0.1,0.1,0.1)#间隔距离，半径的比例
plt.pie(students,explode=explode,labels=labels,startangle=45,shadow=True,
        colors=colors,autopct="%3.1f%%")
plt.title("学生选课情况图",fontsize=18)


plt.figure()
x=[0.05,0.08,0.12,0.25, 0.50 ]
labels=['氧化亚氮','臭氧','甲烷','氯氟碳类','二氧化碳'] 
colors=["red","lightblue","green","pink","c"]#颜色
plt.pie(x,labels=labels,startangle=45,shadow=False,
        colors=colors,autopct="%3.1f%%")
plt.title("温室气体比例",fontsize=28)
#添加表格：
title="温室气体比例"
xValue=[[0.05,0.08,0.12,0.25, 0.50 ]]
plt.table(loc='bottom',   # 表格在图表区的位置
          colLabels=labels,    # 表格每列的列名称
          colColours=colors,    # 表格每列列名称所在单元格的填充颜色
          colLoc='center',    # 表格中每列列名称的对齐位置
          colWidths=[0.35]*5,    # 表格每列的宽度,对字体大小有影响        
          cellText=xValue,    # 表格中的数值, 每行数据的列表的列表
          cellLoc='center',    # 表格中数据的对齐位置
          rowLabels=["温室气体比例"] , #表格行名称
          fontsize=18)

plt.show()
