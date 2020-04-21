import cv2

image = cv2.imread('apple.jpg', -1)  
#2. argüman görüntünün yükleniş şeklini belirler
#cv2.imread('apple.jpg', 1) renkli görüntü
#cv2.imread('apple.jpg', 0) gri tonlamalı görüntü 
#cv2.imread('apple.jpg', -1) değiştirilmemiş görüntü

print(image)
#görüntünün piksellere göre matrisini verir

cv2.imshow('apple', image) 
#görüntüyü gösterir

#cv2.waitKey(8000) 
#kaç milisaniye bekleyeceğini belirler
key = cv2.waitKey(0) 
#(özel durum)ekran kapatılana kadar hiç kapanmaz
if key==27: #enter tuşu ile kapatır
    cv2.destroyAllWindows()
#oluşturulan bütün pencerelerde gösterilir
elif key== ord('c'): #c tuşu ile görüntünün kopyasını oluşturur
    cv2.imwrite('apple_copy.png',image)
    cv2.destroyAllWindows()