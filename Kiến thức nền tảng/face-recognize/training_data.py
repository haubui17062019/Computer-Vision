import cv2
import numpy as np
import os
from PIL import  Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'Train'


def getImageWithId(path):

    # lấy đường dẫn của tất cả các tệp trong thư mục
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')

        # tách để lấy ID của hình ảnh
        ID = int(os.path.split(imagePath)[1].split('.')[1])
        # print(ID)

        faces.append(faceNp)
        IDs.append(ID)

    return IDs, faces

Ids, faces = getImageWithId(path)

# training
recognizer.train(faces, np.array(Ids))

if not os.path.exists('recognizer'):
    os.makedirs('recognizer')

recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()
