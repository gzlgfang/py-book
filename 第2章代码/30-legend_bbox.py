#29_legend_bbox.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
fig, ax = plt.subplots(figsize=(9, 9))

dict1={   0 :    'best' ,        
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
x=np.arange(0,11)
ax.plot(x,0*x+8,label= "bbox(0.35,0.35,0.15,0.1)",color=None,lw=0)
ax.legend(loc=dict1[3], handlelength=0,bbox_to_anchor=(0.35,0.35,0.15,0.1),fontsize=16,edgecolor="k")#loc表示图例位
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("图例bbox_to_anchor设置",fontsize=18)

ax1=ax.twinx()
ax1.plot(x,0*x+8,label= "bbox(0.15,0.75,0.15,0.1)",color=None,lw=0)
ax1.legend(loc=dict1[3], handlelength=0,bbox_to_anchor=(0.15,0.75,0.15,0.1),fontsize=16,edgecolor="k")#loc表示图例位
ax1.set_xticks([])
ax1.set_yticks([])

ax2=ax.twinx()
ax2.plot(x,0*x+8,label= "bbox(0.5,0.5,0.15,0.1)",color=None,lw=0)
ax2.legend(loc=dict1[3], handlelength=0,bbox_to_anchor=(0.5,0.5,0.15,0.1),fontsize=16,edgecolor="k")#loc表示图例位
ax2.set_xticks([])
ax2.set_yticks([])

ax3=ax.twinx()
ax3.plot(x,0*x+8,label= "bbox(0.5,-0.1,0.15,0.1)",color=None,lw=0)
ax3.legend(loc=dict1[3], handlelength=0,bbox_to_anchor=(0.5,-0.1,0.15,0.1),
           facecolor="pink",fontsize=16,edgecolor="k")#loc表示图例位
ax3.set_xticks([])
ax3.set_yticks([])

ax3=ax.twinx()
ax3.plot(x,0*x+8,label= "bbox(0.5,0.15,0.15,0.1)",color=None,lw=0)
ax3.legend(loc=dict1[3], handlelength=0,bbox_to_anchor=(0.5,0.15,0.15,0.1),fontsize=16,edgecolor="k")#loc表示图例位
ax3.set_xticks([])
ax3.set_yticks([])



plt.show()
