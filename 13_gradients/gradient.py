import cv2
import matplotlib.pyplot as plt

#Bir gradyan görüntünün belirli bir yönünde yoğunluktaki değişimi ölçer.
#Böylece kenar algılamada kullanılabilir
img = cv2.imread("sudoku.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal"),plt.show()

#x gradyanı
#y eksenindeki kenarları tespit eder
sobelx = cv2.Sobel(img,ddepth=cv2.CV_16S,dx=1,dy=0,ksize=5)
plt.figure(), plt.imshow(sobelx, cmap = "gray"), plt.axis("off"), plt.title("SobelX"),plt.show()

#y gradyanı
#x eksenindeki kenarları tespit eder
sobely = cv2.Sobel(img,ddepth=cv2.CV_16S,dx=0,dy=1,ksize=5)
plt.figure(), plt.imshow(sobely, cmap = "gray"), plt.axis("off"), plt.title("SobelY"),plt.show()

#laplace gradyanı
#iki yönlü kenar tespiti
laplacian = cv2.Laplacian(img,ddepth=cv2.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("Laplace"),plt.show()
#cv2.imwrite("laplace_gradyani.jpg",laplacian)
