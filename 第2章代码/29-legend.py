#28_legend1.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
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
ax.plot(x,0*x+8,label=dict1[1],color=None,lw=0)
ax.legend(loc=dict1[1], fontsize=16,edgecolor="k")#loc表示图例位
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("图例loc设置",fontsize=18)
for n in range(2, 11):
    ax2 = ax.twinx()
    ax2.plot(x,0*x,label=dict1[n],color="w")
    ax2.legend(loc=dict1[n], fontsize=16,edgecolor="k")#loc表示图例位置
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.tick_params(left='out')
    ax2.set_ylim(1,9)
    ax2.tick_params(left='out',color="w")
plt.show()
