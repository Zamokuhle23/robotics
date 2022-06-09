import numpy as np
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc

font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 50)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2
cap = cv2.VideoCapture(0)
video = VideoWriter('webcam.mp4', VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))
text = input("Enter Text to be displayed: ")
while True:
    ret, frame = cap.read()
    #image = np.zeros(frame.shape, np.uint8)
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.putText(image,text,org, font,fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('frame', image)
    video.write(image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
video.release()