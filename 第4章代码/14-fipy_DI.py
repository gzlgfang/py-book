from fipy import CellVariable, Grid2D, Viewer, TransientTerm, DiffusionTerm,ImplicitSourceTerm,PowerLawConvectionTerm
from fipy.tools import numerix
import numpy as np

import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.shape_base import _hvdsplit_dispatcher
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
mpl.rcParams["font.size"] = 16#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
font1 = {'family': 'Times New Roman'} 


nx = 200
ny = nx
dx = 0.01
dy = dx
L = dx * nx
mesh = Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)
phi = CellVariable(name = "u值求解结果",
                   mesh = mesh,
                   value = 0.)

alpha=8.
D = 10.
eq =TransientTerm()==DiffusionTerm(coeff=D)+ImplicitSourceTerm(alpha)+ PowerLawConvectionTerm((10,1))
#TransientTerm() 

valueTopLeft = 30
valueBottomRight = 100
X, Y= mesh.faceCenters
facesTopLeft = ((mesh.facesLeft & (Y >= 0))
                | (mesh.facesTop & (X <= L)))
facesBottomRight = ((mesh.facesRight & (Y <= L ))
                    | (mesh.facesBottom & (X >=L/2)))
phi.constrain(valueTopLeft, facesTopLeft)
phi.constrain(valueBottomRight, facesBottomRight)



#if __name__ == '__main__':
# viewer = Viewer(vars=phi, datamin=0., datamax=100)
# viewer.plot()

timeStepDuration =0.01
#10 * 0.9 * dx**2 / (2 * D)
steps = 10
num="D="+str(D)+",alpha="+str(alpha)+",t="+str(steps*timeStepDuration)

#from builtins import range
for step in range(steps):
    eq.solve(var=phi,
             dt=timeStepDuration)
        #if __name__ == '__main__':
    #viewer.plot()
    #print((phi[39800]))


arr=np.zeros(len(phi))
for i in range(len(phi)):
    arr[i]=phi[i]
ar=arr.reshape(nx,nx)
print(ar)





x=np.arange(nx)*dx#长度位置，归一处理，从0开始，共101个点
y=np.arange(nx)*dy
X,Y=np.meshgrid(x, y)




norm = mpl.colors.Normalize(0, 100)
fig, ax = plt.subplots(1, 1, figsize=(8,8) )#布局设置
p = ax.pcolor(X, Y, ar, cmap=mpl.cm.jet,norm=norm,shading='auto')#pcolor绘制
cb=plt.colorbar(p, ax=ax)
cb.set_label("应变量u值")
ax.set_title(num+"时不同位置求解结果变化色图")
font1 = {'family': 'Times New Roman'}  
plt.yticks([0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2])# 设置纵轴刻度
plt.xticks([0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2])

#plt.yticks([0.2,0.4,0.6,0.8,1.0])# 设置纵轴刻度
#plt.xticks([0.2,0.4,0.6,0.8,1.0])

ax.set_xlabel('x',font1)
ax.set_ylabel('y',font1)
plt.show()
