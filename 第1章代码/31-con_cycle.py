# 条件及循环语句31-con_cycle.py
# 条件语句测试程序
import numpy as np
# 判断随机数是否大于0.5
n = 1
while n < 10:
    flag = np.random.random()
    if flag > 0.5:
        print(f"n={n},flag大于0.5,flag={flag}")
    else:
        print(f"n={n},flag小于0.5，flag={flag}")
    n = n + 1
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")
# 计算1-10自然数的平方和、立方和
sum2, sum3 = 0, 0
for i in range(10):
    sum2 = sum2 + (i + 1)**2
    sum3 = sum2 + (i + 1)**3
print(f"sum2={sum2},sum3={sum3}")
n, s2, s3 = 1, 0, 0
while n < 11:
    s2 = s2 + n**2
    s3 = s2 + n**3
    n = n + 1
print(f"s2={s2},s3={s3}")
# 计算1-100自然数不能被7整除数的累加和
sum1 = 0
for i in range(1, 101):
    if i % 7 == 0:
        continue
    sum1 = sum1 + i
print(f"sum1={sum1}")
sum2, n = 0, 0
while n < 100:
    n = n + 1
    if n % 7 == 0:
        continue
    sum2 = sum2 + n
print(f"sum2={sum2}")
# 求阶乘和
sum = 0
for i in range(1, 31):
    if i % 3 == 0:
        continue
    temp = 1
    for j in range(1, i + 1):
        temp = temp * j
    sum = sum + temp
print("阶乘和=", sum)

sum, i = 0, 0
while i < 30:
    i = i + 1
    if i % 3 == 0:
        continue
    temp = 1
    for j in range(1, i + 1):
        temp = temp * j
    sum = sum + temp
print("阶乘和=", sum)
