import cv2
import numpy as np

image = cv2.imread(r'C:\Users\Lenovo\Krishnaraj singh\Code\Opencv\1734083369576-i.webp')
gry = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

temp = cv2.imread(r'C:\Users\Lenovo\Krishnaraj singh\Code\Opencv\Screenshot 2025-11-29 103730.png')
gry1 = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)

#make a rectanlge for detect the image (image kisari chize dekhne k lie rectangle bna rhe h )


w,h = gry1.shape[::-1]

# print(gry1.shape)

res = cv2.matchTemplate(gry,gry1,cv2.TM_CCORR_NORMED)

print(res)
thre = 0.93


l = np.where(res>=thre)

for i in zip(*l[::-1]):
    cv2.rectangle(image,i,(i[0]+w,i[1]+h),(0,255,255),5)

image = cv2.resize(image,(600,500))

# cv2.imshow('wscode2',res)
cv2.imshow('wscode',image)
cv2.imshow('wscode1',temp)
cv2.waitKey(0)
cv2.destroyAllWindows()
