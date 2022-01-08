# 递归函数的应用,阶乘（factorial)计算
def fact(n):
     if n==1:
        fa=1
     else:
       fa=fact(n-1)*n
     return fa
print(fact(10))
     
print(2*3*4*5*6*7*8*9*10)

def fact1(n):
     fa=1
     for i in range(n):
         fa=fa*(i+1)
     return fa
print(fact1(10))