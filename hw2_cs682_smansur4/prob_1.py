import cv2
import math
import numpy as np

from matplotlib import pyplot as plt
from tkinter import filedialog
from tkinter import *

def on_mouse_over(event, x, y, flags, param):
    global img
    global dashboard
    if event == cv2.cv2.EVENT_MOUSEMOVE:
        img_reset()
        cv2.rectangle(img,(x-6, y-6), (x+6, y+6),(0,0,255),1)
        intensity = sum(img[y][x])/3
        window = img[y-5:y+5, x-5:x+5]
        mean, std = cv2.meanStdDev(window)
        str_coordinates = "x:{}, y:{}".format(x,y)
        str_rgb = "R:{},G:{},B:{}".format(img[y][x][2], img[y][x][1], img[y][x][0])
        str_intesity = "intensity:{}".format(sum(img[y][x])/3)
        str_mean = "mean: R:{} G:{} B:{}".format(mean[2],mean[1], mean[0])
        str_std = "standard deviation:" + "\n" + "R:{} G:{} B:{}".format(std[2],std[1], std[0])
        output_str = str_coordinates + "\n" + str_rgb + "\n" + str_intesity + "\n" + str_mean + "\n" + str_std
        y0, dy = 50, 50
        for i, line in enumerate(output_str.split('\n')):
            y = y0 + i*dy
            cv2.putText(dashboard, str(line), (20, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

def img_reset():
    global img
    global dashboard
    global filename
    #img = cv2.imread("testimage.png")
    img = cv2.imread(filename)
    dashboard = np.full((400,900), 255, dtype='uint8')
    cv2.imshow("dashboard", dashboard)
    cv2.imshow('image', img)

def channel_histogram():
    global img
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color = col)
        plt.xlim([0, 256])
    plt.show(block=False)


def main():
    global img
    global dashboard
    global filename

    #img = cv2.imread("testimage.png")

    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    filename = root.filename
    img = cv2.imread(filename)

    dashboard = np.full((400,900), 255, dtype='uint8')
    channel_histogram()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image",on_mouse_over)
    while(1):
        cv2.imshow("image", img)
        cv2.imshow("dashboard", dashboard)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

main()
