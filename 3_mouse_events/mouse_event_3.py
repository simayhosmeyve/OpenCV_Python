import numpy as np
import cv2

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorimage = np.zeros((512,512,3),np.uint8)
        mycolorimage[:] = [blue,green,red]
        #tüm ekranı aynı renkle kaplar
        cv2.imshow('color',mycolorimage)
        #görüntüde tıklanan yerdeki rengi seçme
        

img = cv2.imread('apple.jpg')
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()