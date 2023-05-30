import cv2
import mediapipe as mp
import pandas as pd


# doc anh tu webcam
cap = cv2.VideoCapture('jump.mp4')

# khoi tao mediapipe
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

lm_list = []
label = "jump"
no_of_frame = 600


def make_landmark_timestep(results):
    # print(results.pose_landmarks.landmark)
    list_ids = [
        mpPose.PoseLandmark.NOSE,
        mpPose.PoseLandmark.RIGHT_SHOULDER,
        mpPose.PoseLandmark.LEFT_SHOULDER,
        mpPose.PoseLandmark.LEFT_ELBOW,
        mpPose.PoseLandmark.RIGHT_ELBOW,
        mpPose.PoseLandmark.RIGHT_WRIST,
        mpPose.PoseLandmark.LEFT_WRIST,
        mpPose.PoseLandmark.LEFT_HIP,
        mpPose.PoseLandmark.RIGHT_HIP,
        mpPose.PoseLandmark.LEFT_KNEE,
        mpPose.PoseLandmark.RIGHT_KNEE,
        mpPose.PoseLandmark.LEFT_ANKLE,
        mpPose.PoseLandmark.RIGHT_ANKLE
    ]
    c_lm = []
    for id in (list_ids):
        lm = results.pose_landmarks.landmark[id]
        c_lm.append(lm.x)
        c_lm.append(lm.y)
        c_lm.append(lm.z)
        # c_lm.append(lm.visibility)
    return c_lm

def draw_landmark_on_image(mpDraw, results, img):
    # ve cac duong noi

    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    #ve cac diem nut
    for id, lm in enumerate(results.pose_landmarks.landmark):
        h, w, c = img.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(img, (cx, cy), 1, (0, 0, 255), cv2.FILLED)
    return img



while True:
    ret, frame = cap.read()
    if ret:
        # nhan dien pose
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frameRGB)
        if results.pose_landmarks:
            # ghi nhan thong so khung xuong
            lm = make_landmark_timestep(results)
            print(lm)
            lm_list.append(lm)
            # ve khung xuong len anh
            frame = draw_landmark_on_image(mpDraw, results, frame)

        cv2.imshow('image', frame)
        cv2.waitKey(1)

import os
# write vao csv
os.chdir('D:\codepython\mediapipe_action')
df = pd.DataFrame(lm_list)
df.to_csv(label + ".txt")
cap.release()
cv2.destroyAllWindows()
