from signal import signal
import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as op
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"] = 12#设置字体大小
mpl.rcParams['ytick.right']=True
mpl.rcParams['xtick.top']=True
mpl.rcParams['xtick.direction'] = 'in'#坐标轴上的短线朝内，默认朝外
mpl.rcParams['ytick.direction'] = 'in'

n=st.number_input("实验数目num", value=12,step=1,format="%d")
n=int(n)
x=np.zeros(n)
y=np.zeros(n)

st.markdown("单变量参数拟合")
st.latex("多项式:y=a_0+a_1*x+ a_2*x^{2}+a_3*x^{3}+a_4*x^{4}+a_5*x^{5}")
st.latex("指数:y=a*e^{bx}")
st.latex("幂函数:y=a*x^{b}")
st.latex("对数:y=a*lnx+b")

st.write("输入x变量")
col1, col2, col3  = st.columns(3)
with col1:
  x[0]= st.number_input("x1", value=1.001,step=0.001,format="%f")  
with col2:
  x[1]= st.number_input("x2", value=2.001,step=0.001,format="%f") 
with col3:
  x[2]= st.number_input("x3", value=3.001,step=0.001,format="%f")

col1, col2, col3 = st.columns(3)
with col1:
  x[3]= st.number_input("x4", value=4.001,step=0.001,format="%f")
with col2:
  x[4]= st.number_input("x5", value=5.001,step=0.001,format="%f")
with col3:
  x[5]= st.number_input("x6", value=6.001,step=0.001,format="%f")

col1, col2, col3 = st.columns(3)
with col1:
  x[6]= st.number_input("x7", value=7.001,step=0.001,format="%f")
with col2:
  x[7]= st.number_input("x8", value=8.001,step=0.001,format="%f")
with col3:
  x[8]= st.number_input("x9", value=9.001,step=0.001,format="%f")

col1, col2, col3 = st.columns(3)
with col1:
  x[9]= st.number_input("x10", value=10.001,step=0.001,format="%f")
with col2:
  x[10]= st.number_input("x11", value=11.001,step=0.001,format="%f")
with col3:
  x[11]= st.number_input("x12", value=12.001,step=0.001,format="%f")


st.write("输入y变量")
col1, col2, col3  = st.columns(3)
with col1:
  y[0]= st.number_input("y1", value=11.001,step=0.001,format="%f")
with col2:
  y[1]= st.number_input("y2", value=12.001,step=0.001,format="%f") 
with col3:
 y[2]= st.number_input("y3", value=13.001,step=0.001,format="%f")

col1, col2, col3 = st.columns(3)
with col1:
  y[3]= st.number_input("y4", value=14.001,step=0.001,format="%f")
with col2:
  y[4]= st.number_input("y5", value=15.001,step=0.001,format="%f")
with col3:
  y[5]= st.number_input("y6", value=16.001,step=0.001,format="%f")

col1, col2, col3 = st.columns(3)
with col1:
  y[6]= st.number_input("y7", value=17.001,step=0.001,format="%f")
with col2:
  y[7]= st.number_input("y8", value=18.001,step=0.001,format="%f")
with col3:
  y[8]= st.number_input("y9", value=19.001,step=0.001,format="%f")

col1, col2, col3 = st.columns(3)
with col1:
  y[9]= st.number_input("y10", value=20.001,step=0.001,format="%f")
with col2:
  y[10]= st.number_input("y11", value=21.001,step=0.001,format="%f")
with col3:
  y[11]= st.number_input("y12", value=22.001,step=0.001,format="%f")
m=st.number_input("参加拟合数据数目", value=12,step=1,format="%d")
m=int(m)
xx=x[0:m]
yy=y[0:m]

#st.write("x=",x)
#st.write("y=",y)

add_selectbox = st.sidebar.radio(
        "拟合基本图",
        ("一次", "二次", "三次","四次", "五次","指数","幂函数","对数")
    )
if add_selectbox=="一次":
    coef=np.polyfit(xx,yy,deg=1)
     #st.write("coef1=",coef1)
    st.write("拟合方程：y=",int(10000*coef[1]+0.5)/10000,"+",int(10000*coef[0]+0.5)/10000,"*x")
    xdata=xx
    y_real=yy
    ydata=coef[1]+coef[0]*xx

    fig=plt.figure(num="拟合曲线绘制",figsize=(8,8))
    plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
    plt.xlabel("x",fontname="serif")
    plt.ylabel("y",labelpad=5,fontname="serif")
    eer=sum((y_real-ydata)**2)
    plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
    plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.9*(max(yy)-min(yy)+min(yy)),f'均方误差={eer:.5f}' )
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.8*(max(yy)-min(yy)+min(yy)),f'拟合方程：y={coef[1]:.5f}+{coef[0]:.5f}x')#{}
    plt.xlim(min(xx)-0.5,max(xx)+0.5)#设置x轴范围
    plt.ylim(min(yy)-1,max(yy)+1)
    plt.legend()
    st.pyplot(fig)




