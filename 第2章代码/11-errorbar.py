#11-errorbar.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=18
#math_scores=np.random.randint(0,100,1000)#随机产生1000个0-100的整数
#plt.errorbar()
#x：数据点的水平位置
#y：数据点的垂直位置
#yerr：y轴方向的数据点的误差计算方法,可以分上下
#xerr：x轴方向的数据点的误差计算方法，可以分左右
#fmt: 数据点及数据连接线的样式
#ecolor: 误差棒的线条颜色
#elinewidth: 误差棒的线条粗细
#capsize: 误差棒边界横杠的大小
#capthick: 误差棒边界横杠的厚度
#ms: 数据点的大小
#mfc: 数据点的颜色
#mec: 数据点边缘的颜色
#barsabove: bool = ...,
#lolims: bool = ..., 
#uplims: bool = ..., 
#xlolims: bool = ...,
#xuplims: bool = ..., 
# errorevery: int 
#最简单调用figure1
x=np.arange(1,6)
y=[12,16,19,21,28]
yerr,xerr=1,0.2
plt.errorbar(x,y,xerr=xerr,yerr=yerr,fmt='ro:')
plt.title("最简单调用")
#不同误差棒特性调用，figure2
plt.figure()
yerr=[[2,2,1,1,2],[1,2,1,1,1]]
xerr=[0.2,0.1,0.3,0.2,0.4]
plt.errorbar(x,y,xerr=xerr,yerr=yerr,ecolor="b",label="ecolor=b")
plt.errorbar(x+3,y,xerr=xerr,yerr=yerr,fmt="ro:",elinewidth=3,label="elinewidth=3")
plt.errorbar(x+6,y,xerr=xerr,yerr=yerr,fmt="bo:",capsize=3,label="capsize=3")
plt.errorbar(x+9,y,xerr=xerr,yerr=yerr,fmt="go:",capthick=3,label="capthick=3")
plt.legend(fontsize=12)
plt.title("不同误差棒特性调用")
#不同误差大小调用，figure3
plt.figure()
yerr=[[2,2,1,1,2],[1,2,1,1,1]]
xerr=[0.2,0.1,0.3,0.2,0.4]
plt.errorbar(x,y,xerr=xerr,yerr=yerr,label="数据点无连接线")
plt.errorbar(x+3,y,xerr=xerr,yerr=yerr,fmt="ro:",label="红色连接线")
plt.errorbar(x+6,y,xerr=xerr,yerr=yerr,fmt="bo:",lolims=True,label="无下误差线")
plt.errorbar(x+9,y,xerr=xerr,yerr=yerr,fmt="go:",xlolims=True,label="无左误差线")
plt.legend(fontsize=12)
plt.title("不同误差大小调用")
plt.show()