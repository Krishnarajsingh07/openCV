import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('wscube')
cv2.createTrackbar('Threshold','wscube',0,255,nothing)

cv2.createTrackbar('lb','wscube',0,255,nothing)
cv2.createTrackbar('lg','wscube',0,255,nothing)
cv2.createTrackbar('lr','wscube',0,255,nothing)
cv2.createTrackbar('hb','wscube',0,255,nothing)
cv2.createTrackbar('hg','wscube',0,255,nothing)
cv2.createTrackbar('hr','wscube',0,255,nothing)


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(200,200))

    if ret == True:

        
        LB = cv2.getTrackbarPos('lb','wscube')
        LG  = cv2.getTrackbarPos('lg','wscube')
        LR = cv2.getTrackbarPos('lr','wscube')
        hB = cv2.getTrackbarPos('hb','wscube')
        hG  = cv2.getTrackbarPos('hg','wscube')
        hR = cv2.getTrackbarPos('hr','wscube')
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        lower = np.array([LB,LG,LR])
        upper = np.array([hB,hG,hR])
        
        th = cv2.getTrackbarPos('Threshold','wscube')
        m = cv2.inRange(hsv,lower,upper)
        res =cv2.bitwise_and(frame,frame,mask=m)
        fr = cv2.bitwise_not(res)

        _,thi = cv2.threshold(m,th,255,cv2.THRESH_BINARY)
        cnt,hr = cv2.findContours(thi,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame,cnt,-1,(0,123,255),2)


        cv2.imshow('threr',thi)
        cv2.imshow('ress',res)
        cv2.imshow('mask',m)
        cv2.imshow('lie',hsv)
        cv2.imshow('live',frame)
        if cv2.waitKey(25) == ord('q'):
            break


    else:
        break


cap.release()
cv2.destroyAllWindows()