elif add_selectbox=="二次": 
    coef=np.polyfit(xx,yy,deg=2)
     #st.write("coef1=",coef1)
    st.write("拟合方程：y=",int(10000*coef[2]+0.5)/10000,"+",int(10000*coef[1]+0.5)/10000,"*x+",int(10000*coef[0]+0.5)/10000,"*x^2")
    xdata=xx
    y_real=yy
    ydata=coef[2]+coef[1]*xx+coef[0]*xx**2

    fig=plt.figure(num="拟合曲线绘制",figsize=(8,8))
    plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
    plt.xlabel("x",fontname="serif")
    plt.ylabel("y",labelpad=5,fontname="serif")
    eer=sum((y_real-ydata)**2)
    plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
    plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.9*(max(yy)-min(yy)+min(yy)),f'均方误差={eer:.5f}' )
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.8*(max(yy)-min(yy)+min(yy)),f'拟合方程：y={coef[2]:.5f}+{coef[1]:.5f}x+{coef[0]:.5f}x$^{{2}}$')#{}
    plt.xlim(min(xx)-0.5,max(xx)+0.5)#设置x轴范围
    plt.ylim(min(yy)-1,max(yy)+1)
    plt.legend()
    st.pyplot(fig)
    
    
elif add_selectbox == "三次":
    coef=np.polyfit(xx,yy,deg=3)
     #st.write("coef1=",coef1)
    st.write("拟合方程：y=",int(10000*coef[3]+0.5)/10000,"+",int(10000*coef[2]+0.5)/10000,"*x+",int(10000*coef[1]+0.5)/10000,"*x^2+",int(10000*coef[0]+0.5)/10000,"*x^3")
    xdata=xx
    y_real=yy
    ydata=coef[3]+coef[2]*xx+coef[1]*xx**2+coef[0]*xx**3

    fig=plt.figure(num="拟合曲线绘制",figsize=(8,8))
    plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
    plt.xlabel("x",fontname="serif")
    plt.ylabel("y",labelpad=5,fontname="serif")
    eer=sum((y_real-ydata)**2)
    plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
    plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.9*(max(yy)-min(yy)+min(yy)),f'均方误差={eer:.5f}' )
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.8*(max(yy)-min(yy)+min(yy)),f'拟合方程：y={coef[3]:.5f}+{coef[2]:.5f}x+{coef[1]:.5f}x$^{{2}}$+{coef[0]:.5f}x$^{{3}}$')#{}
    plt.xlim(min(xx)-0.5,max(xx)+0.5)#设置x轴范围
    plt.ylim(min(yy)-1,max(yy)+1)
    plt.legend()
    st.pyplot(fig)
elif add_selectbox=="四次": 
    coef=np.polyfit(xx,yy,deg=4)
     #st.write("coef1=",coef1)
    st.write("拟合方程：y=",int(10000*coef[4]+0.5)/10000,"+",int(10000*coef[3]+0.5)/10000,"*x+",int(10000*coef[2]+0.5)/10000,"*x^2+",int(10000*coef[1]+0.5)/10000,"*x^3+",int(10000*coef[0]+0.5)/10000,"*x^4")
    xdata=xx
    y_real=yy
    ydata=coef[4]+coef[3]*xx+coef[2]*xx**2+coef[1]*xx**3+coef[0]*xx**4

    fig=plt.figure(num="拟合曲线绘制",figsize=(8,8))
    plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
    plt.xlabel("x",fontname="serif")
    plt.ylabel("y",labelpad=5,fontname="serif")
    eer=sum((y_real-ydata)**2)
    plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
    plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.9*(max(yy)-min(yy)+min(yy)),f'均方误差={eer:.5f}' )
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.8*(max(yy)-min(yy)+min(yy)),f'拟合方程：y={coef[4]:.5f}+{coef[3]:.5f}x+{coef[2]:.5f}x$^{{2}}$+{coef[1]:.5f}x$^{{3}}$+{coef[0]:.5f}x$^{{4}}$')#{}
    plt.xlim(min(xx)-0.5,max(xx)+0.5)#设置x轴范围
    plt.ylim(min(yy)-1,max(yy)+1)
    plt.legend()
    st.pyplot(fig)
elif add_selectbox == "五次":
    coef=np.polyfit(xx,yy,deg=5)
     #st.write("coef1=",coef1)
    st.write("拟合方程：y=",int(10000*coef[5]+0.5)/10000,"+",int(10000*coef[4]+0.5)/10000,"*x+",int(10000*coef[3]+0.5)/10000,"*x^2+",int(10000*coef[2]+0.5)/10000,"*x^3+",int(10000*coef[1]+0.5)/10000,"*x^4+",int(10000*coef[0]+0.5)/10000,"*x^5")
    xdata=xx
    y_real=yy
    ydata=coef[5]+coef[4]*xx+coef[3]*xx**2+coef[2]*xx**3+coef[1]*xx**4+coef[0]*xx**5

    fig=plt.figure(num="拟合曲线绘制",figsize=(8,8))
    plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
    plt.xlabel("x",fontname="serif")
    plt.ylabel("y",labelpad=5,fontname="serif")
    eer=sum((y_real-ydata)**2)
    plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
    plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.9*(max(yy)-min(yy)+min(yy)),f'均方误差={eer:.5f}' )
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.8*(max(yy)-min(yy)+min(yy)),f'拟合方程：y={coef[5]:.5f}+{coef[4]:.5f}x+{coef[3]:.5f}x$^{{2}}$+{coef[2]:.5f}x$^{{3}}$+{coef[1]:.5f}x$^{{4}}$+{coef[1]:.5f}x$^{{5}}$')#{}
    plt.xlim(min(xx)-0.5,max(xx)+0.5)#设置x轴范围
    plt.ylim(min(yy)-1,max(yy)+1)
    plt.legend()
    st.pyplot(fig)
  
