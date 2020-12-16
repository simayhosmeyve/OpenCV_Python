import cv2

img = cv2.imread("lenna.png")
print("Fotograf boyutu: ",img.shape)

cv2.imshow("Fotograf",img)
cv2.waitKey(1000)

#boyut değiştirme
resized_img = cv2.resize(img, (256,256))
cv2.imshow("Fotograf2",resized_img)
cv2.waitKey(1000)

#kırpma
cropped_img = img[:300,:400] 
#y ekseninde 0-300 ,x ekseninde 0-400 arası olan pikselleri aldık(y,x)
cv2.imshow("Fotograf3",cropped_img)
cv2.imwrite("Cropped.png",cropped_img)
cv2.waitKey(3000)
