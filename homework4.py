from __future__ import print_function
from __future__ import division
import cv2
import random
import cv2 as cv
import numpy as np


alpha_slider_max = 90
title_window = 'Linear Blend'


def nothing(x):
    print(x)

src1 = cv.imread('boss.jpg', cv2.COLOR_BGR2RGB)
src2 = cv.imread('boss.jpg', cv2.COLOR_BGR2RGB)

extracted_color_img = np.zeros((100, 100, 3), np.uint8)
rgb = [0, 0, 0]
percentage = 0.1
p = 0.1
output = np.zeros(src1.shape, np.uint8)





rows, columns, channels = src1.shape

for i in range(rows):
    for j in range(columns):
        r = random.random()
        if r < percentage / 2:
            output[i][j] = [0, 0, 0]
        elif r < percentage:
            output[i][j] = [255, 255, 255]
        else:
            output[i][j] = src1[i][j]

def on_trackbar(val):
    print("We here")
    global percentage
    alpha = val / alpha_slider_max
    beta = (1.0 - alpha)
    dst = cv.addWeighted(output, alpha, output, beta, 0.0)
    cv.imshow(title_window, dst)
    #percentage = cv.getTrackbarPos(trackbar_name, title_window)

    #print(percentage)


cv.namedWindow(title_window)
trackbar_name = 'V 0'
cv.createTrackbar(trackbar_name, title_window, int(percentage*100), alpha_slider_max, on_trackbar)
on_trackbar(10)
# Wait until user press some key
cv.waitKey()
