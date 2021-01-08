import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(-5, 5, 100)
y1 = 0.5 * x
y2 = x * x
 
plt.figure()
plt.xlabel('X axis...')
plt.ylabel('Y axis...') #设置坐标轴的文字标签
 
ax = plt.gca() # get current axis 获得坐标轴对象
 
ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none') # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
 
ax.xaxis.set_ticks_position('bottom') 
ax.yaxis.set_ticks_position('left') # 指定下边的边作为 x 轴 指定左边的边为 y 轴
 
ax.spines['bottom'].set_position(('data', 0)) #指定 data 设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
 
plt.plot(x, y1, linestyle='--')
plt.plot(x, y2)
 
plt.show()
