import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import glob

np.seterr(divide='ignore', invalid='ignore')

def compute_canny_gradients_hog(files):
    hogs_gray = []
    hogs_color = []
    for file in files:
            print(file)
            #------------------FILE read---------------------------------------
            # read color image
            img_color = cv.imread(file)
            # convert to gray image
            img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

            #-------------------------------------------------------------------
            # --------------------------------GRAY------------------------------
            #-------------------------------------------------------------------
            # canny edge detection for gray image
            edges_gray = cv.Canny(img_gray,100,200)

            # gradients for gray image
            sobelx = cv.Sobel(img_gray,cv.CV_32F,1,0,ksize=5)
            sobely = cv.Sobel(img_gray,cv.CV_32F,0,1,ksize=5)
            mag, angle = cv.cartToPolar(sobelx, sobely, angleInDegrees=True)
            angle_scaled_down = np.rint(angle/10)

            # histogram of gradients
            hist, bins = np.histogram(angle_scaled_down, bins=37)

            # append in hog list
            hogs_gray.append(hist)

            #-------------------------------------------------------------------
            # --------------------------------COLOR-----------------------------
            #-------------------------------------------------------------------
            # canny edge detection for color image
            edges_color = cv.Canny(img_color,100,200)

            # gradients for color image
            sobelx = cv.Sobel(img_color,cv.CV_32F,1,0,ksize=5)
            sobely = cv.Sobel(img_color,cv.CV_32F,0,1,ksize=5)
            mag, angle = cv.cartToPolar(sobelx, sobely, angleInDegrees=True)

            # splitting & combining 3 channels
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
            #print(bgr_angle_final)
            #print(bgr_angle_final.min())
            #print(bgr_angle_final.max())

            # histogram of gradients
            hist, bins = np.histogram(bgr_angle_final, bins=37)

            # append in hog list
            hogs_color.append(hist)

    return {"hogs_gray": hogs_gray, "hogs_color": hogs_color}
    #return hogs_color

def histogram_intersection(h1, h2):
    intersection_val = np.true_divide(np.sum(np.minimum(h1,h2)), np.sum(np.maximum(h1,h2)))
    return intersection_val

def histogram_chi2(h1, h2):
    chi2_val = np.nansum(np.true_divide(np.square(np.subtract(h1, h2)), np.add(h1, h2)))
    return chi2_val

def plot(plt, matrix, title):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, 99, 8))
    ax.set_yticks(np.arange(0, 99, 8))
    plt.setp(ax.get_xticklabels(), rotation=90, rotation_mode="anchor")
    ax.set_title(title)
    plt.imshow(matrix)
    plt.colorbar()
    plt.show()

def main():
    # lists for color hlistograms & chi square
    hist_intersect_color_1 = []
    hist_intersect_color_2 = []
    chi2_color_1 = []
    chi2_color_2 = []

    # lists for gray hlistograms & chi square
    hist_intersect_gray_1 = []
    hist_intersect_gray_2 = []
    chi2_gray_1 = []
    chi2_gray_2 = []

    files = [file for file in glob.glob("ST2MainHall4/" + "*")]
    files.sort()

    print("computing canny edge, image gradients & histogram of gradients for both color & gray images ... ")
    h = compute_canny_gradients_hog(files)
    hogs_color = h["hogs_color"]
    hogs_gray = h["hogs_gray"]
    print("computing histogram intersection & chi square measure ...")
    for i in range(0,99):
        for j in range(0,99):
            hist_intersect_color_2.append(histogram_intersection(hogs_color[i],hogs_color[j]))
            chi2_color_2.append(histogram_chi2(hogs_color[i],hogs_color[j]))
            hist_intersect_gray_2.append(histogram_intersection(hogs_gray[i],hogs_gray[j]))
            chi2_gray_2.append(histogram_chi2(hogs_gray[i],hogs_gray[j]))

        hist_intersect_color_1.append(hist_intersect_color_2)
        chi2_color_1.append(chi2_color_2)
        hist_intersect_gray_1.append(hist_intersect_gray_2)
        chi2_gray_1.append(chi2_gray_2)

        hist_intersect_color_2 = []
        chi2_color_2 = []
        hist_intersect_gray_2 = []
        chi2_gray_2 = []

    hist_intersection_color = np.array(hist_intersect_color_1)
    chi_square_color = np.array(chi2_color_1)
    hist_intersection_gray = np.array(hist_intersect_gray_1)
    chi_square_gray = np.array(chi2_gray_1)

    '''
    # scaling
    g_max = 255
    hist_intersection_color_scaled = g_max * hist_intersection_color
    chi_square_color_scaled = g_max * (chi_square_color/max(chi_square_color.ravel()))

    plot(plt, hist_intersection_color_scaled, "Histogram intersection")
    plot(plt, chi_square_color_scaled, "Chi-squared measure")
    '''

    plot(plt, hist_intersection_color, "Histogram intersection: Color Images")
    plot(plt, chi_square_color, "Chi-squared measure: Color Images")
    plot(plt, hist_intersection_gray, "Histogram intersection: Gray Images")
    plot(plt, chi_square_gray, "Chi-squared measure: Gray Images")

main()
