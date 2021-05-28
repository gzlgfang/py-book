import numpy as np
y=[6,9,12,3]
k1=[1,2,3]
k2=[1,3,1]
k3=[4,3,2]
k0=[6,1,4]
x=[k0,k1,k2,k3]
print(x)
print(y)


def paixu(x,y): 
  for i in range(len(y)-1):
      for j in range(i+1,len(y)):
          if y[i]>y[j]:
              tempy=y[i]
              y[i]=y[j]
              y[j]=tempy
              tempx=x[i]
              x[i]=x[j]
              x[j]=tempx
  xx=x
  yy=y
  return xx,yy
xx,yy=paixu(x,y)
print(xx)
print(yy)

