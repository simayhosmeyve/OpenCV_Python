import cv2
import numpy as np

img = cv2.imread("kart.png")
cv2.imshow("Orijinal", img)
cv2.waitKey(1000)

width = 400
height = 500

#kartın köşelerinin koordinatlarını giriyoruz
points1 = np.float32([[203,1],[1,472],[540,146],[340,618]]) #olan köşeler
points2 = np.float32([[0,0],[0, height],[width,0],[width,height]]) #olması gereken köşeler

matrix = cv2.getPerspectiveTransform(points1, points2)
print(matrix)

imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("Yeni fotograf", imgOutput)
cv2.waitKey(1000)
cv2.imwrite('kart2.png',imgOutput)