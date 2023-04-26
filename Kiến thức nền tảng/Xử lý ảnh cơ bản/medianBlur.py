import cv2
from IPython.display import Image
import matplotlib.pyplot as plt

path = 'anh1.jpg'
img_org = cv2.imread(path)
img_Blur = cv2.medianBlur(img_org, 3)
cv2.imshow('img_org', img_org)
cv2.imshow('img_Blur', img_Blur)
cv2.waitKey(0)