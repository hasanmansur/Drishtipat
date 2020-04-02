import numpy as np
import cv2
import copy
from matplotlib import pyplot as plt

# image read & pre processing (gray level & thresholding)
im = cv2.imread('1.png')
im2 = copy.deepcopy(im)
print(im.shape)
print(im.dtype)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
print(imgray.shape)
print(imgray.dtype)
ret,thresh = cv2.threshold(imgray,127,255,0)
print(thresh.shape)
print(thresh.dtype)

# finding contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# drawing & displaying countours
img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.imshow("Contour", img)

# Contour Approximation
cnt = contours[0]
print("cnt", cnt)
#print(cnt.shape)

#print(img)
#print("img", img[2,39])


epsilon = 0.01*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
print("approx", approx.shape)
print(approx)
img2 = cv2.drawContours(im2, [approx], 0, (0,0,255), 3)
cv2.imshow("Contour Approximation", img2)

#plt.imshow(img2)
#plt.colorbar()
#plt.show()

# computing moments, area, perimeter for original image
M = cv2.moments(cnt)
print(M)
area = cv2.contourArea(cnt)
print(area)
perimeter = cv2.arcLength(cnt,True)
print(perimeter)

# convex hull
hull1 = cv2.convexHull(cnt)
print(hull1.shape)
# Convexity Defects
hull2 = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull2)

# computing moments, area, perimeter for convex hull
M = cv2.moments(hull1)
print(M)
area = cv2.contourArea(hull1)
print(area)
perimeter = cv2.arcLength(hull1,True)
print(perimeter)


cv2.waitKey(0)
