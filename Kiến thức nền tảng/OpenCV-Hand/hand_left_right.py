import cv2
from cvzone.HandTrackingModule import HandDetector
import time

wCam = 640
hCam = 480
##################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = HandDetector(detectionCon=0, maxHands=2)
pTime = 0

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        lmList1  = hand1["lmList"] #21 điểm
        bbox1 = hand1["bbox"] #info x,y,w,h
        centerPoint1 = hand1["center"] #center of the hand cx, cy
        handType1 = hand1["type"] #type right left
        #fingers1 = detector.fingersUp(hand1)
        #print(len(lmList1))
        lengt, info, img = detector.findDistance(lmList1[8], lmList1[20], img)
        print(lengt, info)
        #print(lmList1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"
            #fingers2 = detector.fingersUp(hand2)
            #print(handType1, handType2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("img", img)
    cv2.waitKey(1)