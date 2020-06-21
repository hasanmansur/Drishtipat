import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# read gray image
img_gray = cv.imread('ST2MainHall4/a.png', 0)

# canny edge detection for gray image
edges_gray = cv.Canny(img_gray,100,200)

# show image & canny edge
cv.imshow("original_gray",img_gray)
cv.waitKey(0)
cv.imshow("gray_canny",edges_gray)
cv.waitKey(0)

# gradients for gray image
sobelx = cv.Sobel(img_gray,cv.CV_32F,1,0,ksize=5)
sobely = cv.Sobel(img_gray,cv.CV_32F,0,1,ksize=5)
mag, angle = cv.cartToPolar(sobelx, sobely, angleInDegrees=True)
angle_scaled_down = np.rint(angle/10)

'''
print("sobelx shape", sobelx.shape)
print("sobely shape", sobely.shape)
print("mag shape", mag.shape)
print("angle shape", angle.shape)
print(angle_scaled_down)
'''

#histogram of gradients
histr = cv.calcHist([angle_scaled_down], [0], None, [37], [0, 37])
plt.plot(histr)
plt.xlim([0, 36])
plt.show()
