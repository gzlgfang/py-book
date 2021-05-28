# 21-time-date.py#时间日期函数
from datetime import datetime as dt
import time
import datetime
import calendar
# time()求时间差
x = 0
start_time = time.time()
print("start_time:", start_time)
for i in range(5000):
    for j in range(1000):
        x = i + j
end_time = time.time()
print("time程序运行计时", end_time - start_time)
# 获取当地时间元组
print("localtime当地时间元组：", time.localtime())
print("localtime时间戳转换时间元组：", time.localtime(17000000000))
print("ctime当地时间字符串:", time.ctime())
print("ctime指定时间戳字符串:", time.ctime(1620000000))
# perf_counter()求时间差
x = 0
start_time = time.perf_counter()
print("start_time:", start_time)
for i in range(5000):
    for j in range(1000):
        x = i + j
end_time = time.perf_counter()
print("perf_counter程序运行计时=", end_time - start_time)
# process_time()求时间差
x = 0
start_time = time.process_time()
print("start_time:", start_time)
for i in range(5000):
    for j in range(1000):
        x = i + j
end_time = time.process_time()
print("process_time程序运行计时=", end_time - start_time)
# ctime()获取时间字符串
print("ctime获取当前时间字符串：", time.ctime())
time_str = time.ctime()
print("显示时钟部分时间字符串：", time_str[11:19])
# asctime([tupletime]) 获取时间字符串
print("asctime获取当前时间字符串：", time.asctime())
print("asctime获取元组时间字符串：", time.asctime((2021, 2, 16, 8, 15, 18, 1, 47, 0)))
# 按是定格式返回时间元组字符串，默认为当地时间
my_format1 = "%Y/%m/%d %H:%M:%S"
my_format2 = "%Y/%B/%d %A %p:%H:%M:%S"
print("按格式获取当前时间字符串1：", time.strftime(my_format1))
print("按格式获取当前时间字符串2：", time.strftime(my_format2))
t_tup1 = (2021, 2, 16, 8, 15, 18, 1, 47, 0)
t_tup2 = (1, 2, 16, 8, 15, 18, 1, 47, 0)
print("按格式获取元组时间字符串1：", time.strftime(my_format1, t_tup1))
print("按格式获取元组时间字符串2：", time.strftime(my_format2, t_tup2))
# datetime计算程序运行时间
x = 0
start_time = dt.now()
print("start_time:", start_time)
for i in range(5000):
    for j in range(1000):
        x = i + j
end_time = dt.now()
print("datetime计算程序运行计时=", end_time - start_time)
# datetime计算两日期之间的时间差
t1 = dt(2021, 3, 8)
t2 = dt(1997, 10, 8)
print("两日期之差：", (t2 - t1).days)
