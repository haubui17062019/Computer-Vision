import numpy as np
import cv2
import os
from random import randint
import sqlite3



directory = r'D:\code python\recognize_face\data_train'

label = []
path = r'D:\code python\recognize_face\Train'
path0 = r'D:\code python\recognize_face\Test'


pathvideo = []
pathfolder = []
indexfolder = 0

def insertOrUpdate(id, name):
    conn = sqlite3.connect('Data.db')


    query = "SELECT * FROM `People` WHERE ID= " + str(id)
    cusror = conn.execute(query)

    isRecordExist = 0

    for row in cusror:
        isRecordExist = 1

    if (isRecordExist == 0):

        query ="INSERT INTO People('ID', 'Name') VALUES("+ str(id) + ",'" + str(name) + "')"
    else:
        query = "UPDATE People SET Name='" + name + "' WHERE ID=" + str(id)

    conn.execute(query)
    conn.commit()
    conn.close()

for i in os.listdir(directory):
    label.append(i)
    id = int(os.path.split(i)[1].split('.')[1])
    name = (os.path.split(i)[1].split('.')[0])


    yearofbirth = (os.path.split(i)[1].split('.')[0])
    # print(id, name, yearofbirth)
    insertOrUpdate(id, name)

    path1 = os.path.join(directory, i)

    pathfolder.append(path1)

print(pathfolder)

for i in pathfolder:
    # os.mkdir('D:\code_python\recogin_people\Train' + "\\" + str(label[indexfolder]))
    print(i)
    cap = cv2.VideoCapture(i)
    hear_face = cv2.CascadeClassifier()
    cnt = 1


    while True:
        _, img = cap.read()

        basename = os.path.basename(i)
        name_tuple = os.path.splitext(basename)
        filename = name_tuple[0]
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        if  cnt < 250:
            os.chdir(path)
            cv2.imwrite(str(filename) + '.' + str(cnt) + '.png', img)
        else:
            break
        cnt = cnt + 1




