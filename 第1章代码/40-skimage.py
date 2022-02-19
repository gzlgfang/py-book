# skimage库应用40-skimage.py
from skimage import data
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
img1 = ("taoflower2.jpg")
asimg1 = io.imread(img1)
print(type(asimg1), asimg1.shape, asimg1.dtype)
plt.imshow(asimg1)
plt.show()
print(asimg1[3000, 300:400, :])
# data module
plt.close
cat = data.chelsea()
print(f"shape:{cat.shape}")
print(cat.min(), cat.max())
plt.imshow(cat)
plt.colorbar()
cat[10: 110, 10: 110, :] = [255, 0, 0]
plt.imshow(cat)
plt.show()
