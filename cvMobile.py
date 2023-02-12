import cv2
import numpy as np
url = "http://10.15.132.34:8080/video"
cp = cv2.VideoCapture(url)
while(True):
    camera, frame = cp.read()
    if frame is not None:
        
        cv2.putText(frame, 'AAA', (30,400), cv2.FONT_HERSHEY_TRIPLEX, 2.5, (127,127,255))
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()