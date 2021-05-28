from itertools import chain
import pandas as pd

df = pd.read_excel('第8章代码/func.xlsx')
df = df.astype("str").T  # 去掉一个nan值
val = df.values
vals = []
# for ary in val:
#     for a in ary:
#         vals.append(str(a))
vals = list(chain.from_iterable(val))
vals = [v for v in vals if v != 'nan']
print("、".join(vals))
