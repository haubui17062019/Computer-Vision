import threading

import cv2
import keras
import mediapipe as mp
import numpy as np
import pandas as pd


# doc anh tu webcam
cap = cv2.VideoCapture(0)

# khoi tao mediapipe
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

# load model
model = keras.models.load_model('model.h5')

lm_list = []
label= "...."
local = int()

def make_landmark_timestep(results):
    # print(results.pose_landmarks.landmark)
    c_lm = []
    for id, lm in enumerate(results.pose_landmarks.landmark):
        c_lm.append(lm.x)
        c_lm.append(lm.y)
        c_lm.append(lm.z)
        c_lm.append(lm.visibility)
    return c_lm

def draw_landmark_on_image(mpDraw, results, img):
    # ve cac duong noi
    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    #ve cac diem nut
    for id, lm in enumerate(results.pose_landmarks.landmark):
        h, w, c = img.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
    return img

def draw_class_on_image(label, img):
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomleftCornerOfText = (10, 30)
    fonScale = 1
    fontColor = (0, 255, 0)
    thickness = 2
    lineType = 2
    cv2.putText(img, label,
                bottomleftCornerOfText,
                font,
                fonScale, fontColor,
                thickness,
                lineType)
    return img

def detect(model, lm_list):
    global local
    lm_list = np.array(lm_list)
    lm_list = np.expand_dims(lm_list, axis=0)
    results = model.predict(lm_list)
    local = np.argmax(results[0])
    return local

actions = ['walking', 'jogging', 'upstaris', ' downstaris','sitting','standing']
i = 0
war = 60
while True:
    ret, frame = cap.read()
    # nhan dien pose
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    i=i+1
    if i > war:
        # print("Process Start")
        if results.pose_landmarks:
            # ghi nhan thong so khung xuong
            lm = make_landmark_timestep(results)
            lm_list.append(lm)

            if len(lm_list) == 10:
                # dua vao model
                t1 = threading.Thread(target=detect, args=(model, lm_list))
                t1.start()
                lm_list= []

            # ve khung xuong len anh
            frame = draw_landmark_on_image(mpDraw, results, frame)

        label = actions[local]

        draw_class_on_image(label, frame)

        cv2.imshow('image', frame)
        if cv2.waitKey(1) == ord('q'):
            break

# write vao csv


cap.release()
cv2.destroyAllWindows()
