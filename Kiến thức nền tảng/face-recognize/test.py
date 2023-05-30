import numpy as np
import cv2
import os
from random import randint
import sqlite3






path = r'D:\code python\recognize_face\CNN\training\mouse'



cap = cv2.VideoCapture('mouse.mp4')
hear_face = cv2.CascadeClassifier()
cnt = 1


while True:
    _, img = cap.read()


    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    if  cnt < 210:
        os.chdir(path)
        cv2.imwrite('mouse' + '.' + str(cnt) + '.png', img)
    else:
        break
    cnt = cnt + 1




