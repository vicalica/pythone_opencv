import cv2
import numpy as np
# 使用numpy创建矩阵

# img = np.zeros((512,512))
# 若是想添加颜色就必须要三通道 BGR

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
# img[:] = 255,0,0  # 变蓝色
# img[200:300, 100:300] = 255, 0, 0  # 区域变蓝

# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)  #最后是宽度
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 300), (0, 0, 255),cv2.FILLED)
cv2.rectangle(img, (0, 0), (250, 300), (0, 0, 255),cv2.FILLED)
# 最后是宽度 cv2.FILLED 直接填充

cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
# 画圆

cv2.putText(img,"open",(300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0))


cv2.imshow("Image",img)
cv2.waitKey(0)