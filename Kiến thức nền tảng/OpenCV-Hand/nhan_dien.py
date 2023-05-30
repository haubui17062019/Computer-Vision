from unittest import result
import cv2
import numpy as np
import time
import mediapipe as mp
import os

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils



pTime = 0


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                if id == 12:
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                # #vẽ chấm tròn tại id =12
                # if id == 12:
                #     cv2.circle(img, (cx,cy), 15, (255, 0, 255), cv2.FILLED)


                    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            #handLms, , mpHands.HAND_CONNECTIONS
    

    #h, w, c = overlayList[0].shape
    #img[0:h, 0:w] = overlayList[0]
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (18,78), cv2.FONT_HERSHEY_PLAIN,3,
    (255,0,255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)