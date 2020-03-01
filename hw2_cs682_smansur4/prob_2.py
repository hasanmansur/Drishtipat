import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

np.seterr(divide='ignore', invalid='ignore')

def create_histograms(files):
    histograms = []
    for file in files:
            print(file)
            img = cv2.imread(file).astype('uint16')
            b_channels, g_channels, r_channels = img[:, :, 0], img[:, :, 1], img[:, :, 2]
            img_bit_shifted = (b_channels >> 5) + ((g_channels >> 5) << 3) + ((r_channels >>5) << 6)
            img_flat = img_bit_shifted.ravel()
            histogram, bins = np.histogram(img_flat,bins=range(0,513))
            histograms.append(histogram)
    return histograms

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
    hist_intersect_1 = []
    hist_intersect_2 = []
    chi2_1 = []
    chi2_2 = []

    files = [file for file in glob.glob("ST2MainHall4/" + "*")]
    files.sort()

    print("computing histograms")
    h = create_histograms(files)
    print("computing histogram intersection & chi square measure ...")
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

    g_max = 255
    hist_intersection_scaled = g_max * hist_intersection
    chi_square_scaled = g_max * (chi_square/max(chi_square.ravel()))
    #chi_square_scaled = (255-255*(chi_square-min(chi_square.ravel()))/(max(chi_square.ravel())-min(chi_square.ravel())))

    plot(plt, hist_intersection_scaled, "Histogram intersection")
    plot(plt, chi_square_scaled, "Chi-squared measure")

main()
