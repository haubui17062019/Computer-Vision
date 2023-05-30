import cv2
import mediapipe as mp
import time
import pyautogui, sys
import math


# class creation
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, modelComplexity=1, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        # Send rgb image to hands
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    # Draw dots and connect them
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            # Which hand are we talking about
            myHand = self.results.multi_hand_landmarks[handNo]
            # Get id number and landmark information
            for id, lm in enumerate(myHand.landmark):
                # id will give id of landmark in exact index number
                # height width and channel
                h, w, c = img.shape
                # find the position
                cx, cy = int(lm.x * w), int(lm.y * h)  # center
                # print(id,cx,cy)
                lmlist.append([id, cx, cy])

                # Draw circle for 0th landmark
                if draw:
                    cv2.circle(img, (cx, cy), 15, (0, 0, 1), cv2.FILLED)
        return lmlist

    def fingersUp(self):
        fingers = []
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers


def main():
    # Frame rates
    width, height = 1280, 720
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    cap.set(3, width)
    cap.set(4, height)
    pTime = 0
    cTime = 0
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[8], lmList[11], lmList[4])
            ax = lmList[8][1]
            ay = lmList[8][2]
            bx = lmList[11][1]
            by = lmList[11][2]
            cx = lmList[4][1]
            cy = lmList[4][2]
            if math.sqrt((ax - bx) * (ax - bx) + (ay - by) * (ay - by)) <= 50:
                pyautogui.moveTo(51, 1054)
                pyautogui.click(button='left')
                time.sleep(1)
            if math.sqrt((cx - ax) * (cx - ax) + (cy - ay) * (cy - ay)) <= 40:
                pyautogui.moveTo(22, 1054)
                pyautogui.click(button='left')
                time.sleep(1)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Video", img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "_main_":
    main()