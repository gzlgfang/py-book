#Kepler equation
#05-Kepler_equ
import numpy as np
import math
import matplotlib  as mpl
import matplotlib.pyplot as plt
from scipy.optimize import fsolve,bisect,newton,brentq,brenth
def f(E):
    return M-E+e*math.sin(E)
sol=np.zeros((8,31))
f_sol=np.zeros((8,31))
for i in range(8):
    e=(i+1)*0.1
    for j in range(31):
        M=(j+1)*0.1
        sol[i,j]=fsolve(f,0.1)#所求根
        f_sol[i,j]=f(sol[i,j])#零点处函数值
print(sol)
print(f_sol)
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"] = 16#设置字体大小
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
mpl.rcParams['ytick.direction'] = 'in'
font1 = {'family': 'Times New Roman'} 
p=np.linspace(0,3.0,31)
for i in range(8):
    et="e="+str(int(10*(i+1)*0.1)/10)
    y1=sol[i,:]
    y2=f_sol[i,:]
    plt.plot(p,y1,lw=2,label=et)
plt.xlim(0,3.5)
plt.ylim(0,3.5)
plt.xlabel("平近点角,M")
plt.ylabel("偏平近点角,E")
plt.legend()
plt.grid()
plt.show()





