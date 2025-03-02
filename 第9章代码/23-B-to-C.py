import cv2
import matplotlib.pyplot as plt
import numpy as np

# 读取黑白图片
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
# 伪彩色处理（颜色映射）
colorized = cv2.applyColorMap(img, cv2.COLORMAP_JET)
# 保存结果
cv2.imwrite("mather_c.jpg", colorized)
img1 = cv2.imread("mather_c.jpg")
plt.imshow(img1)
plt.show()
