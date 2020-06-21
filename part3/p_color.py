import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# read color image
img_color = cv.imread('ST2MainHall4/ST2MainHall4001.jpg')

# canny edge detection for color image
edges_color = cv.Canny(img_color,100,200)

# show color image & canny edge
cv.imshow("original_color",img_color)
cv.waitKey(0)
cv.imshow("color_canny",edges_color)
cv.waitKey(0)

# gradients for color image
sobelx = cv.Sobel(img_color,cv.CV_32F,1,0,ksize=5)
sobely = cv.Sobel(img_color,cv.CV_32F,0,1,ksize=5)
mag, angle = cv.cartToPolar(sobelx, sobely, angleInDegrees=True)

# combining magnitude of 3 channels
b_mag = np.square(mag[:, :, 0])
g_mag = np.square(mag[:, :, 1])
r_mag = np.square(mag[:, :, 2])
bgr_mag = np.sqrt(b_mag + g_mag + r_mag)
#print(bgr_mag.shape)

# combining angle of 3 channels
b_x = sobelx[:,:,0]
g_x = sobelx[:,:,1]
r_x = sobelx[:,:,2]
b_y = sobely[:,:,0]
g_y = sobely[:,:,1]
r_y = sobely[:,:,2]
bgr_x = b_x + g_x + r_x
bgr_y = b_y + g_y + r_y
bgr_angle_degree = (np.arctan2(bgr_y, bgr_x) * 180 / np.pi) + 360
bgr_angle_final = np.rint((bgr_angle_degree % 360)/10)
print(bgr_angle_final)

#histogram of gradients
# histr = cv.calcHist([bgr_angle_final], [0], None, [37], [0, 37])

print(bgr_angle_final.min())
print(bgr_angle_final.max())
hist, bins = np.histogram(bgr_angle_final, bins=36)
print(hist)
plt.plot(hist)
# plt.xlim([0, 36])
plt.show()
