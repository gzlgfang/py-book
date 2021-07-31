#01-relax_itera
#松弛迭代法求超越方程零根:xsinx+7x-18
# Relaxation iteration 
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"] = 16#设置字体大小
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
mpl.rcParams['ytick.direction'] = 'in'
f = lambda x: x *np.sin(x) + 7 * x-18#超越方程
def f1(x,omiga):
     return x+omiga*((18-7*x)/np.sin(x)-x)#迭代格式1
def f2(x,omiga):
    return x+omiga*((18-x*np.sin(x))/7-x)#迭代格式2
""" 精度及初始点设置
   eps: precision
   x0： Initial point 
"""
eps=0.0000001
x0=4
k=0#迭代次数
flag=True
sol1=[]
while abs(f(x0))>eps:
      x0=f1(x0,0.1)
      k=k+1
      sol1.append(f(x0))
      if k>10000:
          print("此迭代格式发散")
          flge=False
          break
if flag==True:
    print("迭代次数k={},x={:.5f},f(x)={:.7f}".format(k,x0,f(x0)))
eps=0.0000001
x0=1
k=0#迭代次数
flag=True
sol2=[]
while abs(f(x0))>eps:
      x0=f2(x0,0.1)
      k=k+1
      sol2.append(f(x0))
      if k>10000:
          print("此迭代格式发散")
          flge=False
          break
if flag==True:
    print("迭代次数k={},x={:.5f},f(x)={:.7f}".format(k,x0,f(x0)))
fig=plt.figure(figsize=(16,8),num="收敛过程图")
plt.plot(sol1,lw=2,color="b",marker="o",label="格式1")#绘制迭代格式1函数曲线
plt.plot(sol2,lw=2,color="r",marker="*",label="格式2")#绘制迭代格式2函数曲线
plt.xlabel("迭代次数，k",fontsize=18)
plt.ylabel("函数值，f(x)",labelpad=5,fontsize=18)
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.xlim(0,30)
plt.legend()
plt.title("收敛过程图")
plt.show()