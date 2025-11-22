import cv2
import numpy as np

def wscube(x):
    pass

new = np.zeros((500,500,3),np.uint8)*255

cv2.namedWindow('Color')
cv2.createTrackbar('R','Color',0,255,wscube)
cv2.createTrackbar('G','Color',0,255,wscube)
cv2.createTrackbar('B','Color',0,255,wscube)

while True:
    cv2.imshow('Color',new)

    if cv2.waitKey(1) == ord('p'):
        break

    r = cv2.getTrackbarPos('R','Color')
    g = cv2.getTrackbarPos('G','Color')
    b = cv2.getTrackbarPos('B','Color')

    new[:] = [b,g,r]


cv2.destroyAllWindows()
