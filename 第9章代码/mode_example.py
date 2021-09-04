#mode_example

from scipy.stats import mode#函数作用：返回传入数组/矩阵中最常出现的成员以及出现的次数。
#如果多个成员出现次数一样多，返回值小的那个。
import numpy as np
a_mode=np.random.randint(0,10,size=(10,10))
print(a_mode)
c_number=10*[0]
c_num=0
for i in range(100):
    for j in range(10):
        for  k in range(10):
            if a_mode[i,j]==k:
               c_number[k]=c_number[k]+1
               exit
print(c_number)
most_a=mode(a_mode,axis=0)#axis=1,按行进行统计；默认按列进行统计
print(most_a)
print(most_a[0])

