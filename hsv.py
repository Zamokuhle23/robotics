import cv as cv
import cv2
import numpy as np

def nothing(x):
    print(x)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        hsv_value = np.uint8([[[blue, green, red]]])
        hsv = cv2.cvtColor(hsv_value, cv2.COLOR_BGR2HSV)
        print("HSV : ", hsv)
        print("R: %s G: %s B %s" % (red,green,blue))
        print(hsv[0][0][2])
        extracted_color_img = np.zeros((100, 100, 3), np.uint8)
        extracted_color_img[:] = [blue, green, red]
        cv2.imshow('Extracted Color', extracted_color_img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('robot.png')
#cv2.namedWindow('img')
cv2.imshow('Image', img)
points = []
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()