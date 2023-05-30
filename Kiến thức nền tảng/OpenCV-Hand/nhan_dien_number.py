import cv2
import time
import os
import mediapipe as mp

import HandTracking as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

folderPath = "FingerImage"
myList = os.listdir(folderPath)
print(myList)

overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    #print(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0)

tipIds=[4,8,12,16,20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=True)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(len(lmList) )


    #print(lmList)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                #vẽ chấm tròn tại id =12
                if id == 12:
                    cv2.circle(img, (cx,cy), 15, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            # print("Index finger open")
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                #print("Index finger open")
                fingers.append(1)
            else:
                fingers.append(0)



        #print(fingers)
        totalFingers = fingers.count(1)
        #print(totalFingers)

        h, w, c = overlayList[0].shape
        # img[0:194, 0:295] = overlayList[0]
        #cv2.rectangle(img, (20,255), (178, 425), (0,255,0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (0,100), cv2.FONT_HERSHEY_PLAIN,
                    8, (255,0,0), 15)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime



    cv2.putText(img, f'FPS: {int(fps)}', (480, 70), cv2.FONT_HERSHEY_PLAIN,
    3, (255,0,0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)