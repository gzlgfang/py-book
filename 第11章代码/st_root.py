import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"] = 16#设置字体大小
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
mpl.rcParams['ytick.direction'] = 'in'
#https://share.streamlit.io/gzlgfang/st-apps/main/st_root.py

st.title("二分法求解超越方程零根")
st.latex("a_0+a_1*x^{n_1}+ a_2*x^{n_2}+a_3*x^{n_3}+a_4*x* sinx +a_5*x^2*cosx")
st.header("系数输入")
col1, col2, col3  = st.columns(3)
with col1:
  a0= st.number_input("a0", value=-5.0)
with col2:
  a1= st.number_input("a1", value=0.0)  
with col3:
  a2= st.number_input("a2", value=0.0)
col1, col2 ,col3 = st.columns(3)
with col1:
  a3= st.number_input("a3", value=0.0)
with col2:
  a4= st.number_input("a4", value=1.0)
with col3:
  a5= st.number_input("a5", value=0.0)
col1, col2 ,col3 = st.columns(3)
with col1:
  n1= st.number_input("n1", value=1.0)
with col2:
  n2= st.number_input("n2", value=2.0)
with col3:
  n3= st.number_input("n3", value=3.0)
col1, col2 ,col3  = st.columns(3)
with col1:
  eps = st.number_input("精度", value=0.000001,step=0.000001,format="%f")
with col2:
   a = st.number_input("起点", value=0.0)
with col3:
   b = st.number_input("终点", value=30.0)

f = lambda x: a0+a1*x**n1+ a2*x**n2+a3*x**n3+a4*x* np.sin(x) +a5*np.cos(x)*x**2 #超越方程



fig=plt.figure(figsize=(16, 8), num="绘制函数曲线")
x = np.linspace(a, b, 300)
y = f(x)
plt.plot(x, y, lw=2, color="b", label="y")  # 绘制函数曲线
plt.xlabel("变量，x", fontsize=18)
plt.ylabel("函数值，f(x)", labelpad=5, fontsize=18)
plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
plt.xlim(a, b)
plt.legend()
plt.title("函数图")
st.pyplot(fig)





h=0.1 #搜索空间增量，不要太大，否则会漏根
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
#eps=0.000001
sol = binaryMulSolver(f, a, b, eps)
for i, s in enumerate(sol):
    st.write("x{}={:.5f}".format(i,s))

