#27-twinxy
import matplotlib.ticker as mticker
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字

#设置刻度线朝内
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
#normal	默认值，正常体
# 均值、标准差、shape
flow = np.random.normal(160, 60, 300)#共300个随机数，均值为160
print(flow)
speed = np.random.normal(30, 12, 300)
x = np.arange(0, 24, 24/300)
# 自定义字体
font1 = {'family': 'Times New Roman'}     
fig, ax1 = plt.subplots(figsize=(16, 6))
# 设置第一纵坐标轴的单位
ax1.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d km/h'))
# 自定义横轴
ax1.set_xticks([i for i in range(0, 25, 2)])
ax1.set_xticklabels([str(i)+':00' for i in range(0, 25,2)],font1)
ax1.tick_params(labelsize=18)
ax1.plot(x, speed, 'r', label="车速",ls="--")
ax1.grid()# 显示网格
ax1.set_xlabel("时间",fontsize=18)
ax1.set_ylabel('车速',fontsize=18)
ax1.set_ylim(0,70)
ax1.set_title("共享时间坐标",fontsize=18)
# 设置图例的位置
ax1.legend(loc='upper left',fontsize=18)
# 第二纵轴的设置和绘图
ax2 = ax1.twinx()
ax2.plot(x, flow, 'g', label="车流")
ax2.legend(loc='upper right',fontsize=18)
ax2.tick_params(labelsize=18)
ax2.set_ylabel("车流",fontsize=18)
ax2.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d 辆/h'))
# 限制横轴显示刻度的范围
plt.xlim(0, 24)
plt.show()
