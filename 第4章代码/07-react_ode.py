#07-react_ode.py 
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import math
#设置刻度线朝内
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
#全局设置字体
mpl.rcParams["font.sans-serif"]=["FangSong"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 28#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
font1 = {'family': 'Times New Roman'} 
#常数赋值
R= 8.31434 # 气体常数 kJ/kmol.K
k0=np.array( [1.2e+10 , 2.8e+10, 1.8e+5,  3.2e+7])#% 阿累乌尼斯常数, 1/s
E=np.array([1.3e+5,  1.6e+5 , 8.0e+4 , 1.2e+5])# ;% 活化能, kJ/kmol
# 反应速率常数, 1/s
T=230+273.15
global k
k= k0*np.exp(-E/(R*T))#;
print(k)
#y1,y2,y3,y3=c_A,c_B,c_C,c_D,
def dy(y,t):
    y1,y2,y3,y4=y[0],y[1],y[2],y[3]
    dy1=-(k[0]+k[1])*y1
    dy2= k[0]*y1-k[2]*y2
    dy3= k[1]*y1-k[3]*y3
    dy4= k[2]*y2+k[3]*y2
    return [dy1,dy2,dy3,dy4]
y0 = [2, 0,0,0]# 确定初始状态
tspan=np.linspace(0,10000,10001)#确定自变量范围
cbmax=[]
timemax=[]
temper=[]
for i in range(50):
    T=181+i+273.15
    k= k0*np.exp(-E/(R*T))#;
    sol =odeint(dy, y0, tspan)
    MAX_C_B=max(sol[:,1])
    time1=list(sol[:,1]).index(MAX_C_B)
    cbmax.append(MAX_C_B)
    timemax.append(time1)
    temper.append(T)
plt.figure(figsize=(8,6), dpi=80)
plt.plot(temper, cbmax, label='$maxc_{B}$',color="green", linewidth=3.0, linestyle="-")
plt.legend()
plt.grid(True)
plt.xlabel("反应温度，T(K)")
plt.ylabel("物质B浓度，"+"$c_{B}$")
plt.xticks()
plt.yticks()

plt.figure(figsize=(8,6), dpi=80)
plt.plot(temper, timemax, label='opt—time',color="green", linewidth=3.0, linestyle="-")
plt.legend()
plt.grid(True)
plt.xlabel("反应温度，T(K)")
plt.ylabel("物质B浓度最大时反应时间，s")
plt.xticks()
plt.yticks()




plt.figure(figsize=(8,6), dpi=80)# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(tspan, sol[:,0], label=r'$c_{A}$',color="red", linewidth=3, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(tspan, sol[:,1], label='$c_{B}$',color="green", linewidth=3.0, linestyle="-.")
plt.plot(tspan, sol[:,2], label='$c_{C}$',color="b", linewidth=3.0, linestyle="--")
plt.plot(tspan, sol[:,3], label='$c_{D}$',color="k", linewidth=3.0, linestyle=":")

#list.index(obj)
#print(MAX_C_B)

plt.annotate( f'最高点{MAX_C_B:.5f}', xy=(time1,MAX_C_B), xytext=(time1+1400,MAX_C_B+0.2), arrowprops=dict(arrowstyle='->',color="r",lw=2.5))
#print(time1)width：箭杆的宽度，以箭头单位衡量。默认是由以上单位的选择和矢量数量来决定。常用的初始值是0.005倍的画的宽度。
#headwidth：头部宽度相对于箭杆宽度的倍数，默认是3倍。
##headlength： 轴交叉处的头部长度，默认是4.5。
#minshaft：箭头比例的长度，以头部长度为单位。
plt.xlim(0,10000)
plt.ylim(0,2)
plt.xticks()# 设置横轴刻度
plt.xlabel('时间t,s',color='blue')# 设置x轴描述信息
plt.ylabel("浓度"+r"$c,kmol/m^{3}$",color='red')# 设置y轴描述信息
plt.yticks()# 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.savefig("g:\\recat_ode_07.png",dpi=72)# 以分辨率 72 来保存图片
plt.show()# 在屏幕上显示

