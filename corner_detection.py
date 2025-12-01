# __Harris corner Detection__
#  jnha 2 edges milte h vo wale corner ko detect krta h ( junction ko detect krta haiiii)
import cv2
import numpy as np

# image = cv2.imread(r'C:\Users\Lenovo\Krishnaraj singh\Code\Opencv\shape.png')
image = cv2.imread(r'C:\Users\Lenovo\Krishnaraj singh\Code\Opencv\1734083369576-i.webp')
image = cv2.resize(image,(500,500))
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# isme aapko integer ko float me convert krna pdega

gray = np.float32(gray)

resut = cv2.cornerHarris(gray,4,3,0.04)

resut = cv2.dilate(resut,None)
print(resut)

image[resut>0.01*resut.max()] = [0,0,255]
 
# print(gray)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
