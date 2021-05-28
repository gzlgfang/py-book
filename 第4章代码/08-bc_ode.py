#08-bc_ode.py 
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
#设置刻度线朝内
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#全局设置字体
mpl.rcParams["font.sans-serif"]=["FangSong"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 48#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
font1 = {'family': 'Times New Roman'} 
def dy(y,t):#已知微分方程y1的两个端点值为40和80，但不知y2的开始端点值
    y1,y2=y[0],y[1]
    dy1=y2
    dy2=0.05*(1+t**2)*y1+2
    return [dy1,dy2]
tspan=np.linspace(0,10,101)#确定自变量范围
#假设2个y2开始端点，算出y1的末端端点值，利用内插产生y2开始端点迭代初值
f2=80#y1右端值
a1,a2=0,-20
y0_1,y0_2=[40,a1],[40,a2]
sol_1=odeint(dy, y0_1, tspan)#计算得到y1的末端值为sol_1[101,0]
sol_2=odeint(dy, y0_2, tspan)#计算得到y1的末端值为sol_2[101,0]
k=(a2-a1)/(sol_2[100,0]-sol_1[100,0])
c_0=a1+k*(f2-sol_1[100,0])
#print(c_0)
#print(sol_1[100,0])
#print(sol_2[100,0])
flag=True
while flag:
    sol=odeint(dy, [40,c_0], tspan)
    if abs((f2-sol[100,0])/f2)>=0.00001:
        c_1=c_0+k*(f2-sol[100,0])
        c_0=c_1
    else:
        flag=False
print(c_0)
print(sol[100,0])
          
plt.figure(figsize=(8,6), dpi=80)# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(tspan, sol[:,0], label="y",color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(tspan, sol[:,1], label='dy',color="green", linewidth=2.0, linestyle="--")
plt.xticks(np.linspace(0,10,11,endpoint=True))# 设置横轴刻度
plt.xlim(0,10)# 设置x轴的上下限
plt.ylim(-20,180)
plt.xlabel('x',font1,color='blue')# 设置x轴描述信息
plt.ylabel('y,dy',color='red')# 设置y轴描述信息
plt.yticks(np.linspace(-20,180,11))# 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.savefig("g:\\bcyode.png",dpi=72)# 以分辨率 72 来保存图片
plt.show()# 在屏幕上显示
