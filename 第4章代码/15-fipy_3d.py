#15-fipy_3d
import fipy  as fp
from fipy.tools import numerix
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["FangSong"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#保证负号显示
mpl.rcParams["font.size"] = 12#设置字体大小
mpl.rcParams["font.style"] = "oblique"#设置字体风格，倾斜与否
mpl.rcParams["font.weight"] ="normal"# "normal",=500，设置字体粗细
font1 = {'family': 'Times New Roman'} 
nx = 10
ny = nx
nz=nx
dx =0.1
dy = dx
dz=dx
L = dx * nx
#mesh = Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)
mesh = fp.Grid3D(dx=dx, dy=dy, dz=dz,nx=nx, ny=ny,nz=nz)

u =fp.CellVariable(name = "solution variable",
                   mesh = mesh,
                   value = 0.)
D = 10.
#eq =DiffusionTerm(coeff=D)==0
#TransientTerm()
alpha=100
eq =fp.TransientTerm() == fp.DiffusionTerm(coeff=D)+fp.ImplicitSourceTerm(alpha)
valueTopLeft = 30
valueBottomRight = 100
X, Y,Z= mesh.faceCenters
facesTopLeft = ((mesh.facesLeft & (Y > 0)) | (mesh.facesTop & (X < L)))
facesBottomRight = ((mesh.facesRight & (Y <= L ))| (mesh.facesBottom & (X >=L/2)))
u.constrain(valueTopLeft, facesTopLeft)
u.constrain(valueBottomRight, facesBottomRight)
timeStepDuration = 10 * 0.9 * dx**2 / (2 * D)
steps = 10
for step in range(steps):
    eq.solve(var=u,
             dt=timeStepDuration)
    print(u)
    #print(type(phi),len(phi))
arr=np.zeros(len(u))
for i in range(len(u)):
    arr[i]=u[i]
arr1=list(arr)
b=arr1.reverse()
arr=np.array(arr1)
ar=arr.reshape(nx,ny,nz)
print(ar)
x=np.arange(nx)*dx#长度位置，归一处理，从0开始，共101个点
y=np.arange(ny)*dy

X,Y=np.meshgrid(x, y)
#print(X)
#print(len(X))
norm = mpl.colors.Normalize(30, 100)
for i in range(1,9,4):
#for i in range(nz):
    c=ar[:,:,i]
    fig=plt.figure()
    ax = plt.subplot(111,projection='3d' )
    p = ax.plot_surface(X, Y, c, rstride=1, cstride=1, linewidth=0, antialiased=False, norm=norm, cmap=mpl.cm.jet)
    #ax.contour(X, Y, z, zdir='z', offset=0, norm=norm, cmap=mpl.cm.copper)
    ax.set_xlabel('x',font1)
    ax.set_ylabel('y',font1)
    fig.colorbar(p, ax=ax, shrink=0.8)

z=np.arange(nz)*dz
X1,Y1,Z1=np.meshgrid(x, y,z)
fig=plt.figure()
ax = plt.subplot(111,projection='3d' )
#p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, norm=norm, cmap=mpl.cm.jet)
p=ax.scatter(X1,Y1,Z1,s=250, c=ar,cmap=mpl.cm.jet,marker="o",zdir="z",norm=norm)
ax.set_xlabel('x',font1)
ax.set_ylabel('y',font1)
ax.set_zlabel('z',font1)
fig.colorbar(p, ax=ax,shrink=0.8)
plt.show()
  