elif add_selectbox == "指数":
    #xdata=np.array([1,2,3,4,5,6,7,8])
    #y_real=np.array([15.3,20.5,27.4,36.6,49.1,65.6,87.8,117.6])
    xdata=xx
    y_real=yy
    def func(x, a,  b):
        return  a*np.exp(b*x)
    alf_opt,alf_cov=op.curve_fit(func,xdata,y_real)

    st.write("拟合方程：y=",int(10000*alf_opt[0]+0.5)/10000,"e^",int(10000*alf_opt[1]+0.5)/10000,"x")

    
    fig=plt.figure(num="拟合曲线绘制",figsize=(8,8))
    plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
    plt.xlabel("x",fontname="serif")
    plt.ylabel("y",labelpad=5,fontname="serif")
    ydata=func(xdata,*alf_opt)
    eer=sum((y_real-ydata)**2)
    plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
    plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.9*(max(yy)-min(yy)+min(yy)),f'均方误差={eer:.5f}' )
    alf=(int(alf_opt[1]*10000+0.5)/10000)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.8*(max(yy)-min(yy)+min(yy)),f'拟合方程：y={alf_opt[0]:.5f}e$^{{{alf}x}}$')#{}
    plt.xlim(min(xx)-0.5,max(xx)+0.5)#设置x轴范围
    plt.ylim(min(yy)-1,max(yy)+1)
    plt.legend()
    st.pyplot(fig)
    
elif add_selectbox == "幂函数":
    xdata=xx
    y_real=yy
    def func(x, a,  b):
        return  a*x**b
    alf_opt,alf_cov=op.curve_fit(func,xdata,y_real)

    st.write("拟合方程：y=",int(10000*alf_opt[0]+0.5)/10000,"x^",int(10000*alf_opt[1]+0.5)/10000)

    
    fig=plt.figure(num="拟合曲线绘制",figsize=(8,8))
    plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
    plt.xlabel("x",fontname="serif")
    plt.ylabel("y",labelpad=5,fontname="serif")
    ydata=func(xdata,*alf_opt)
    eer=sum((y_real-ydata)**2)
    plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
    plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.9*(max(yy)-min(yy)+min(yy)),f'均方误差={eer:.5f}' )
    alf=(int(alf_opt[1]*10000+0.5)/10000)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.8*(max(yy)-min(yy)+min(yy)),f'拟合方程：y={alf_opt[0]:.5f}x$^{{{alf}}}$')#{}
    plt.xlim(min(xx)-0.5,max(xx)+0.5)#设置x轴范围
    plt.ylim(min(yy)-1,max(yy)+1)
    plt.legend()
    st.pyplot(fig)
elif add_selectbox == "对数":
    xdata=xx
    y_real=yy
    def func(x, a,  b):
        return  a*np.log(x)+b
    alf_opt,alf_cov=op.curve_fit(func,xdata,y_real)

    st.write("拟合方程：y=",int(10000*alf_opt[0]+0.5)/10000,"ln(x)+",int(10000*alf_opt[1]+0.5)/10000)

    
    fig=plt.figure(num="拟合曲线绘制",figsize=(8,8))
    plt.scatter(xdata,y_real,color="red",label='实验数据')#绘制数据点
    plt.xlabel("x",fontname="serif")
    plt.ylabel("y",labelpad=5,fontname="serif")
    ydata=func(xdata,*alf_opt)
    eer=sum((y_real-ydata)**2)
    plt.plot(xdata,ydata, label='拟合曲线',color="green", linewidth=2.0, linestyle="--")
    plt.grid(which='both', axis='both', color='r', linestyle=':', linewidth=1)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.9*(max(yy)-min(yy)+min(yy)),f'均方误差={eer:.5f}' )
    alf=(int(alf_opt[1]*10000+0.5)/10000)
    plt.text(min(xx)+0.1*(max(xx)-min(xx)),0.8*(max(yy)-min(yy)+min(yy)),f'拟合方程：y={alf_opt[0]:.5f}ln(x)+{alf:.5f}')#{}
    plt.xlim(min(xx)-0.5,max(xx)+0.5)#设置x轴范围
    plt.ylim(min(yy)-1,max(yy)+1)
    plt.legend()
    st.pyplot(fig)
