import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

np.seterr(divide='ignore', invalid='ignore')

img = cv.imread("./ST2MainHall4/ST2MainHall4001.jpg")

imgDiffX = cv.Sobel(img, cv.CV_32F, 1, 0)
imgDiffY = cv.Sobel(img, cv.CV_32F, 0, 1)

imgDiffXY = cv.multiply(imgDiffX, imgDiffY)
imgDiffXX = cv.multiply(imgDiffX, imgDiffX)
imgDiffYY = cv.multiply(imgDiffY, imgDiffY)

a = imgDiffXX[:,:,0] + imgDiffXX[:,:,1] + imgDiffXX[:,:,2]
b = imgDiffXY[:,:,0] + imgDiffXY[:,:,1] + imgDiffXY[:,:,2]
c = imgDiffYY[:,:,0] + imgDiffYY[:,:,1] + imgDiffYY[:,:,2]

b_square = b * b
ac = a * c
a_plus_c = a + c
a_plus_c_square = a_plus_c * a_plus_c
lambda1 = ((a_plus_c + np.sqrt(a_plus_c_square - 4 * (b_square - ac))))/2
lambda2 = ((a_plus_c - np.sqrt(a_plus_c_square - 4 * (b_square - ac))))/2

#print("lambda1",lambda1)
#print("lambda2",lambda2)
a_minus_lambda1 = a - lambda1
b_neg = b * (-1)
x = b_neg / a_minus_lambda1
#print(x.shape)

bgr_angle_degree = (np.arctan2(1, x) * 180 / np.pi) + 360
bgr_angle_final = np.rint((bgr_angle_degree % 360))
bgr_angle_final[np.isnan(bgr_angle_final)] = 0
print(bgr_angle_final.min())
print(bgr_angle_final.max())

hist, bins = np.histogram(bgr_angle_final, bins=18)

plt.plot(hist)
plt.title("Histogram of color gradients: using eigenvalues and eigenvectors")
plt.xlabel("angles(in degrees)")
plt.ylabel("number of edges selected")
plt.show()
