import cv2
import time

video_name = "sokak_video.mp4"

#video içe aktarma capture 
cap = cv2.VideoCapture(video_name)

print("Genislik: ",cap.get(3))
print("Yükseklik: ",cap.get(4))

#video olmasa bile yüklenir ve çalışır
#videonun düzgün yüklendiğini kontrol etmeliyiz
if cap.isOpened() == False:
    print("Hata")

while True:
    ret,frame = cap.read()
    if ret == True:
        #time.sleep(0.01)  #yavaşlatır
        cv2.imshow("Video",frame)
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):  #q tuşu ile kapatır
        break
cap.release()
cv2.destroyAllWindows()