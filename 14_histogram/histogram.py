import cv2
import matplotlib.pyplot as plt
import numpy as np

#Görüntü histogramı, ton dağılımının grafiksel bir temsili
img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis),plt.show()
print(img.shape)

img_hist = cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure(), plt.plot(img_hist),plt.show()
print(img_hist.shape)

#renklendirilmiş histogram
color = ("b","g","r")
plt.figure()
for i, c in enumerate(color):
    hist =cv2.calcHist([img],channels=[i],mask=None,histSize=[256],ranges=[0,256])
    plt.plot(hist,color=c)
plt.show()

#Fotoğraf 2
golden_gate = cv2.imread("goldenGate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(golden_gate_vis)    
    
print(golden_gate.shape)

#Maskeleme
mask = np.zeros(golden_gate.shape[:2], np.uint8) #siyahlaştırma
#plt.figure(), plt.imshow(mask, cmap = "gray")  

mask[1500:2000, 1000:2000] = 255 #istenilen bölgeyi beyazlaştırma
#plt.figure(), plt.imshow(mask, cmap = "gray") 

#birleştirip sadece istediğimiz bölgeyi görüyoruz
masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask = mask)
plt.figure(), plt.imshow(masked_img_vis, cmap = "gray"),plt.show()

masked_img = cv2.bitwise_and(golden_gate, golden_gate, mask = mask)
masked_img_hist = cv2.calcHist([golden_gate], channels = [0], mask = mask, histSize = [256], ranges = [0,256])
#channels = [0] -> kırmızı grafiği RGB'ye göre 0,1,2 kullanabiliriz
plt.figure(), plt.plot(masked_img_hist),plt.show()

#histogram eşitleme
#kontrast arttırmaya yarar

#Fotoğraf 3
img = cv2.imread("hist_equ.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"),plt.show()

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist),plt.show()

#eşitlenmiş histogramda grafikteki yoğunluk dağılımı artıyor
eq_hist = cv2.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist, cmap = "gray"),plt.show()

eq_img_hist = cv2.calcHist([eq_hist], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(eq_img_hist),plt.show()
