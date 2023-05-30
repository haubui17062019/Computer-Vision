import cv2
import numpy as np
import Hand_Tracking_Module as htm
import di_chuyen_mouse as dcm
import time
import pyautogui, sys
import math

#import autopy




#################
wCam = 640
hCam = 480
##################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=1)




while True:
    # 1. find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw= False)


    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        #print(x1, y1)
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        length = math.hypot(x1 - x2, y1 - y2)


        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.circle(img, (cx, cy), 7, (0, 0, 255), cv2.FILLED)
        print(length)



        #print(x1, y1, x2, y2)



        fingers = detector.fingerUp()
        totalfingers = fingers.count(1)
        if totalfingers == 1:
            pyautogui.moveTo(3 * x1, 3 * y1)
        #print(fingers)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255,0,0), 3)
    # 12. display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
