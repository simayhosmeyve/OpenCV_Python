import cv2
import numpy as np 

img = cv2.imread("lenna.png")
cv2.imshow("Orijinal",img)
cv2.waitKey(0)

#yatay birleştirme
horizontal = np.hstack((img,img))
cv2.imshow("Yatay",horizontal),cv2.imwrite("Yatay.png",horizontal)
cv2.waitKey(0)


#dikey birleştirme
vertical = np.vstack((img,img))
cv2.imshow("Dikey",vertical),cv2.imwrite("Dikey.png",vertical)
cv2.waitKey(0)
