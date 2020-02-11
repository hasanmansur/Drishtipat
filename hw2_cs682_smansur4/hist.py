# histograms of images in ST2MailHall
from os import listdir
from os.path import isfile, join
import numpy as np
import cv2
import matplotlib.pyplot as plt
import fnmatch

def HistogramIntersection(h1, h2):
    sum1 = 0.0
    sum2 = 0.0
    for i in range(0,512):
        if (h1[i]+h2[i]>0):
            sum1 = sum1 + min(h1[i],h2[i])
            sum2 = sum2 + max(h1[i],h2[i])

    minimum = np.minimum(h1,h2)
    #print(minimum)
    maximum = np.maximum(h1,h2)
    sum10 = np.sum(minimum)
    sum20 = np.sum(maximum)
    #print (sum1, sum10, sum2, sum20)

    return sum1/sum2

def HistogramChi2(h1, h2):
    sum1 = 0.0
    for i in range(0,512):
        h11 = h1[i]
        h22 = h2[i]
        if (h11+h22>5):
            sum1 = sum1+(h11-h22)**2/(h11+h22)
    return sum1

def ComputeHistograms(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    hist = []
    onlyfiles.sort()
    for f in onlyfiles:
            name = join('ST2MainHall4/',f)
            #print(name)
            img = cv2.imread(name)
            b, g, r = cv2.split(img)
            b1 = b.astype('uint16')
            g1 = g.astype('uint16')
            r1 = r.astype('uint16')
            in1 = ((b1 >> 5)<<6) + ((g1>>5)<<3) + (r1>>5)
            x = in1.shape
            in2 = in1.reshape([x[0]*x[1],1])
            h2, bins = np.histogram(in2,bins=range(0,513))
            #print(h2)
            #break
            hist.append(h2)
    return hist

def main():
    h = ComputeHistograms('ST2MainHall4/')
    HI = np.zeros((99,99),dtype='float')
    HCHI2 = np.zeros((99,99),dtype='float')
    for i in range(0,98):
        HI[i,i] = 1.0
        HCHI2[i,i] = 0.0;
        for j in range(i+1,99):
            #print(i,j)
            HI[i,j] = HistogramIntersection(h[i],h[j])
    print("HI", HI)

if __name__ == '__main__':
   main()
