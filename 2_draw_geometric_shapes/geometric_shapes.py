import cv2
import numpy as np

image = cv2.imread('apple.jpg',-1)
#image = np.zeros([512, 512, 3], np.uint8)
#tüm overwrite edilenleri görmemizi sağlar
image = cv2.line(image,(0,0),(255,255),(0,0,255),5)
#line overwrite
#parametreler(image,başlangıç,bitiş,(blue,green,red),kalınlık)
image = cv2.arrowedLine(image,(0,255),(255,255),(255,0,0),2)
image = cv2.rectangle(image,(384,0),(510,128),(0,0,255),5) #içi boş kare
#image = cv2.rectangle(image,(384,0),(510,128),(0,0,255),-1) #içi dolu kare
#parametrelerde başlangıç ve bitiş koordinatları çapraz iki köşededir
image = cv2.circle(image,(447,63),63,(0,255,0),-1)
#(image,orta nokta,radyan,renk,kalınlık)
font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image,'apple',(10,480),font,4,(255,255,255),7,cv2.LINE_AA)
#text overwrite
#(image,'metin',koordinat,yazı tipi,boyut,renk,kalınlık,çizgi tipi)
cv2.imshow('apple',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('apple_2.png',image)