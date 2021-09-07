import numpy as np
import matplotlib.pyplot as plt
from skimage import io

## 不应指定绝对路径，而应该换成相对路径

img1 = '.\imgs\\logo.png'
asimg1 = io.imread(img1)
print(type(asimg1), asimg1.shape, asimg1.dtype)

plt.imshow(asimg1)
plt.show()
# scikit_image-0.17.2-cp37-cp37m-win_amd64.whl

print(asimg1[5000, 300:400, :])
