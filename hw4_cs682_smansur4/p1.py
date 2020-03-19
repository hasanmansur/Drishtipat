import numpy as np
import cv2
import copy

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
epsilon = 0.01*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
img2 = cv2.drawContours(im2, [approx], 0, (0,0,255), 3)
cv2.imshow("Contour Approximation", img2)

# computing moments, area, perimeter for original image
M = cv2.moments(cnt)
print(M)
area = cv2.contourArea(cnt)
print(area)
perimeter = cv2.arcLength(cnt,True)
print(perimeter)
cv2.waitKey(0)
