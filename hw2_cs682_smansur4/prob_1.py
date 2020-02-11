import cv2
import math
import numpy as np

from matplotlib import pyplot as plt
from tkinter import filedialog
from tkinter import *

def on_mouse_over(event, x, y, flags, param):
    global img
    global gray
    if event == cv2.cv2.EVENT_MOUSEMOVE:
        print("------------------")
        img_reset()
        cv2.rectangle(img,(x-6, y-6), (x+6, y+6),(255,255,255),1)
        print("p: x,y", x,y)
        print("p: rgb", img[y][x][2], img[y][x][1], img[y][x][0])
        intensity = sum(img[y][x])/3
        print("p: intensity", intensity)
        window = gray[y-5:y+5, x-5:x+5]
        mean, std = cv2.meanStdDev(window)
        print("window mean", mean)
        print("window std", std)

def img_reset():
    global img
    img = cv2.imread('testimage.png')
    #print("cleaned")
    cv2.imshow('image', img)

def channel_histogram():
    global img
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color = col)
        plt.xlim([0, 256])
    plt.show()

#to handle image file with dialogbox
#root = Tk()
#root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
#img = cv2.imread('testimage.png')
#img = cv2.imread(root.filename)

img = cv2.imread("testimage.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

channel_histogram()
cv2.namedWindow("image")
cv2.setMouseCallback("image",on_mouse_over)

while(1):
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
