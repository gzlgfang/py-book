import numpy as np

prime_num = np.zeros((80, 5))
for no in range(80):
    k = 0
    for i in range(100000 + 1000 * (no + 1), 10000000):
        para = True
        m = np.int(np.math.sqrt(i) + 1)
        for j in range(2, m):
            if i % j == 0:
                para = False
                break
        if para:
            prime_num[no][k] = i
            k += 1
        if k == 5:  # 0 index
            break

print(prime_num)
