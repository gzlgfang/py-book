#24-ls-lw_set.py
import numpy as np
import matplotlib.pyplot as plt
#loc=1,2,3,4=右上角，左上角，左下角，右下角=uper right,upper left,lower left,lower right
fig, ax = plt.subplots(figsize=(9, 9))
#ax=fig.add_axes([0,0,0.7,0.7])
ls = ['-',':', '-.', '--']#ls=linestyles
x = np.linspace(-10, 10, 100)
for n in range(1, 9):
    ax.plot(x, 0 * x+n, lw=n,ls=ls[n%4],label="lw = %d" % n)
ax.legend(ncol=4, loc='lower left',bbox_to_anchor=(0, 1), fontsize=16)#nocl表示图例分为多少列，loc表示图例位置
fig.subplots_adjust(top=0.8);
plt.xticks([])
plt.yticks([])
plt.ylim(0,9)#y轴取值范围为0-9
plt.show()
