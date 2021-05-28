#10-boxplot.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=18
math_scores=np.random.randint(0,100,1000)#随机产生1000个0-100的整数
plt.boxplot(math_scores)#绘制默认箱线图
plt.figure()
data=[1,2,4,6,8,12,15,18,23,45,67,87]
w=np.percentile(data,[0,25,50,75])
print("w=",w)
plt.boxplot(data)
plt.figure()
#全参数调用
#plt.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None,
#  widths=None, patch_artist=None, bootstrap=None, usermedians=None,
#  conf_intervals=None, meanline=None, showmeans=None, showcaps=None,
#  showbox=None, showfliers=None, boxprops=None, labels=None,
#  flierprops=None, medianprops=None, meanprops=None, capprops=None,
#  whiskerprops=None, manage_xticks=True, autorange=False, zorder=None, * data=None)
#参数含义
#x 绘制箱线图数据
#notch 是否显式凹痕箱体
#sym   离群数据点图形
#vert     是否需要将箱线图垂直摆放，默认False
#whis   用以计算上下须与上下四分位的距离的参数，默认为1.5；
#positions   指定箱线图的位置；
#widths    指定箱线图的宽度，默认为0.5；
#patch_artist     是否填充箱体的颜色，默认False；
#meanline     是否用线的形式表示均值，默认用点来表示；
#showmeans   是否显示均值，默认不显示；
#showcaps     是否显示箱线图顶端和末端的两条线，默认显示；
#showbox    是否显示箱线图的箱体，默认显示；
#showfliers   是否显示异常值，默认显示；
#boxprops   设置箱体的属性，如边框色，填充色等；
#labels    为箱线图添加标签，类似于图例的作用；
# flierprops  设置异常值的属性，如异常点的形状、大小、填充色等；
#medianprops   设置中位数的属性，如线的类型、粗细等；
#meanprops   设置均值的属性，如点的大小、颜色等；
#capprops     设置箱线图顶端和末端线条的属性，如颜色、粗细等；
#whiskerprops   设置须的属性，如颜色、粗细、线的类型等

colors=["r","b","m"]
labels=["白玉兰","细叶榕","阔叶榕"]
d1=[3.1,2.9,2.5,3.01,3,4.1,3.1,2.8,2.9,2.0,3.11,2.89,2.3,3.3,3.2,3,4,3.5,2.6,2.8,3.6,4.1,2.2]
d2=d1-2*np.ones(len(d1))+0.2*np.random.random(len(d1))
d3=d1-np.ones(len(d1))-0.1*np.random.random(len(d1))
x=[d1,d2,d3]
width=[0.5,0.5,0.5]
whis=1.2
flp1={'marker': 'o', 'markersize':16,'markerfacecolor' : 'red','color' : 'black'}
ax1=plt.subplot(121)
#p_box=plt.boxplot(x,whis=whis,widths=width,sym="o",flierprops=flp1,labels=labels,patch_artist=True)
p_box=ax1.boxplot(x,whis=whis,widths=width,sym="o",flierprops=flp1,labels=labels,patch_artist=True)
for patch,color in zip(p_box["boxes"],colors):
    patch.set_facecolor(color)
plt.ylabel("树叶的长宽比",fontsize=18)
plt.title("三种不同树叶长宽比统计数据比较",fontsize=18)
plt.grid(True,ls=":",lw=2,c="b")
##plt.figure()
colors=['orangered', 'goldenrod', 'orchid']
flp2={'marker': '*', 'markersize':12,'markerfacecolor' : 'blue','color' : 'black'}
 #设置异常值属性，点的形状，填充色和边框色
ax2=plt.subplot(122)
p_box=ax2.boxplot(x,whis=whis,widths=width,sym="*",flierprops=flp2,labels=labels,patch_artist=True,vert=False)
#p_box=plt.boxplot(x,whis=whis,widths=width,sym="*",flierprops=flp2,labels=labels,patch_artist=True,vert=False)
for patch,color in zip(p_box["boxes"],colors):
    patch.set_facecolor(color)
plt.xlabel("树叶的长宽比",fontsize=18)
plt.title("三种不同树叶长宽比统计数据比较",fontsize=18)
plt.grid(True,ls=":",lw=2,c="b")



plt.show()