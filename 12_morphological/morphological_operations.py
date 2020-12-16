import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("yazi.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal"),plt.show()

#erozyon
kernel = np.ones((5,5), dtype= np.uint8) #5x5lik 1'lerden oluşan matris

result = cv2.erode(img,kernel,iterations=1) # 1 kez erozyon uygulayacak
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon"),plt.show()
cv2.imwrite("erozyon.jpg",result)

#genişleme (dilation)
result2 = cv2.dilate(img,kernel,iterations=1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genişleme"),plt.show()
cv2.imwrite("genisleme.jpg",result2)

#beyaz gürültü
white_noise = np.random.randint(0,2,size = img.shape[:2])
white_noise = white_noise*255
plt.figure(), plt.imshow(white_noise, cmap = "gray"), plt.axis("off"), plt.title("Gürültü"),plt.show()

noisy_img = img + white_noise
plt.figure(), plt.imshow(noisy_img, cmap = "gray"), plt.axis("off"), plt.title("Gürültülü"),plt.show()
cv2.imwrite("gurultu_eklenen.jpg",noisy_img)

#açılma (erozyon+genişleme)
#beyaz gürültüyü azaltmak için kullanılır
opening = cv2.morphologyEx(noisy_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Açılma uygulanan"),plt.show()
cv2.imwrite("acilma_uygulanan.jpg",opening)

#siyah gürültü
black_noise = np.random.randint(0,2,size = img.shape[:2])
black_noise = black_noise*255
plt.figure(), plt.imshow(black_noise, cmap = "gray"), plt.axis("off"), plt.title("Gürültü2"),plt.show()

noisy_img2 = img + black_noise
noisy_img2[noisy_img <= -245] = 0
plt.figure(), plt.imshow(noisy_img2, cmap = "gray"), plt.axis("off"), plt.title("Gürültülü2"),plt.show()

#kapanma (genişleme+erozyon)
#siyah gürültüyü azaltmak için kullanılır
closing = cv2.morphologyEx(noisy_img2.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("Kapama uygulanan"),plt.show()

#gradyan (genişleme-erozyon)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.figure(), plt.imshow(gradient
, cmap = "gray"), plt.axis("off"), plt.title("Gradyan uygulanan"),plt.show()
cv2.imwrite("gradyan.jpg",gradient)