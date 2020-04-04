import numpy as np
import cv2
import copy
from matplotlib import pyplot as plt

import matplotlib.colors as colors
import matplotlib.cm as cmx

np.seterr(divide='ignore', invalid='ignore')

# image read & pre processing (gray level & thresholding)
im = cv2.imread('GaitImages/00000048.png')
im2 = copy.deepcopy(im)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

# np zeros array creation
height = imgray.shape[0]
width = imgray.shape[1]
dim = (height, width)
zeros_array = np.zeros(dim).astype("uint8")
#print(zeros_array.shape)

# finding contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# finding x y coordinates of contour
x = cnt[:,:,0]
x_flat = x.ravel()
y = cnt[:,:,1]
y_flat = y.ravel()

#x_flat = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#y_flat = np.array([1, 2, 7, 4, 5, 6, 7, 8, 9, 10])

# windowing
k_i_list = np.zeros(len(x_flat))
k = 3

for i in range(k,len(x_flat)-k,1):
    #print(x_flat[i], y_flat[i])

    t_window = [index for index in range(i-k, i+k+1)]
    x_window = x_flat[i-k:i+k+1]
    y_window = y_flat[i-k:i+k+1]

    cooeffs_xt = np.polyfit(x_window, t_window, 2)
    cooeffs_yt = np.polyfit(y_window, t_window, 2)
    a2 = cooeffs_xt[0]
    a1 = cooeffs_xt[1]
    a0 = cooeffs_xt[2]
    b2 = cooeffs_yt[0]
    b1 = cooeffs_yt[1]
    b0 = cooeffs_yt[2]
    #print(a1,a1,a0,b2,b1,b0)
    k_i = abs(2*(a1*b2-b1*a2) / pow((pow(a1,2)+pow(b1,2)),1.5))
    #print(k_i)
    k_i_list[i] = k_i

#print(k_i_list)

mn = min(k_i_list)
mx = max(k_i_list)
a = 0
b = 99
for index in range(len(k_i_list)):
     val = k_i_list[index]
     z = ((b-a)*(val-mn)/(mx-mn))+a
     #print(int(z))
     k_i_list[index] = z

#print(k_i_list)

# plotting
plt.plot(x_flat, y_flat)

# YlOrRd
color_map = plt.get_cmap('YlOrRd')
cNorm = colors.Normalize(vmin=0, vmax=99)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=color_map)

for i in range(len(x_flat)):
    colorVal = scalarMap.to_rgba(k_i_list[i])
    plt.plot(x_flat[i], y_flat[i], '.', color=colorVal, markersize=20)
plt.gca().invert_yaxis()
plt.title("curvature estimation (k = " + str(k) + ")")
plt.show()
