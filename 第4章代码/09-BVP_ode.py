#09-BVP_ode.py 
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_bvp
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
tspan=np.linspace(0,10,101)#确定自变量范围
y_tspan = np.zeros((2, tspan.size))
#定义微分方程,注意和程序08-bc_ode中的不同，自变量t放在前面
def dy(t,y):#已知微分方程y1的两个端点值为40和80，但不知y2的开始端点值
    y1,y2=y[0],y[1]
    dy1=y2
    dy2=0.05*(1+t**2)*y1+2
    return np.vstack((dy1, dy2))
#定义边界条件
def BC(ya, yb):
    f1,f2=40,80
    return np.array([ya[1]-f1, yb[0]-f2])
sol = solve_bvp(dy, BC,tspan, y_tspan)
y=sol.sol(tspan)[0] 
dyy=sol.sol(tspan)[1]
plt.figure(figsize=(8,6), dpi=80)# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# 绘制温度曲线，使用红色、连续的、宽度为 2（像素）的线条
plt.plot(tspan, y, label="y",color="red", linewidth=2, linestyle="-")
# 绘制温度变化速率曲线，使用绿色的、虚线、宽度为 2 （像素）的线条
plt.plot(tspan, dyy, label='dy',color="green", linewidth=2.0, linestyle="--")

plt.xticks(np.linspace(0,10,11,endpoint=True))# 设置横轴刻度
plt.xlim(0,10)# 设置x轴的上下限
plt.ylim(-120,180)
plt.xlabel('x',font1,color='blue')# 设置x轴描述信息
plt.ylabel('y,dy',color='red')# 设置y轴描述信息
plt.yticks(np.linspace(-120,180,16))# 设置纵轴刻度
plt.legend()
plt.grid(True)
plt.savefig("g:\\bvp_ode.png",dpi=72)# 以分辨率 72 来保存图片
plt.show()# 在屏幕上显示