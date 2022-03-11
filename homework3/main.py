from __future__ import print_function
from __future__ import division

import colorsys

import cv2 as cv
import numpy as np
import argparse
alpha_slider_max = 255
title_window = 'Linear Blend'

def nothing(x):
    print(x)
extracted_color_img = np.zeros((100, 100, 3), np.uint8)
hsv = [[[0,0,0]]]
rgb = [0,0,0]
def click_event(event, x, y, flags, param):
    global hsv,rgb
    if event == cv.EVENT_LBUTTONDOWN:
        blue = src1[y, x, 0]
        green = src1[y, x, 1]
        red = src1[y, x, 2]
        rgb = [blue,green,red]
        hsv_value = np.uint8([[[blue, green, red]]])
        hsv = cv.cvtColor(hsv_value, cv.COLOR_BGR2HSV)
        print("HSV : ", hsv)
        print("R: %s G: %s B %s" % (red,green,blue))
        print(hsv[0][0][2])

        extracted_color_img[:] = rgb
        cv.imshow('Extracted Color', extracted_color_img)


def on_trackbar(val):
    global rgb
    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
    cv.imshow(title_window, dst)
    v = cv.getTrackbarPos(trackbar_name, title_window)
    hsv[0][0][2] = v

    extracted_color_img[:] = [hsv[0][0][0],hsv[0][0][1],hsv[0][0][2]]
    hsvimage = colorsys.hsv_to_rgb(hsv[0][0][0],hsv[0][0][1],hsv[0][0][2])# picture with desired color.
    extracted_color_img[:] = [hsvimage]
    cv.imshow('Extracted Color', extracted_color_img)
parser = argparse.ArgumentParser(description='Code for Adding a Trackbar to our applications tutorial.')
parser.add_argument('--input1', help='Path to the first input image.', default='test.jpg')
parser.add_argument('--input2', help='Path to the second input image.', default='boss.jpg')
args = parser.parse_args()
src1 = cv.imread('robot.png')
src2 = cv.imread('robot.png')
if src1 is None:
    print('Could not open or find the image: ', args.input1)
    exit(0)
if src2 is None:
    print('Could not open or find the image: ', args.input2)
    exit(0)
cv.namedWindow(title_window)
trackbar_name = 'V 0'
cv.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)
# Show some stuff
points = []
cv.setMouseCallback(title_window, click_event)

on_trackbar(0)
# Wait until user press some key
cv.waitKey()