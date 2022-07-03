import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
import matplotlib  as mpl
#全局设置字体
mpl.rcParams["font.sans-serif"]=["FangSong"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 18#设置字体大小
#mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
font1 = {'family': 'Times New Roman'} 
labels=['最近7日活跃人数','学习者总规模','论坛发帖回复率','讨论区人均互动次数','讨论区参与规模']

#labels=['数学','语文',  '英文',' 物理','化学']
data1=np.array([95,90,93,86,80])#五个方面的数据，与平均值相比的百分数，超过平均值取100
N=len(data1)#计算数据长度
angles = np.linspace(0, 2*np.pi, N+1)

# 使雷达图数据封闭
data_1 = np.concatenate((data1, [data1[0]]))#数列组合

labels = np.concatenate((labels, [labels[0]]))
fig1 = plt.figure(figsize=(8,6), dpi=100)
ax1 = plt.subplot(111, polar=True)
# 绘制雷达图
ax1.plot(angles, data_1, color='b',marker='o',linewidth=1,markersize=12)
ax1.fill(angles, data_1, color='pink')
plt.xticks(angles,labels=labels,size=16)
# 设置雷达图中每一项的标签显示
#ax.set_thetagrids(angles*180/np.pi, labels)
ax1.set_rlim(0, 100)
ax1.set_theta_offset(np.pi/2-np.pi/N)#保证第一类与最后一类的空间放在正上方，单位为弧度

ax1.set_theta_direction(-1)
#方法用于设置极径标签显示位置,参数为标签所要显示在的角度
ax1.set_rlabel_position(180)#单位为360度值
ax1.spines['polar'].set_visible(False)
#ax.grid(False)
ax1.set_title("慕课学习健康图")
#ax1.set_title("李四课程学习健康图")
       
#plt.legend(["计算机辅助设计"], loc='best',bbox_to_anchor=(1, 0.5, 0, 0.1))
fig2 = plt.figure(figsize=(8,6), dpi=100)
ax2 = plt.subplot(111, polar=True)
# 绘制雷达图
ax2.plot(angles, data_1, color='b',marker='o',linewidth=1,markersize=12)
plt.xticks(angles,labels=labels,size=16)

# 设置雷达图的0度起始位置
ax2.set_theta_zero_location("E")#默认为东方
# 设置雷达图的坐标刻度范围
ax2.set_rlim(0, 100)
ax2.set_theta_offset(np.pi/2-np.pi/N)#保证第一类与最后一类的空间放在正上方，单位为弧度
ax2.set_theta_direction(-1)
#方法用于设置极径标签显示位置,参数为标签所要显示在的角度
ax2.set_rlabel_position(180)#单位为360度值
ax2.spines['polar'].set_visible(False)
#ax.grid(False)
ax2.set_title("慕课学习健康图")
#ax2.set_title("李四课程学习健康图")         
#plt.legend(["计算机辅助设计"], loc='best',bbox_to_anchor=(1, 0.5, 0, 0.1))

#两门课程
data2=np.array([80,85,90,95,90])#计算机化工应用
data_2 = np.concatenate((data2, [data2[0]]))#数列组合
fig = plt.figure(figsize=(8,6), dpi=100)
ax = plt.subplot(111, polar=True)
# 绘制雷达图
ax.plot(angles, data_1, marker='o',color='b',linewidth=1,label="计算机辅助设计")
ax.fill(angles, data_1, color='g',alpha=0.3)
ax.plot(angles, data_2, color='#C51B7D',marker='*',linewidth=1,label="计算机化工应用")
ax.fill(angles, data_2, color='#C51B7D',alpha=0.3)
# 设置雷达图中每一项的标签显示,两种方法均可以。
ax.set_thetagrids(angles*180/np.pi, labels,size=16)#单位为360度制
#plt.xticks(angles,labels=labels,size=18)#单位为弧度
#ax.set_ylabel("1月",labelpad=28) 
# 设置雷达图的0度起始位置
ax.set_theta_zero_location("N")#东方为起始位置，也可以是其他方位，如北方"N"
# 设置雷达图的坐标刻度范围
ax.set_rlim(0, 100)
ax.set_theta_offset(np.pi/2-np.pi/N)#保证第一类与最后一类的空间放在正上方
ax.set_theta_direction(-1)#表示顺时针方向为正
#方法用于设置极径标签显示位置,参数为标签所要显示在的角度
#ax.set_rlabel_position(0)
ax.spines['polar'].set_visible(False)
#ax.grid(False)
ax.set_title("两门慕课学习健康图")
plt.legend(loc='best',bbox_to_anchor=(1, 0.5, 0, 0.1))
plt.show()


