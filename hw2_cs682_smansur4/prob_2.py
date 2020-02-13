import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

def create_histograms(path):
    files = [file for file in glob.glob(path + "*")]
    files.sort()
    histograms = []
    for file in files:
            print(file)
            img = cv2.imread(file)
            img_uint16 = img.astype('uint16')
            b_channels = img_uint16[:, :, 0]
            g_channels = img_uint16[:, :, 1]
            r_channels = img_uint16[:, :, 2]
            img_bit_shifted = ((b_channels >> 5)<<6) + ((g_channels>>5)<<3) + (r_channels>>5)
            img_flat = img_bit_shifted.ravel()
            histogram, bins = np.histogram(img_flat,bins=range(0,513))
            histograms.append(histogram)
    return histograms

def histogram_intersection(h1, h2):
    intersection_val = np.true_divide(np.sum(np.minimum(h1,h2)), np.sum(np.maximum(h1,h2)))
    return intersection_val

def histogram_chi2(h1, h2):
    chi2_val = 0.0
    for i in range(0,512):
        if (h1[i]+h2[i]>0):
            chi2_val += (h1[i]-h2[i])**2/(h1[i]+h2[i])
    return chi2_val

def main():
    hist_intersect_1 = []
    hist_intersect_2 = []
    chi2_1 = []
    chi2_2 = []
    print("computing histograms")
    h = create_histograms('ST2MainHall4/')
    print("computing histogram intersection & chi square value ...")
    for i in range(0,99):
        for j in range(0,99):
            hist_intersect_2.append(histogram_intersection(h[i],h[j]))
            chi2_2.append(histogram_chi2(h[i],h[j]))
        hist_intersect_1.append(hist_intersect_2)
        chi2_1.append(chi2_2)
        hist_intersect_2 = []
        chi2_2 = []

    hist_intersection = np.array(hist_intersect_1)
    chi_square = np.array(chi2_1)

    #i_pos = [i for i in range(99)]
    #j_pos = [j for j in range(99)]

    #fig, ax = plt.subplots(figsize=(500, 250))
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, 99, 2))
    ax.set_yticks(np.arange(0, 99, 2))
    plt.setp(ax.get_xticklabels(), rotation=90, rotation_mode="anchor")

    ax.set_title("Image Pairs (Histogram Intersection)")
    plt.imshow(hist_intersection)
    plt.colorbar()
    plt.show()

    ax.set_title("Image Pairs (Chi2)")
    #plt.imshow(chi_square, cmap="Blues_r")
    plt.imshow(chi_square)
    plt.colorbar()
    plt.show()
main()
