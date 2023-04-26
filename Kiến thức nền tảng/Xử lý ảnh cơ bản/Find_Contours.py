import cv2
import numpy as np

def get_background(cap):
    frame_indices = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=50)
    frames = []
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        frames.append(frame)
    median_frame = np.median(frames, axis=0).astype(np.uint8)
    return median_frame

def center(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x + x1
    cy = y + y1
    return cx, cy

cap = cv2.VideoCapture('video6.mp4')

first_frame = get_background(cap)


first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

detect = []


consecutive_frame = 2

while True:
    ret, frame = cap.read()

    value = 0



    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))



    difference = cv2.absdiff(first_frame, gray_frame)


    # if len(detect) == 0:
    #     first_frame = gray_frame

    _, difference = cv2.threshold(difference, 50, 255, cv2.THRESH_BINARY)

    # difference =cv2.erode(difference, kernel, iterations=1)
    difference = cv2.dilate(difference, kernel, iterations=1)


    # _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)




    contours, _ = cv2.findContours(difference, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 600:
            # cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cento = center(x, y, w, h)
            cv2.circle(frame, cento, 2, (0, 255, 0), -1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            if cento[0] > 100 and cento[0] < 500 and cento[1] > 100 and cento[1] < 400:
                value += 1

    cv2.rectangle(frame, (100, 100), (500, 400), (0, 255, 0), 1)
    cv2.putText(frame,  str('value: ') + str(value), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('difference', difference)


    if cv2.waitKey(50) == ord('q'):
        break