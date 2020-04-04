import numpy as np
import cv2
import copy
import glob
from matplotlib import pyplot as plt

files = [file for file in glob.glob("GaitImages/" + "*")]
files.sort()
area_list = []
for file in files:
    print(file)
    # image read & pre processing (gray level & thresholding)
    im = cv2.imread(file)
    #im = cv2.imread('1.png')
    im2 = copy.deepcopy(im) # use for drawing poly. approx
    im3 = copy.deepcopy(im) # use for drawing convex hull
    im4 = copy.deepcopy(im) # use for drawing convexity defects
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)

    # contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
    #cv2.imshow("Contour", img)

    # polygonal approximation
    cnt = contours[0]
    epsilon = 0.01 * cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    img2 = cv2.drawContours(im2, [approx], 0, (0,0,255), 3)
    #cv2.imshow("Polygonal Approximation", img2)

    # convex hull
    hull1 = cv2.convexHull(cnt)
    img3 = cv2.drawContours(im3, [hull1], 0, (255,0,0), 3)
    #cv2.imshow("Convex Hull", img3)

    # convexity defects
    hull2 = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull2)
    if(defects is not None):
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            cv2.line(im4,start,end,[0,255,0],2)
            cv2.circle(im4,far,5,[0,0,255],-1)
        #cv2.imshow('Convexity Defects',im4)

    # moments, area, perimeter for original image
    print("---moments, area, perimeter for original image---")
    M = cv2.moments(cnt)
    #print(M)
    print("m10", M["m10"])
    print("m01", M["m01"])
    print("m20", M["m20"])
    print("m11", M["m11"])
    print("m02", M["m02"])
    o_area = cv2.contourArea(cnt)
    print("o_area", o_area)
    o_perimeter = cv2.arcLength(cnt,True)
    print("o_perimeter", o_perimeter)

    # moments, area, perimeter for convex hull
    print("---moments, area, perimeter for convex hull---")
    M1 = cv2.moments(hull1)
    #print(M1)
    print("m10", M1["m10"])
    print("m01", M1["m01"])
    print("m20", M1["m20"])
    print("m11", M1["m11"])
    print("m02", M1["m02"])
    h_area = cv2.contourArea(hull1)
    print("h_area", h_area)
    h_perimeter = cv2.arcLength(hull1,True)
    print("h_perimeter", h_perimeter)

    # write feature values into a file
    filename = "------------------------------------------" + str(file.split("/")[1]) + "----------------------------------------------------------------"
    line1 = "(original image) --> m10: {a} | m01: {b} | m20: {c} | m11 {d} | m02: {e} | area: {f} | perimeter: {g}".format(a=round(M["m10"],2),b=round(M["m01"],2),c=round(M["m20"],2),d=round(M["m11"],2),e=round(M["m02"],2),f=round(o_area,2),g=round(o_perimeter,2))
    line2 = "(convex hull)    --> m10: {h} | m01: {i} | m20: {j} | m11 {k} | m02: {l} | area: {m} | perimeter: {n}".format(h=round(M1["m10"],2),i=round(M1["m01"],2),j=round(M1["m20"],2),k=round(M1["m11"],2),l=round(M1["m02"],2),m=round(h_area,2),n=round(h_perimeter,2))
    f = open("resultfile_p2.txt", "a")
    f.write(filename)
    f.write( "\n")
    f.write(line1)
    f.write( "\n")
    f.write(line2)
    f.write( "\n")
    f.close()
    area_list.append(o_area)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# image vs area plot
plt.plot(range(len(files)), area_list)
plt.xlabel("images")
plt.ylabel("area")
plt.show()
