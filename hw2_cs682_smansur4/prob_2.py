import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

def ComputeHistograms(path):
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
            print(len(histogram), len(bins))
            histograms.append(histogram)
    return histograms

def main():
    ComputeHistograms('ST2MainHall4/')

main()
