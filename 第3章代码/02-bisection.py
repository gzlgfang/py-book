# 02-bisection.py
# 二分法非解线性方程零根
# bisection method 
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
f = lambda x: 3-x *np.sin(x) #超越方程
def f1(x):
    return x ** 3- 7.7 * x ** 2 + 19.2 * x - 15.3 #多项式方程
def f2(x):
    return  x**0.5-1.74+2*np.log10(0.1+18.7*x**0.5/5000) #摩擦系数方程
h=0.2 #搜索空间增量，不要太大，否则会漏根
def binarySolver(f, a, b, eps):
    """
    f: function
    a, b: search range of root
    eps: precision
    """
    y1, y2 = f(a), f(b)
    if y1 * y2 > 0:
        print(f"the input range [{a},{b}] is not valid, plz check")
        raise ValueError
    elif abs(y1)==0: # edge case
        return a
    elif abs(y2)==0:
        return b
    while y1 * y2 < 0:
        mid = (a + b) / 2
        y = f(mid)
        if abs(y) <= eps:
            return mid 
            #print(f"the root of the function is {mid}, y= {y}")
        if y * y1 < 0:
            b = mid # [a, mid]
            continue
        if y * y2 < 0:
            a = mid # [mid, b] 

def binaryMulSolver(f, a, b, eps):
    """ 应对多个零点的方程，找出全部的零点
    f: function
    a, b: search range of root
    eps: precision
    """
    res = []
    i, j = a, a + h # 子区间
    while i < b and j < b:
        if f(i) * f(j) <=0: # one solution exists in [i, j]
            k = binarySolver(f, i, j, eps)
            res.append(k)
            i = j # modify "start" of the range
        else:
            j = j + h # modify "end" of the range
    return res
sol1 = binaryMulSolver(f, 0, 30, 0.000001)
sol2 = binaryMulSolver(f1, 0, 30, 0.000001)
sol3 = binaryMulSolver(f2, 0, 30, 0.000001)
for i, s1 in enumerate(sol1):
    print("x{}={:.5f}".format(i,s1))
print()
for i, s2 in enumerate(sol2):
     print("x{}={:.5f}".format(i,s2))
print()
for i, s3 in enumerate(sol3):
     print("x{}={:.8f}".format(i,1/s3))

fig=plt.figure(figsize=(16,8),num="收敛过程图")
#ls = ['-',':', '-.', '--']
x=np.linspace(0,30,1000)
y1=f(x)
y2=f1(x)
y3=f2(x)
plt.plot(x,y1,lw=2,color="b",ls="-",label="方程1")#绘制函数曲线1
plt.plot(x,y2,lw=2,color="r",ls=":",label="方程2")#绘制函数曲线2
plt.plot(x,y3,lw=2,color="r",ls="-.",label="方程3")#绘制函数曲线3
plt.xlabel("自变量，x",fontsize=18)
plt.ylabel("函数值，f(x)",labelpad=5,fontsize=18)
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.xlim(0,30)
plt.ylim(-30,30)
plt.legend()
plt.title("函数变化过程图")
plt.show()




