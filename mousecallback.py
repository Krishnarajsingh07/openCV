import cv2
import numpy as np


def python(event,x,y,f,p):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(shape,(x,y),6,(23,65,87),3)
    elif event ==cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(shape,(x,y),(x+12,y+12),(25,64,43),3)


shape = np.ones((500,500,3),np.uint8)*255

cv2.namedWindow('krishna')

cv2.setMouseCallback('krishna',python)


while True:
    cv2.imshow('krishna',shape)
    if cv2.waitKey(25) == ord('p'):
        break
    
    


cv2.destroyAllWindows()
