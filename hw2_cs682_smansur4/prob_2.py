import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

def HistogramIntersection(h1, h2):
    sum1 = 0.0
    sum2 = 0.0
    minimum = np.minimum(h1,h2)
    maximum = np.maximum(h1,h2)
    sum10 = np.sum(minimum)
    sum20 = np.sum(maximum)
    intersection = np.true_divide(sum10, sum20)
    return intersection

def ComputeHistograms(path):
    files = [file for file in glob.glob(path + "*")]
    files.sort()
    histograms = []
    for file in files:
            #print(file)
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

def main():
    a_l = []
    b_l = []
    h = ComputeHistograms('ST2MainHall4/')
    HI = np.zeros((99,99),dtype='float')
    for i in range(0,99):
        for j in range(0,99):
            #HI[i,j] = HistogramIntersection(h[i],h[j])
            b_l.append(HistogramIntersection(h[i],h[j]))
        a_l.append(b_l)
        b_l = []

    i_pos = [i for i in range(0, 99)]
    j_pos = [j for j in range(0, 99)]
    val = np.array(a_l)

    fig, ax = plt.subplots()
    im = ax.imshow(val)

    cbarlabel = " "
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel(cbarlabel, rotation = -90, va="bottom")

    ax.set_xticks(np.arange(len(i_pos)))
    ax.set_yticks(np.arange(len(j_pos)))

    ax.set_xticklabels(i_pos)
    ax.set_yticklabels(j_pos)

    plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")

    #ax.set_title("Image Pairs (Histogram Intersection)")
    ax.set_title("Image Pairs (Chi-squared Measure)")#comment this line and uncomment the previous
    #line for Histogram intersection

    fig.tight_layout()
    plt.show()
main()
