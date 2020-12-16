import cv2

cap = cv2.VideoCapture(0) # 0 default kameradır

genislik = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
yukseklik =int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(genislik,yukseklik)

writer = cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(genislik,yukseklik)) 
#fourcc bir codec kodu ,windows için DIVX yazılır 
#20 oynatma hızı

while True:
    ret,frame = cap.read()
    cv2.imshow("Video",frame)

    #kamera kayıt
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()