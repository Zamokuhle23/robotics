from __future__ import print_function
from __future__ import division
import cv2
import random
import cv2 as cv
import numpy as np

<<<<<<< HEAD

alpha_slider_max = 90
title_window = 'Linear Blend'


def nothing(x):
    print(x)
=======
alpha_slider_max = 90
title_window = 'Salt and Paper'
>>>>>>> origin/main

src1 = cv.imread('boss.jpg', cv2.COLOR_BGR2RGB)
src2 = cv.imread('boss.jpg', cv2.COLOR_BGR2RGB)

extracted_color_img = np.zeros((100, 100, 3), np.uint8)
rgb = [0, 0, 0]
<<<<<<< HEAD
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
=======
percentage = 0.5
output = np.zeros(src1.shape, np.uint8)


def on_trackbar(val):
    global percentage
    alpha = val / alpha_slider_max
    beta = (1.0 - alpha)

    percentage = (cv.getTrackbarPos(trackbar_name, title_window))/100
    #print(percentage)
    salt()

    dst = cv.addWeighted(output, alpha, output, beta, 0.0)
    median_using_cv2 = cv2.medianBlur(output, 3)
    gaussian_using_cv2 = cv2.GaussianBlur(output, (3, 3), 0, borderType=cv2.BORDER_CONSTANT)
    bilateral_using_cv2 = cv2.bilateralFilter(output, 5, 20, 100, borderType=cv2.BORDER_CONSTANT)

    cv.imshow(title_window, dst)
    cv.imshow("Median", median_using_cv2)
    cv2.imshow("Using cv2 gaussian", gaussian_using_cv2)
    cv2.imshow("cv2 bilateral", bilateral_using_cv2)


def salt():
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

    print(percentage)
>>>>>>> origin/main


cv.namedWindow(title_window)
trackbar_name = 'V 0'
<<<<<<< HEAD
cv.createTrackbar(trackbar_name, title_window, int(percentage*100), alpha_slider_max, on_trackbar)
=======
cv.createTrackbar(trackbar_name, title_window, 10, alpha_slider_max, on_trackbar)
>>>>>>> origin/main
on_trackbar(10)
# Wait until user press some key
cv.waitKey()
