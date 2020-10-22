import cv2
import numpy as np

print("Package Imported")

'''
# 剪裁 重定义大小
img = cv2.imread("Resources/learn.png")
print(img.shape)

imgResize = cv2.resize(img, (500, 400))  # 重定义大小
imgCropped = img[0:200,200:500]  # 利用矩阵剪裁


cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)


cv2.waitKey(0)
'''

'''
# 膨胀腐蚀等基操
img = cv2.imread("Resources/learn.png")
kernel = np.ones((5, 5), np.uint8)


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像灰度化
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # 模糊图像 需添加内核
imgCanny = cv2.Canny(img, 150, 200)  # 边缘
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # 膨胀 迭代次数 1
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)  # 腐蚀

# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)


cv2.waitKey(0)

'''


'''
# 使用摄像头
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''



'''
# 读取图片
img = cv2.imread("Resources/learn.png")
cv2.imshow("Output",img)
cv2.waitKey(0)    # 等待按键
'''

'''
# 视频显示
# cap = cv2.VideoCapture("")
# 视频需要逐帧显示

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q')
        break

'''


