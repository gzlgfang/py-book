#14-polar.py
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=18
plt.figure(num="polar_draw",figsize=(16,4))

ax1=plt.subplot(141,projection='polar')
ax2=plt.subplot(142,projection='polar')
ax3=plt.subplot(143,projection='polar')
ax4=plt.subplot(144,projection='polar')
#玫瑰花极坐标绘制
x=np.linspace(0,2*np.pi,1000,endpoint=False)
r=2*np.sin(6*x)
ax1.fill(x,r)
ax1.plot(x,r,c="red",lw=2,marker="*",mfc="r",ms=0.1)#mfc表示marker颜色，ms表示大小
ax1.set_title("玫瑰花极坐标绘制",fontsize=12)  
#渐开线绘制
x=np.linspace(0,6*np.pi,1000)
r=3*x
ax2.plot(x,r,c="blue",lw=2,ls=":",marker="*",mfc="r",ms=0.1)#mfc表示marker颜色，ms表示大小
ax2.set_title("渐开线极坐标绘制",fontsize=12)  
#随机折线绘制
x = np.linspace(0.0, 2*np.pi, 17 )
r = 20*np.random.rand(16)
r= np.concatenate((r, [r[0]]))
ax3.plot(x, r, color="b", linewidth=2, marker="*", mfc="r", ms=20)
ax3.set_title("随机折线极坐标绘制",fontsize=12)  

#极坐标绘制椭圆
a,b=20,10
x = np.linspace(0.0, 2*np.pi, 500)
r = np.sqrt((a**2+b**2)/(b**2*np.cos(x)**2+a**2*np.sin(x)**2))
ax4.plot(x, r, color="g", linewidth=2)
ax4.set_title("极坐标绘制椭圆",fontsize=12)  
#ms是标注的大小，mfc是标注的颜色，color是连接线条的颜色
#plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.tight_layout()#和上面adjust语句功能相同
plt.show()