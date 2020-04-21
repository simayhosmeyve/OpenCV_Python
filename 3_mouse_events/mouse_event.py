import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)
#tüm mouse etkileşimlerini gösterir
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:#sol tıklandığında
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+ ',' + str(y)
        cv2.putText(img,strXY,(x,y),font,0.5,(255,255,0),2)
        cv2.imshow('image',img)
        #tıklanan yerin koordinatlarını gösterir
    if event == cv2.EVENT_RBUTTONDOWN:#sağ tıklandığında
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue)+ ',' + str(green)+','+str(red)
        cv2.putText(img,strBGR,(x,y),font,0.5,(0,255,255),2)
        cv2.imshow('image',img)
        #tıklanan yerin rengini verir

#img = np.zeros((512,512,3),np.uint8)
#siyah ekran verir
img = cv2.imread('apple.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.imwrite('coordinate_apple.png',img)
cv2.destroyAllWindows()