import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# blurring (detayı azaltır, gürültüyü engeller)
#fotoğraftaki etkisini anlamak için fotoğrafta gürültü oluşturuyoruz
def gaussianNoise(image):
    row,col,ch = image.shape
    mean = 0
    var = 0.02 #varyans
    sigma = var**0.5

    gauss = np.random.normal(mean, sigma, (row,col,ch))
    noisy = image + gauss #gürültülü fotoğraf
    return noisy

#gürültüyü normalize edilmiş görüntüye ekleyebiliriz
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255 #genliği 0-255ten 0-1 e çevrilecek
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("normalize"),plt.show()

noisy_image = gaussianNoise(img)
plt.figure(),plt.imshow(noisy_image),plt.axis("off"),plt.title("gürültülü"),plt.show()

#tuz-karabiber gürültüsü
def saltpepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5 #beyaz ve siyah nokta oranı
    amount =0.004
    noisy = np.copy(image)
    #salt
    num_salt = int(np.ceil(amount * image.size * s_vs_p))
    coords = [np.random.randint(0,i-1,num_salt) for i in image.shape]
    noisy[coords] = 1
    #pepper
    num_pepper = int(np.ceil(amount * image.size * (1-s_vs_p)))
    coords = [np.random.randint(0,i-1,num_pepper) for i in image.shape]
    noisy[coords] = 0

    return noisy

spnoise = saltpepperNoise(img)
plt.figure(),plt.imshow(spnoise),plt.axis("off"),plt.title("siyah beyaz gürültülü"),plt.show()

#ortalama bulanıklaştırma yöntemi
dst = cv2.blur(noisy_image, ksize= (3,3))
#ksize = bulanıklaştırma için kutucuk boyutu
#kutucuktaki piksellerin ortalamasını alır
plt.figure()
plt.imshow(dst)
plt.axis("off")
plt.title("ortalama bulanıklık")
plt.show()

#gauss bulanıklaştırma
gb = cv2.GaussianBlur(noisy_image, ksize= (3,3), sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("gauss bulanıklık")
plt.show()

#medyan bulanıklaştırma
#kutucuktaki piksellerin medyanını alır
mb = cv2.medianBlur(spnoise.astype(np.float32), ksize= 3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("medyan bulanıklık")
plt.show()

#denoising
df = cv2.fastNlMeansDenoising(img,None,11, 7, 21)
plt.figure()
plt.imshow(df)
plt.axis("off")
plt.title("denoise")
plt.show()

sharp = unsharp_mask(df,amount=4.0)
plt.figure()
plt.imshow(sharp)
plt.axis("off")
plt.title("sharpened")
plt.show()

