# 二分法解线性方程零根
# bisection method ?
import math
h = 0.2  # 搜索空间增量，不要太大，否则会漏根


def binarySolver(f, a, b, eps):
    """
    f: function
    a, b: search range of root
    eps: precision
    """
    y1, y2 = f(a), f(b)
    if y1 * y2 > 0:
        print(f"the input range [{a},{b}] is not valid, plz check")
        raise ValueError
    elif y1 == 0:  # edge case
        return a
    elif y2 == 0:
        return b
    while y1 * y2 < 0:
        mid = (a + b) / 2
        y = f(mid)
        if abs(y) <= eps:
            return mid
            #print(f"the root of the function is {mid}, y= {y}")
        if y * y1 < 0:
            b = mid  # [a, mid]
            continue
        if y * y2 < 0:
            a = mid  # [mid, b]


def binaryMulSolver(f, a, b, eps):
    """ 应对多个零点的方程，找出全部的零点
    f: function
    a, b: search range of root
    eps: precision
    """
    res = []
    i, j = a, a + h  # 子区间
    while i < b and j < b:
        if f(i) * f(j) < 0:  # one solution exists in [i, j]
            k = binarySolver(f, i, j, eps)
            res.append(k)
            i = j  # modify "start" of the range
        else:
            j = j + h  # modify "end" of the range
    return res


def f1(x): return x ** 3 - 7.7 * x ** 2 + 19.2 * x - 15.3


def f2(x):
    return x ** 3 - 7.7 * x ** 2 + 19.2 * x - 15.3


def f3(x): return 3 - x * math.sin(x)


sol1 = binarySolver(f1, 1, 2, 0.0001)
sol2 = binaryMulSolver(f3, 0, 30, 0.0001)
print(f"sol1={sol1:.5f}")
print("sol1=%.7f" % sol1)  # 不同的format string写法


for i, s2 in enumerate(sol2):
    print(f"x{i} = {s2:.4f}")

# f'result: {value:{width}.{precision}}' check https://www.python.org/dev/peps/pep-0498/#id30
