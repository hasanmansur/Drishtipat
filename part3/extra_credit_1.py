import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#-----------------------color image---------------------------------------------
img_color = cv.imread("./ST2MainHall4/ST2MainHall4001.jpg")

# gradients for color image
sobelx = cv.Sobel(img_color,cv.CV_32F,1,0,ksize=5)
sobely = cv.Sobel(img_color,cv.CV_32F,0,1,ksize=5)

# splitting & combining 3 channels
b_x = sobelx[:,:,0]
g_x = sobelx[:,:,1]
r_x = sobelx[:,:,2]
b_y = sobely[:,:,0]
g_y = sobely[:,:,1]
r_y = sobely[:,:,2]
bgr_x = b_x + g_x + r_x
bgr_y = b_y + g_y + r_y

# downscaling the image size for faster computation
bgr_x = bgr_x[::50, ::50]
bgr_y = bgr_y[::50, ::50]
print(bgr_x.shape, bgr_y.shape)

# plotting
fig, ax = plt.subplots()
ax.quiver(bgr_x, bgr_y)
ax.set(aspect=1, title='Quiver Plot: Color Gradients')
plt.show()
