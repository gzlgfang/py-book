# 求素数并计算所用时间34-para.py
import math
import numpy as np
from time import *
start = time()
sushu = np.zeros((100, 50))
for No in range(100):  # No从0-99
    k = 0
    for i in range(10**6 + 10**4 * (No + 1), 10**8):
        Para = True
        m = int(math.sqrt(i) + 1)
        for j in range(2, m):
            if i % j == 0:
                Para = False  # 只要能被其中一个数整除，就不是素数
                break
        if Para == True:  # 所有数都不能整除时，才是素数
            sushu[No, k] = i
            k = k + 1
        if k == 50:
            break
print(sushu)
end = time()
print(f"计算用时：{(end-start):.4f}秒")
