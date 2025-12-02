import cv2
import numpy as np

def click(event , x,y,f,p):  #
    if event == cv2.EVENT_LBUTTONDOWN:
        s = f"{x},{y}"
        cv2.putText(image,s,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0),1)
        cv2.imshow('mouse',image)

    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = image[y,x,0]
        green = image[y,x,1]
        red = image[y,x,2]
        # put text integet me nhi leta h vo string me leta h so string me change kiya hai
        s = f"{blue},{green},{red}"

        cv2.putText(image,s,(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1)
        cv2.imshow('mouse',image)

image = cv2.imread(r'C:\Users\Lenovo\Krishnaraj singh\Code\Opencv\1734083369576-i.webp')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('mouse',image)

#  ab krege mouse event function ko 

cv2.setMouseCallback('mouse',click)
cv2.waitKey(0)
cv2.destroyAllWindows()
