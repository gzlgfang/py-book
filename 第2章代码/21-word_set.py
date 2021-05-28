#21-word_set.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
#设置刻度线朝内
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["lisu"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 28#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
#normal	默认值，正常体
#italic	斜体，这是一个属性
#oblique 将字体倾斜，将没有斜体变量（italic）的特殊字体，要应用oblique
#局部设置字体
from matplotlib.font_manager import FontProperties
font1 = FontProperties(fname='g:\Fonts\simhei.ttf', size=24)
font2 = FontProperties(fname='g:\Fonts\simkai.ttf', size=28,style="oblique",weight=500)
font3 = FontProperties(fname='g:\Fonts\simfang.ttf', size=24,style="oblique",weight=900)
font4 = FontProperties(fname='g:\Fonts\simyou.ttf', size=24,style="oblique",weight=100)
#系统编码设置中文支持
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
#似乎对matplotlib中的中文输出无效果

x=np.arange(11)
for i in range(10):
    plt.plot(x,0*x+(i+1)*5,lw=2)
plt.xlim(0, 10)
plt.ylim(0, 40)
plt.text(1, 35, "我是全局设置大小28号隶书", size=28)
plt.text(1, 31, "我是局部设置大小18号隶书",size=18)
plt.text(1, 26, "我是黑体24号",FontProperties=font1)
plt.text(1, 21, "我是楷体28号",FontProperties=font2)
plt.text(1, 16, "我是仿宋体24号",FontProperties=font3)
plt.text(1, 11, "我是幼体24号",FontProperties=font4)
plt.text(1, 6, "有些字体字库有但Python不一定支持",size=18)
plt.xticks([0,2,4,6,8,10])
plt.show()
#具体字库的名称不同的电脑上可能有些差别，倾斜和加粗功能似乎没有发挥作用

#各种字体名称对照表
#新细明体	PMingLiU
#细明体	MingLiU
#标楷体	DFKai-SB
#黑体	SimHei
#宋体	SimSun
#新宋体	NSimSun
#仿宋	FangSong
#楷体	KaiTi
#仿宋_GB2312	FangSong_GB2312
#楷体_GB2312	KaiTi_GB2312
#微软正黑体	Microsoft JhengHei
#微软雅黑	Microsoft YaHei
#Office
#隶书	LiSu
#幼圆	YouYuan
#华文细黑	STXihei
#华文楷体	STKaiti
#华文宋体	STSong
#华文中宋	STZhongsong
#华文仿宋	STFangsong
#方正舒体	FZShuTi
#方正姚体	FZYaoti
#华文彩云	STCaiyun
#华文琥珀	STHupo
#华文隶书	STLiti
#华文行楷	STXingkai
#华文新魏	STXinwei