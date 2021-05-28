#24-marker_set.py
import numpy as np
import matplotlib.pyplot as plt
#loc=1,2,3,4=右上角，左上角，左下角，右下角=uper right,upper left,lower left,lower right
fig, ax = plt.subplots(figsize=(16, 9))
mks = ['.',',', 'o', 'v','^','<','>','1','2','3','4','s','p','*','H','h','X','x','D','d','|','+']#mks=marker styles
dic = {
    1: 'red',
    2: 'orange',
    3: 'yellow',
    4: 'green',
    5: 'blue',
    6: 'purple',
    7: 'pink',
    8: 'purple'}
x = np.arange(1,6)
for n,mks  in enumerate(mks):#color=dic[n%8+1]#
    ax.plot(x, 0 * x+n, lw=1,ls="-.",marker=mks,label=mks,color="k",markersize=12)#利用0和x相乘再加n产生列表数据，也可以y=np.zeros.like(x)+n
ax.legend(ncol=11, loc='lower left',bbox_to_anchor=(0, 1), fontsize=15)#nocl表示图例分为多少列，loc表示图例位置
plt.subplots_adjust(top=0.8)  # the top of the subplots of the figure图片中子图的顶部的高度
plt.xticks([])#消除坐标刻度和标签
plt.yticks([])
plt.show()