import cv2

path_to_image = "boss.jpg"
image = cv2.imread(path_to_image,0)
(h,w) = image.shape[:2]

centerX, centerY = (w//2),(h//2)
topLeft = image[0:centerY, 0:centerX]
cv2.imshow('topLeft',topLeft)

topRight = image[0:centerY, centerX:w]
cv2.imshow('topRight',topRight)
cv2.imwrite('topRight.jpg',topRight)

bottomLeft = image[centerY:h,0:centerX]
cv2.imshow('bottomLeft',bottomLeft)
cv2.imwrite('bottomLeft.jpg',bottomLeft)

bottomRight = image[centerY:h,centerX:w]
cv2.imshow('bottomRight',bottomRight)
cv2.imwrite('bottomRight.jpg',bottomRight)

#cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
