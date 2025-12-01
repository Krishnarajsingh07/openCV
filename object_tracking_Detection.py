import cv2
import numpy as np

cap = cv2.VideoCapture(r'C:\Users\Lenovo\Krishnaraj singh\Code\Opencv\Man and woman jogging together on the street  1080p HD video  Copyright Free  Stock Videos - Stock Vlog (1080p, h264) (1).mp4')

ret,framee = cap.read()

x,y,w,h =400,99,400,885   # isko phle paint me jakr or fir apne hisab se adjust kr k dekhna pdega 

t = (x,y,w,h)
roi = frame[y:y+h,x:x+w]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi,np.array((0.,60.,32.)),np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
cv2.imshow('test',roi)

# termination point -- tr
tr = (cv2.TermCriteria_EPS | cv2.TERM_CRITERIA_COUNT,10,1)



while cap.isOpened():
    ret , frame = cap.read()
    
    if ret == True:
        hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # Search backimage
        d = cv2.calcBackProject([hsv_frame],[0],roi_hist,[0,180],1)
        r ,tp = cv2.CamShift(d,t,tr)    # ye resize hoga object k according 
        # r ,tp = cv2.meanShift(d,t,tr)
        x,y,w,h = tp
        final = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
        
        # cv2.imshow('Thisisframe',frame)
        cv2.imshow('Thisisframe',final)

        if cv2.waitKey(25) == ord('p'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
