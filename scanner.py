import cv2
import numpy as np

image = cv2.imread('istockphoto-827255150-612x612.jpg')

# directly crop straight line me krta h 

# cv2.circle(image,(283,67),4,(0,0,255),-1)
# cv2.circle(image,(492,79),4,(0,0,255),-1)
# cv2.circle(image,(265,360),4,(0,0,255),-1)
# cv2.circle(image,(475,372),4,(0,0,255),-1)

w,h = 500,600

src1 = np.float32([[283,67],[492,79],[265,360],[475,372]])
destination  =np.float32([[0,0],[w,0],[0,h],[w,h]])

m=cv2.getPerspectiveTransform(src1,destination)

new_image = cv2.warpPerspective(image,m,(w,h))

print(image.shape)
cv2.imshow('krishna',new_image)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
