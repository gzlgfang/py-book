#31.py
#离心泵工作曲线绘制
#29_legend_bbox.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as mticker
#全局设置字体
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
plt.rcParams['ytick.direction'] = 'in'
fig, ax = plt.subplots(figsize=(9, 9))
x=[0,2,4,6,8,10,12,14]
H=[11,10.8,10.5,10,9.2,8.4,7.4,6]
eita=[0,15,30,45,60,65,55,30]
P=[2,2.3,2.5,2.9,3.5,3.9,4.5,5.0]
He=[6,6.096,6.384,6.864,7.536,8.4,9.456,10.704]
#流量qv/L·s-1	0	2	4	6	8	10	12	14
#压头H/m	11	10.8	10.5	10	9.2	8.4	7.4	6
#效率η/%	0	15	30	45	60	65	55	30
#管路阻力He/m	6	6.096	6.384	6.864	7.536	8.4	9.456	10.704
#功率P/kw	2	2.04	2.08	2.12	2.16	2.2	2.24	2.28
cy_c= ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'
           , '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
d_loc={   0 :    'best' ,        
          1  :   'upper right' ,  
          2    : 'upper left' ,   
          3    : 'lower left',     
          4    : 'lower right',    
          5    : 'right',         
          6    : 'center left',    
          7    : 'center right',   
          8    : 'lower center',  
          9   :  'upper center',  
          10 :    'center'}  
mks = ['.',',', 'o', 'v','^','<','>','1','2','3','4','s','p','*','H','h','X','x','D','d','|','+']
ax.plot(x,H,label="压头H/m",c=cy_c[1],marker=mks[2],lw=2)
ax.plot(x,He,label="管路阻力He/m",c=cy_c[2],marker=mks[3],lw=2)
ax.legend(loc=d_loc[1],fontsize=16)#loc表示图例位
ax.set_xlim(0,15)
ax.set_ylim(5,13)
ax.set_ylabel("压头H/m,管路阻力He/m",fontsize=18)
ax.set_xlabel("流量"+r"$q_{v}/L·s^{-1}$",fontsize=18)
ax.set_title("离心泵工作曲线",fontsize=18)
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(2))#主刻度间隔10
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))#次刻度间隔5
#ax.tick_params( top='on', which='both',direction = 'in')
ax.grid(color="b", which="both", linestyle=':', linewidth=1)



ax1=ax.twinx()
ax1.plot(x,eita,label="效率η/%",c=cy_c[3],marker=mks[5],lw=2)
ax1.set_ylim(0,80)
ax1.legend(loc=d_loc[2] ,fontsize=16)#loc表示图例位
ax1.yaxis.set_major_locator(mpl.ticker.MultipleLocator(10))#主刻度间隔10
ax1.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))#次刻度间隔5
ax1.grid(color="b", which="both", linestyle=':', linewidth=1)
ax1.set_ylabel("效率η/%",fontsize=18)

ax2=ax.twinx()
ax2.plot(x,P,label="功率P/kw",c=cy_c[4],marker=mks[6],lw=2)
ax2.set_ylim(0,10)
ax2.legend(loc=d_loc[3] ,bbox_to_anchor=(0.004,0.83),fontsize=16)#loc表示图例位
ax2.spines['right'].set_position(('data', 16))
ax2.set_ylabel("功率P/kw",fontsize=18)




plt.show()
