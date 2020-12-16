import cv2

image1 = cv2.imread("img1.png")
#image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) #renk skalasını değiştirme
image2 = cv2.imread("img2.png")
#image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print(image1.shape)
print(image2.shape)

#fotoğrafların boyutları eşitlensin
image1 = cv2.resize(image1, (600,400))
print(image1.shape)

image2 = cv2.resize(image2, (600,400))
print(image2.shape)


cv2.imshow("image1",image1)
cv2.waitKey(1000)

cv2.imshow("image2",image2)
cv2.waitKey(1000)

# karıştırılmış resim = alpha*image1 + beta*image2
#alpha ve beta saydamlıklarını belirler
blended = cv2.addWeighted(src1 = image1, alpha =0.5, src2= image2, beta = 0.5, gamma = 0)

cv2.imshow("birlesim",blended)
cv2.waitKey(2000)

cv2.imwrite('img3.png',blended)












