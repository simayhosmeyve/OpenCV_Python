import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gri skalada gösteriyor
#gri skala renk tonlarının tespiti için kullanılıyor
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off") #x,y eksenlerini kapat
plt.show()

#eşikleme
retval,thres_img1 = cv2.threshold(img,thresh= 50,maxval= 255,type= cv2.THRESH_BINARY)
#60-255 arası değerleri beyaz yapıyor

plt.figure()
plt.imshow(thres_img1, cmap = "gray")
plt.axis("off") 
plt.show()

retval,thres_img2 = cv2.threshold(img,thresh= 50,maxval= 255,type= cv2.THRESH_BINARY_INV)
#60-255 arası değerleri siyah yapıyor

plt.figure()
plt.imshow(thres_img2, cmap = "gray")
plt.axis("off") 
plt.show()

#uyarlamalı eşik değeri
#belirli bölgeler ve nesneler için aynı fotoğraf içinde farklı yöntemler uygulama

thres_img3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
#cv2.adaptiveThreshold(orj_fotograf,uyarlamalı yöntem,tresh tipi,komşu piksel çokluğu,c sabiti)
#blockSize % 2 == 1 && blockSize > 1 (komşu piksel çokluğu)
plt.figure()
plt.imshow(thres_img3, cmap = "gray")
plt.axis("off") 
plt.show()

cv2.imwrite("thres_img1.jpg",thres_img1)
cv2.imwrite("thres_img2.jpg",thres_img2)
cv2.imwrite("thres_img3.jpg",thres_img3)