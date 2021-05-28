#10-sensitivity analysis 灵敏度分析
import numpy as np
from scipy.optimize import linprog
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams["font.size"] = 18#设置字体大小
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
J=np.zeros(10)#设置初值建立列表
x=np.zeros((10,3))
A_ub =[[4,2,4],[6, 5, 3],[9,4,2],[1,5,2],[2,5,3]]
b_ub = [38,30,36,28,48]
for i in range(10):
    c1=-12-i
    c = [c1,-12,-8]
    r = linprog(c,A_ub=A_ub,b_ub=b_ub, bounds=( (0,None), (0,None),(2,None)),method='simplex')
    #print(r)
    J[i]=r.fun
    x[i,:]=r.x
    #print(x[i,:])
#print(r)

plt.figure(num="灵敏度分析1",figsize=(8,8))
x_c1=np.linspace(12,21,10)#共10个c1
y_j=-0.1*J#目标函数乘0.1以便和x的值比例相似
plt.plot(x_c1,y_j,lw=2,color="b",label="0.1J",marker="o",markersize=12)#绘制c1和J之间的函数曲线
plt.plot(x_c1,x[:,0],lw=2,color="r",label="x1",marker="*",markersize=12)#绘制c1和x1之间的函数曲线
plt.plot(x_c1,x[:,1],lw=2,color="k",label="x2",marker="d",markersize=12)#绘制c1和x2之间的函数曲线
plt.plot(x_c1,x[:,2],lw=2,color="purple",label="x3",marker="p",markersize=12)#绘制c1和x3之间的函数曲线
plt.xlabel("c1",fontname="serif")
plt.ylabel("J_X",labelpad=5,fontname="serif")
plt.xticks(np.arange(12,22,1))
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.title("目标函数中系数变化对最优解的影响")
plt.legend()



#研究第二种资源由30变化到39对最优解的影响, 紧约束
J=np.zeros(10)#设置初值建立列表
x=np.zeros((10,3))
c = [-16,-12,-8]
A_ub =[[4,2,4],[6, 5, 3],[9,4,2],[1,5,2],[2,5,3]]
for i in range(10):
    b_ub = [38,25+i,36,28,48]
    r = linprog(c,A_ub=A_ub,b_ub=b_ub, bounds=( (0,None), (0,None),(2,None)),method='simplex')
    #print(r)
    J[i]=r.fun
    x[i,:]=r.x
plt.figure(num="灵敏度分析2",figsize=(8,8))
x_b2=np.linspace(25,34,10)#共10个b2
y_j=-0.1*J#目标函数乘0.1以便和x的值比例相似
plt.plot(x_b2,y_j,lw=2,color="b",label="0.1J",marker="o",markersize=12)#绘制b2和J之间的函数曲线
plt.plot(x_b2,x[:,0],lw=2,color="r",label="x1",marker="*",markersize=12)#绘制b2和x1之间的函数曲线
plt.plot(x_b2,x[:,1],lw=2,color="k",label="x2",marker="d",markersize=12)#绘制b2和x2之间的函数曲线
plt.plot(x_b2,x[:,2],lw=2,color="purple",label="x3",marker="p",markersize=12)#绘制b2和x3之间的函数曲线
plt.xlabel("b2",fontname="serif")
plt.ylabel("J_X",labelpad=5,fontname="serif")
plt.xticks(np.arange(25,34,1))
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.title("约束资源b2变化对最优解的影响")
plt.legend()

#研究第一种资源由23变化到42对最优解的影响（非紧约束
J=np.zeros(20)#设置初值建立列表
x=np.zeros((20,3))


for i in range(20):
    b_ub = [23+i,30,36,28,48]
    r = linprog(c,A_ub=A_ub,b_ub=b_ub, bounds=( (0,None), (0,None),(2,None)),method='simplex')
    #print(r)
    J[i]=r.fun
    x[i,:]=r.x
plt.figure(num="灵敏度分析3",figsize=(8,8))
x_b1=np.linspace(23,42,20)#共20个b1
y_j=-0.1*J#目标函数乘0.1以便和x的值比例相似
plt.plot(x_b1,y_j,lw=2,color="b",label="0.1J",marker="o",markersize=12)#绘制b1和J之间的函数曲线
plt.plot(x_b1,x[:,0],lw=2,color="r",label="x1",marker="*",markersize=12)#绘制b1和x1之间的函数曲线
plt.plot(x_b1,x[:,1],lw=2,color="k",label="x2",marker="d",markersize=12)#绘制b1和x2之间的函数曲线
plt.plot(x_b1,x[:,2],lw=2,color="purple",label="x3",marker="p",markersize=12)#绘制b1和x3之间的函数曲线
plt.xlabel("b1",fontname="serif")
plt.ylabel("J_X",labelpad=5,fontname="serif")
plt.xticks(np.arange(23,42,1))
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.title("约束资源b1变化对最优解的影响")
plt.legend()


plt.show()

