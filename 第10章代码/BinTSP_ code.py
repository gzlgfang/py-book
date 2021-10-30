# Binary_TSP code 
import numpy as np
def Bin_pop(ZQS,N):
    LJ=np.zeros((ZQS,N))
    for i in range(ZQS):
         for j in range(N):
             LJ[i,j]=np.fix(0.5+np.random.random())
    return LJ.astype(int)#需要强制转变成整数
print(Bin_pop(10,20))
def TSP_pop(ZQS,N):
    li=np.arange(0,N)
    LJ=np.zeros((ZQS,N))
    for i in range(ZQS):
         np.random.shuffle(li)
         LJ[i,:]=li
    return LJ.astype(int)#需要强制转变成整数

print(TSP_pop(10,20))