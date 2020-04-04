import numpy as np
import cv2
import copy
from matplotlib import pyplot as plt

import matplotlib.colors as colors
import matplotlib.cm as cmx

np.seterr(divide='ignore', invalid='ignore')

# image read & pre processing (gray level & thresholding)
im = cv2.imread('00000048.png')
im2 = copy.deepcopy(im)
#print("im.shape", im.shape)
#print(im.dtype)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#print("imgray.shape", imgray.shape)
#print(imgray.dtype)
ret,thresh = cv2.threshold(imgray,127,255,0)
#print(thresh.shape)
#print(thresh.dtype)

# np zeros array creation
height = imgray.shape[0]
width = imgray.shape[1]
dim = (height, width)
zeros_array = np.zeros(dim).astype("uint8")
#print(zeros_array.shape)

# finding contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# drawing & displaying countours
#img = cv2.drawContours(im, contours, -1, (0,255,0), 1)
#cv2.imshow("Contour", img)
cnt = contours[0]
#print(cnt.shape)

# finding x y coordinates of contour
x = cnt[:,:,0]
x_flat = x.ravel()
y = cnt[:,:,1]
y_flat = y.ravel()
#print(x_flat)
#print(y_flat)
#print("x flat", x_flat, "\ny flat", y_flat)
#z = np.polyfit(x_flat, y_flat, 2)
#print(z)

'''
for i in range(1,len(x_flat)-1,1):
    print(x_flat[i-1:i+2])
'''
# windowing
#x_flat = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#y_flat = np.array([1, 2, 7, 4, 5, 6, 7, 8, 9, 10])
k_i_list = np.zeros(len(x_flat))
coordinates_list = []
k = 3
for i in range(k,len(x_flat)-k,1):
    #print(x_flat[i], y_flat[i])
    x_coordinate = x_flat[i]
    y_coordinate = y_flat[i]
    coordinates_list.append([y_coordinate, x_coordinate])

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



'''
plt.plot(x_flat,y_flat)
k_i = np.zeros(len(x_flat))
k_i[1] = 99
k_i[2] = 90
k_i[3] = 70

print(k_i)

color_map = plt.get_cmap('YlOrRd')
cNorm = colors.Normalize(vmin=0, vmax=99)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=color_map)

for i in range(len(x_flat)):
    colorVal = scalarMap.to_rgba(k_i[i])
    plt.plot(x_flat[i], y_flat[i], '.', color=colorVal)

plt.show()
'''

# heatmap = cv2.applyColorMap(thresh, cv2.COLORMAP_BONE)
# mn = min(k_i_list)
# mx = max(k_i_list)
# a = 100.0
# b = 200.0
# for index in range(len(k_i_list)):
#     val = k_i_list[index]
#     z = ((b-a)*(val-mn)/(mx-mn))+a
#     print(int(z))
#     y_coordinate = coordinates_list[index][0]
#     x_coordinate = coordinates_list[index][1]
#     #zeros_array[y_coordinate, x_coordinate] = int(z)
#     heatmap[y_coordinate, x_coordinate] = [0, int(z), 255]
#
# print(len(heatmap))
# for i in range(len(heatmap)):
#     print(i, "-------------")
#     print(heatmap[i])
#
#
# plt.imshow(heatmap)
# #plt.colorbar()
# plt.show()


'''
test = [1,2,3,4,5,6,7,8,9]
for i in range(len(test)):
    print("i", test[i])
    print("i-1", test[i-1])
    if(i == len(test)-1):
        print("i+1", test[0])
    else:
        print("i+1", test[i+1])
    print("---------------")

plt.imshow(imgray)
plt.colorbar()
plt.show()
'''

'''
a = [1,2,3,4,5,6,7,8,9]
for i in range(1,len(a)-1,1):
    print(a[i])
'''
'''
hell = [item for item in range(0,4)]
print(hell)
'''

'''
       (b-a)(x - min)
f(x) = --------------  + a
          max - min
'''
