import cv2;
import numpy as np;



cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)
cap.set(10,100)



myColor = [[5,107,0,19,255,255],
           [133,56,0,159,156,255],
           [64,50,136,155,255,255]]

myPoints = [] # [x, y]

def findColor(img):
    newPts = []
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array(myColor[2][:3])
    upper = np.array(myColor[2][3:6])
    mask = cv2.inRange(imgHsv, lower, upper)
    x,y =  getconters(mask)
    cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)
    if x!=0 and y!=0:
        newPts.append([x,y])
    # cv2.imshow("mask",mask)
    return newPts

def getconters(img):
    conter, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h =0,0,0,0
    for cnt in conter:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt,True)
        print(peri)
        aprox = cv2.approxPolyDP(cnt,0.02*peri,True)
        x,y,w,h = cv2.boundingRect(aprox)
    return x+w//2,y

def draeOnCanvas(myPts):
    for pt in myPts:
        cv2.circle(imgResult, (pt[0],pt[1]), 10, (255, 0, 0), cv2.FILLED)



while True:
    success,img = cap.read()
    imgResult = img.copy()
    newPts = findColor(img)
    if len(newPts)!=0:
        for newP in newPts:
            myPoints.append(newP)
    if len(myPoints)!=0:
        draeOnCanvas(myPoints)
    cv2.imshow("video", imgResult)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break











